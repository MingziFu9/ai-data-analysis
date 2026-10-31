# 人工智能数据分析与处理

面向成人教育人工智能技术应用专业（专科）的《人工智能数据分析与处理》网络教材，从系列模板 `ai-textbook-template` 生成。网页版：https://mingzifu9.github.io/ai-data-analysis/

- 4 学分，72 学时（线上理论 40 + 线上实验 18 + 线下理论 14），第 4 学期，期末开卷
- 12 章，每章 3 个实验，共 36 个；面向几乎没有编程经验的学生，★ 实验给出完整代码，读懂、运行、改参数
- 贯穿案例：虚构的广州美食点评平台“食客说”，数据由 `labs/data/make_datasets.py` 生成
- 对应证书：人工智能训练师（四级）、人工智能数据处理工程师（中级）、Python 技术应用工程师（中级），见 `docs/certificate.md`
- 动笔和修改前先读 `编写规范.md`

## 目录结构

| 路径 | 内容 |
|---|---|
| `course.yml` | 课程配置（书名、学时、章节、证书），改完运行 `python tools/course.py sync` |
| `docs/chapters/` | 各章正文，目录名 `NN-英文短名` |
| `docs/appendix/` | 附录 A 零基础入门、B 工具速查、C 实验环境与数据、D 术语表、E 报告与规范模板 |
| `docs/sims/` | 16 个交互动画，公共样式在 `common/` |
| `docs/learning-graph/` | 学习图谱（`data.js`），`concepts-draft.csv` 是概念与先修关系表 |
| `docs/faq/`、`docs/certificate.md`、`docs/mock-exam.md` | 常见问题、证书考点对照、在线模拟卷 |
| `labs/` | 按章存放的实验代码；`labs/data/` 为数据，见 `labs/data/README.md` |
| `slides/`、`lesson-plans/` | 课件和教案的底稿 |
| `tools/` | 维护脚本 |

## 维护脚本

```bash
python tools/glossary_links.py anchors     # 给术语表每个术语加锚点
python tools/glossary_links.py link 03     # 第 3 章正文中的术语改成悬停可见定义的链接
python tools/glossary_links.py concepts 03 # 生成第 3 章的“本章概念清单”
python tools/build_graph.py                # 由概念表和术语表生成学习图谱 data.js
python tools/graph_text.py                 # 检查学习图谱并生成文字版
python tools/make_mock_exam.py             # 从各章课后练习组成两套在线模拟卷 docs/mock-exam.md
python tools/book_stats.py                 # 更新首页“全书概览”统计表
python tools/course.py sync                # 按 course.yml 更新导航、首页、章节骨架等
python tools/course.py new-sim 名称 3 "标题" # 新建第 3 章的交互动画骨架
python tools/export_docx.py --pdf          # 导出 Word 版和 PDF 版到 build/（需要 pandoc 和 LibreOffice）
```

## 课件、教案和 Word/PDF 版

```bash
pip install -r requirements-tools.txt      # 第一次：Python 库
npm install && npx playwright install chromium   # 第一次：渲染配图用的 Node 库和浏览器
npm run figures                            # 把 Mermaid 图和交互动画渲染成图片（课件、Word 版要用）

python tools/make_slides.py draft 3        # 从第 3 章正文生成课件底稿 slides/ch03.md，精简后再 build
python tools/make_slides.py build 3        # → build/课件/第03章 章名.pptx（all 表示全部章节）
python tools/make_lesson_plan.py draft 3   # 生成教案底稿 lesson-plans/ch03.yml，补写“【待填】”后再 build
python tools/make_lesson_plan.py build 3   # → build/教案/第03章 章名 教案.docx
python tools/export_docx.py --pdf          # → build/书名.docx 和 .pdf，动画换成截图和二维码
```

本机不想装这些工具时，在 GitHub 仓库的 **Actions → 导出课件、教案和 Word/PDF → Run workflow** 运行一次，几分钟后在运行页面底部的 Artifacts 下载全部文件。底稿（`slides/`、`lesson-plans/`）要提交到仓库，生成的文件不提交。

## 本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve          # 浏览器打开 http://127.0.0.1:8000
mkdocs build --strict # 提交前确认没有警告
```

## 说明

书中运行结果均为编者实测；需要 GPU、联网下载模型或调用大模型 API 的部分标为“待实测”，并附记录表。数据集来源与许可见 `labs/data/README.md`，仅用于教学。
