#!/usr/bin/env python
"""Extract a PDF with OpenAI, one page per API call.

This script is intentionally not local OCR. Local work is limited to splitting
the source PDF into one-page PDFs and writing markdown outputs. OpenAI reads
each page.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from pypdf import PdfReader, PdfWriter


RESPONSES_URL = "https://api.openai.com/v1/responses"


PAGE_PROMPT = """You are extracting a scanned scientific-writing teaching PDF one page at a time.

Rules:
- Work only on the current page.
- Do not skip headings, bullets, labels, examples, captions, or body text.
- Preserve the reading order and hierarchy.
- Transcribe readable text first; then extract practical writing principles.
- Mark uncertain text as [unclear]. Never invent missing text.
- Be detailed. The purpose is to prepare a durable reference for a writing skill, not a brief summary.

Return markdown with exactly these sections:
# Page {page_number}
## Transcription
## Writing Principles
## Style / Structure Notes
## Unclear Areas
"""


def load_api_key_from_env_file(start_dir: Path) -> str | None:
    for directory in [start_dir, *start_dir.parents]:
        env_file = directory / ".env.local"
        if not env_file.exists():
            continue
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, value = line.split("=", 1)
            if name.strip() == "OPENAI_API_KEY":
                return value.strip().strip('"').strip("'")
    return None


def parse_pages(spec: str | None, page_count: int) -> list[int]:
    if not spec:
        return list(range(1, page_count + 1))
    pages: set[int] = set()
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            start_s, end_s = chunk.split("-", 1)
            start, end = int(start_s), int(end_s)
            pages.update(range(start, end + 1))
        else:
            pages.add(int(chunk))
    bad = [p for p in pages if p < 1 or p > page_count]
    if bad:
        raise ValueError(f"Invalid pages for a {page_count}-page PDF: {sorted(bad)}")
    return sorted(pages)


def split_page(reader: PdfReader, page_number: int, output_path: Path) -> None:
    writer = PdfWriter()
    writer.add_page(reader.pages[page_number - 1])
    with output_path.open("wb") as f:
        writer.write(f)


def extract_text_from_response(payload: dict) -> str:
    if isinstance(payload.get("output_text"), str):
        return payload["output_text"].strip()

    parts: list[str] = []
    for item in payload.get("output", []):
        for content in item.get("content", []):
            text = content.get("text")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(parts).strip()


def call_openai(
    *,
    api_key: str,
    model: str,
    page_pdf: Path,
    page_number: int,
    page_count: int,
    timeout: int,
) -> str:
    encoded = base64.b64encode(page_pdf.read_bytes()).decode("ascii")
    prompt = PAGE_PROMPT.format(page_number=page_number)
    prompt += f"\n\nCurrent page: {page_number} of {page_count}."

    body = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {
                        "type": "input_file",
                        "filename": page_pdf.name,
                        "file_data": f"data:application/pdf;base64,{encoded}",
                    },
                ],
            }
        ],
    }

    request = urllib.request.Request(
        RESPONSES_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API HTTP {exc.code}: {detail}") from exc

    text = extract_text_from_response(payload)
    if not text:
        raise RuntimeError(f"No text returned for page {page_number}")
    return text


def call_openai_with_curl(
    *,
    api_key: str,
    model: str,
    page_pdf: Path,
    page_number: int,
    page_count: int,
    timeout: int,
) -> str:
    curl = shutil.which("curl.exe") or shutil.which("curl")
    if not curl:
        return call_openai(
            api_key=api_key,
            model=model,
            page_pdf=page_pdf,
            page_number=page_number,
            page_count=page_count,
            timeout=timeout,
        )

    encoded = base64.b64encode(page_pdf.read_bytes()).decode("ascii")
    prompt = PAGE_PROMPT.format(page_number=page_number)
    prompt += f"\n\nCurrent page: {page_number} of {page_count}."
    body = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {
                        "type": "input_file",
                        "filename": page_pdf.name,
                        "file_data": f"data:application/pdf;base64,{encoded}",
                    },
                ],
            }
        ],
    }

    request_json = page_pdf.with_suffix(".request.json")
    request_json_for_curl = str(request_json).replace("\\", "/")
    request_json.write_text(json.dumps(body), encoding="utf-8")
    curl_config = "\n".join(
        [
            f'url = "{RESPONSES_URL}"',
            'request = "POST"',
            f'header = "Authorization: Bearer {api_key}"',
            'header = "Content-Type: application/json"',
            f'data = "@{request_json_for_curl}"',
            "silent",
            "show-error",
            "fail-with-body",
            f"max-time = {timeout}",
            "",
        ]
    )
    try:
        completed = subprocess.run(
            [curl, "--config", "-"],
            input=curl_config,
            text=True,
            capture_output=True,
            timeout=timeout + 30,
            check=False,
        )
    finally:
        try:
            request_json.unlink()
        except FileNotFoundError:
            pass

    if completed.returncode != 0:
        stderr = completed.stderr.strip()
        stdout = completed.stdout.strip()
        raise RuntimeError(f"curl failed with exit {completed.returncode}: {stderr}\n{stdout}")

    payload = json.loads(completed.stdout)
    text = extract_text_from_response(payload)
    if not text:
        raise RuntimeError(f"No text returned for page {page_number}")
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="Source PDF path.")
    parser.add_argument("--out", required=True, help="Output directory.")
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", "gpt-4.1"))
    parser.add_argument("--pages", help="Pages to process, e.g. 1-5,8,10. Default: all.")
    parser.add_argument("--resume", action="store_true", help="Skip pages with existing output.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Seconds between API calls.")
    parser.add_argument("--timeout", type=int, default=180, help="HTTP timeout per page.")
    parser.add_argument("--retries", type=int, default=2, help="Retries per page after API/network failure.")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY") or load_api_key_from_env_file(Path.cwd())
    if not api_key:
        print("OPENAI_API_KEY is not set and .env.local was not found.", file=sys.stderr)
        return 2

    pdf_path = Path(args.pdf).resolve()
    out_dir = Path(args.out).resolve()
    pages_dir = out_dir / "pages"
    single_page_dir = out_dir / "_single_page_pdfs"
    pages_dir.mkdir(parents=True, exist_ok=True)
    single_page_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(pdf_path))
    page_count = len(reader.pages)
    pages = parse_pages(args.pages, page_count)

    manifest = {
        "source_pdf": str(pdf_path),
        "model": args.model,
        "page_count": page_count,
        "pages": pages,
        "method": "one OpenAI Responses API call per single-page PDF; no local OCR",
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    completed: list[Path] = []
    for page_number in pages:
        page_output = pages_dir / f"page-{page_number:03d}.md"
        if args.resume and page_output.exists() and page_output.read_text(encoding="utf-8").strip():
            print(f"skip page {page_number}: existing output")
            completed.append(page_output)
            continue

        page_pdf = single_page_dir / f"page-{page_number:03d}.pdf"
        split_page(reader, page_number, page_pdf)
        text = None
        for attempt in range(1, args.retries + 2):
            try:
                print(f"extract page {page_number}/{page_count} with {args.model} (attempt {attempt})")
                text = call_openai_with_curl(
                    api_key=api_key,
                    model=args.model,
                    page_pdf=page_pdf,
                    page_number=page_number,
                    page_count=page_count,
                    timeout=args.timeout,
                )
                break
            except Exception as exc:
                if attempt > args.retries:
                    raise
                print(f"page {page_number} failed attempt {attempt}: {exc}", file=sys.stderr)
                time.sleep(max(args.sleep, 2.0) * attempt)
        assert text is not None
        page_output.write_text(text.rstrip() + "\n", encoding="utf-8")
        completed.append(page_output)
        time.sleep(args.sleep)

    combined = out_dir / "nature-masterclass-gpt-extraction.md"
    with combined.open("w", encoding="utf-8") as f:
        f.write("# Nature Masterclass GPT Extraction\n\n")
        f.write("Each page was processed in a separate OpenAI API call. No local OCR was used.\n\n")
        for page_output in sorted(pages_dir.glob("page-*.md")):
            f.write(page_output.read_text(encoding="utf-8").rstrip())
            f.write("\n\n---\n\n")

    print(f"combined output: {combined}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
