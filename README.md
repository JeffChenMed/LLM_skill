# LLM Skill Library

这是我的个人 LLM skill 与工作流知识库，用来沉淀医学科研写作、论文润色、文稿格式化和论文汇报 PPT 生成相关的方法。

## 目录

- `skills/ajhg-polishing-skill/`：AJHG / Cell 风格的医学科研英文润色 skill，包含 AJHG Perspective PDF 风格参考。
- `skills/czf-writing-skill/`：CZF 文稿写作总控 skill，按“科学结构 -> 语言润色 -> Word 格式化”的顺序组织工作。
- `skills/czf-cover-skill/`：高影响力 biomedical / translational medicine cover letter 起草、润色和审查 skill，使用 CZF 三问结构，并支持 PUMCH/Nan Wu DOCX cover-letter template。
- `skills/czf-formatting-skill/`：CZF 文稿 Word 格式化 skill，包含格式参考文件。
- `skills/nature-masterclass-writing-skill/`：基于 Nature Masterclass 思路的科研论文结构化写作 skill，包含原始 Nature Masterclass PDF 参考。
- `skills/nature-figure/`：Nature / high-impact journal 风格科研图制作与审查 skill，支持 Python 和 R 工作流。
- `skills/codex-ppt/`：生成视觉统一的图片型 PPT/PPTX 汇报 deck 的 skill。
- `skills/_shared/`：多个 skill 共享的术语、原则或辅助材料。
- `THINKING.md`：这些 skill 背后的设计思路和工作原则。

## 使用方式

把需要使用的 skill 目录复制或同步到当前电脑用户的 Codex skills 目录中。不要写死任何 Windows 绝对用户目录，因为不同电脑的用户名不同。

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills"
```

在 Windows PowerShell 中安装指定 skill 的例子：

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

$skills = @(
  "ajhg-polishing-skill",
  "czf-writing-skill",
  "czf-cover-skill",
  "czf-formatting-skill",
  "nature-masterclass-writing-skill",
  "codex-ppt"
)

foreach ($name in $skills) {
  Copy-Item -LiteralPath "skills\$name" -Destination $dest -Recurse
}
```

在 macOS / Linux 中，Codex skills 目录通常是：

```bash
~/.codex/skills
```

每个 skill 的主要入口是对应目录下的 `SKILL.md`。如果 skill 包含 `assets/`、`references/` 或 `static/`，这些文件应与 `SKILL.md` 一起保留。安装或更新 skill 后，重启 Codex 以加载新内容。

## 维护原则

- 每个 skill 解决一个明确工作场景。
- 把稳定原则写进 `SKILL.md`，把长材料、参考标准和可选细节放入 `references/` 或 `static/`。
- 不在 skill 中保存账号、token、API key、患者身份信息或未脱敏数据。
- 更新 skill 后，同步更新本仓库，保留可追踪的版本历史。
