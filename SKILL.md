---
name: docx-master
description: "Professional Word document processing skill - combines the advantages of minimax-docx and docx-official, providing complete document creation, editing, formatting and AI intelligent analysis functions. Supports font, paragraph, page format control, style management, AI intelligent analysis (document structure analysis, text correction, format optimization). Use this skill when users mention Word documents, docx, official document typesetting, academic papers, document formatting, font settings, paragraph typesetting, etc."
license: MIT
metadata:
  version: "1.0.0"
  category: document-processing
  author: OpenCode
---

# 📝 docx-master

**🎯 Professional Word Document Processing Skill** - Combines the advantages of minimax-docx and docx-official, providing complete document creation, editing, formatting and AI intelligent analysis functions.

## ✨ Features

### 🚀 Core Functions
- **📄 Document Creation**: Create professional Word documents from scratch, supporting multiple templates
- **✏️ Document Editing**: Modify existing document content while preserving formatting
- **🎨 Format Control**: Precisely control fonts, paragraphs, page formats
- **📐 Style Management**: Create, modify, apply custom styles
- **🤖 AI Integration**: Integrate DeepSeek API for intelligent analysis and optimization

### 🎨 Format Control
- **🔤 Font settings**: Chinese and English fonts, font size, color, bold, italic, etc.
- **📝 Paragraph format**: alignment, line spacing, indentation, spacing, etc.
- **📐 Page settings**: paper size, margins, headers and footers, etc.
- **📊 Table format**: borders, alignment, cell styles, etc.

## 📋 Format Standards (重要)

### 🎯 Default Format Rules (默认格式规则)
- **段前间距**: 0磅 (space_before=0)
- **段后间距**: 0磅 (space_after=0)
- **首行缩进**: 2字符 (first_line_indent_chars=2)，所有段落统一
- **行间距**: 22磅固定值 (line_spacing=22, line_spacing_rule='exact')
- **标题格式**: 居中，首行缩进2字符，行距22磅
- **公文行间距**: 28磅固定值 (line_spacing=28, line_spacing_rule='exact')

### 📜 公文格式标准（GB/T 9704）
| 项目 | 格式 |
|------|------|
| 📄 纸张 | A4 (210×297mm) |
| 📏 页边距 | 上3.7cm、下3.5cm、左2.8cm、右2.6cm |
| 📝 标题 | 方正小标宋简体 二号（22pt），居中，行距28磅 |
| 📑 一级标题 | 黑体 三号（16pt） |
| 📋 二级标题 | 楷体 三号（16pt） |
| 📃 三级标题 | 仿宋 三号（16pt）加粗 |
| 📄 四级标题 | 仿宋 三号（16pt） |
| 📝 正文 | 仿宋 三号（16pt），首行缩进2字符，行距28磅 |
| ✍️ 落款 | 右空四字，阿拉伯数字日期 |
| 📖 页码 | 宋体小四号（12pt），居中，-X-格式 |

### 🔢 公文序号规则
- **一级标题**: 一、二、三、...（中文数字+顿号）
- **二级标题**: （一）（二）（三）...（中文数字+括号）
- **三级标题**: 1. 2. 3. ...（阿拉伯数字+点）
- **四级标题**: （1）（2）（3）...（阿拉伯数字+括号）

### 🔤 字体要求
| 字体 | 用途 |
|------|------|
| 方正小标宋简体 | 公文标题 |
| 黑体/SimHei | 一级标题 |
| 楷体/楷体_GB2312 | 二级标题 |
| 仿宋/仿宋_GB2312 | 正文、三级标题、四级标题 |
| 宋体/SimSun | 页码 |

### ✍️ 落款格式
- **发文机关署名**: 右空四字
- **成文日期**: 右空四字，阿拉伯数字格式（如：2026年7月21日）

### 📖 页码格式
- **格式**: -X-（短横线-数字-短横线）
- **位置**: 页面底部居中
- **字体**: 宋体小四号（12pt）

## 🚀 Usage Scenarios (使用情境)

### 📝 1. 制作公文，自动调取公文格式
当用户提到"公文"、"通知"、"报告"等公文相关词汇时，自动应用GB/T 9704公文格式标准：
```python
from core.document import DocumentManager
from core.ai_integration import AIIntegration

# 创建文档管理器
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# 添加内容
doc_manager.add_paragraph("关于XXX的通知")
doc_manager.add_paragraph("这是正文内容。")

# 使用AI分析并自动应用公文格式
ai = AIIntegration()
ai.analyze_and_apply_format(doc_manager, target_style="公文")

# 保存文档
doc_manager.save_document("official_document.docx")
```

### 📄 2. 发送了格式要求，能自主按照格式调整文档
当用户发送具体的格式要求时，解析并应用：
```python
from core.document import DocumentManager
from core.ai_integration import AIIntegration

# 用户输入格式要求
user_input = "请将文档行距设置为28磅，首行缩进2字符，两端对齐，标题居中"

# 打开文档
doc_manager = DocumentManager()
doc_manager.open_document("input.docx")

# 使用AI分析文档结构并应用格式
ai = AIIntegration()
analysis = ai.analyze_structure({
    "paragraphs": [{"index": i, "text": p.text} for i, p in enumerate(doc_manager.document.paragraphs)]
})

# 根据分析结果应用格式
ai.apply_format_by_analysis(doc_manager, analysis)

# 保存文档
doc_manager.save_document("output.docx")
```

### 📄 3. 没有要求，按照默认格式输出word
当用户没有明确格式要求时，自动应用默认格式：
```python
from core.document import DocumentManager
from core.formatting import FormattingManager

def apply_default_format(doc_manager):
    """应用默认格式"""
    fm = FormattingManager(doc_manager.document)
    
    for para in doc_manager.document.paragraphs:
        # 判断是否为标题
        if para.style.name.startswith('Heading') or para.alignment == WD_ALIGN_PARAGRAPH.CENTER:
            # 标题格式：居中，首行缩进2字符，行距22磅
            fm.set_paragraph_format(
                para,
                alignment='center',
                first_line_indent_chars=2,
                line_spacing=22,
                line_spacing_rule='exact',
                space_before=0,
                space_after=0
            )
        else:
            # 正文格式：两端对齐，首行缩进2字符，行距22磅
            fm.set_paragraph_format(
                para,
                alignment='justify',
                first_line_indent_chars=2,
                line_spacing=22,
                line_spacing_rule='exact',
                space_before=0,
                space_after=0
            )

# 创建文档
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# 添加内容
doc_manager.add_paragraph("这是标题")
doc_manager.add_paragraph("这是正文内容。")

# 应用默认格式
apply_default_format(doc_manager)

# 保存文档
doc_manager.save_document("output.docx")
```

## 📦 Install Dependencies

```bash
pip install python-docx requests
```

## 🔑 Environment Variables (Optional)

Set DeepSeek API key to enable AI functions:

```bash
# Windows
set DEEPSEEK_API_KEY=your-api-key

# Linux/Mac
export DEEPSEEK_API_KEY=your-api-key
```

## 🚀 Quick Start

### 1. 📄 Create New Document

```python
from core.document import DocumentManager

# Create document manager
doc_manager = DocumentManager()

# Create new document
doc = doc_manager.create_document()

# Add content
doc_manager.add_heading("Document Title", level=0)
doc_manager.add_paragraph("This is the body text.")

# Save document
doc_manager.save_document("output.docx")
```

### 2. ✏️ Open and Edit Existing Document

```python
from core.document import DocumentManager

# Open document
doc_manager = DocumentManager()
doc_manager.open_document("input.docx")

# Replace text
doc_manager.replace_text("old text", "new text")

# Save document
doc_manager.save_document("output.docx")
```

### 3. 🎨 Set Format

```python
from core.document import DocumentManager
from core.formatting import FormattingManager

# Create document
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# Add paragraph
para = doc_manager.add_paragraph("This is a test paragraph")

# Set format (推荐使用字符单位)
formatting_manager = FormattingManager(doc)
formatting_manager.set_paragraph_format(
    para,
    alignment="justify",           # 两端对齐
    line_spacing=29,               # 行距29磅
    line_spacing_rule="exact",     # 固定值
    space_before=0,                # 段前0磅
    space_after=0,                 # 段后0磅
    first_line_indent_chars=2      # 首行缩进2字符
)

# Set font
for run in para.runs:
    formatting_manager.set_font(
        run,
        font_name="SimSun",
        font_size=12,
        bold=True,
        color="#FF0000"
    )
```

### 4. 🤖 Use AI Analysis

```python
from core.document import DocumentManager
from core.ai_integration import AIIntegration

# Open document
doc_manager = DocumentManager()
doc_manager.open_document("input.docx")

# Analyze document
analysis = doc_manager.analyze_document(use_ai=True)
print(analysis)
```

## 🧩 Core Modules

### 📄 DocumentManager
Document manager, provides core document operations:
- `create_document()`: Create new document
- `open_document()`: Open existing document
- `save_document()`: Save document
- `analyze_document()`: Analyze document structure
- `replace_text()`: Replace text
- `add_paragraph()`: Add paragraph
- `add_heading()`: Add heading
- `add_table()`: Add table

### 🎨 FormattingManager
Format manager, provides format control functions:
- `set_font()`: Set font format
- `set_paragraph_format()`: Set paragraph format
- `set_page_format()`: Set page format
- `set_table_format()`: Set table format
- `set_cell_format()`: Set cell format
- `create_custom_style()`: Create custom style

### 📐 StyleManager
Style manager, provides style management functions:
- `get_style()`: Get style
- `create_paragraph_style()`: Create paragraph style
- `create_character_style()`: Create character style
- `create_table_style()`: Create table style
- `apply_style()`: Apply style
- `modify_style()`: Modify style
- `import_styles()`: Import styles

### 🤖 AIIntegration
AI integration class, provides AI functions:
- `analyze_structure()`: Analyze document structure
- `correct_text()`: Text correction
- `optimize_formatting()`: Optimize formatting
- `generate_content()`: Generate content
- `translate_formatting()`: Convert format rules
- `apply_format_by_analysis()`: Apply format based on analysis
- `analyze_and_apply_format()`: Analyze and apply format automatically

## 📜 Official Document Format Example (公文格式)

```python
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from core.document import DocumentManager
from core.formatting import FormattingManager

# Create official document
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# Set page format (A4公文格式)
formatting_manager = FormattingManager(doc)
formatting_manager.set_page_format(
    page_width=21.0,  # A4 width
    page_height=29.7,  # A4 height
    left_margin=2.8,
    right_margin=2.6,
    top_margin=3.7,
    bottom_margin=3.5
)

# Add title (方正小标宋简体，二号，居中)
title = doc_manager.add_paragraph("关于XXX的通知")
formatting_manager.set_paragraph_format(title, alignment="center", 
                                       first_line_indent_chars=2,
                                       line_spacing=28, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in title.runs:
    formatting_manager.set_font(run, font_name="方正小标宋简体", font_size=22)

# Add first level heading (黑体，三号)
heading1 = doc_manager.add_paragraph("一、总体要求")
formatting_manager.set_paragraph_format(heading1, alignment="left",
                                       first_line_indent_chars=2,
                                       line_spacing=28, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in heading1.runs:
    formatting_manager.set_font(run, font_name="黑体", font_size=16)

# Add body text (仿宋，三号，首行缩进2字符，行距28磅)
body = doc_manager.add_paragraph("这是正文内容，需要首行缩进2字符。")
formatting_manager.set_paragraph_format(body, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=28, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in body.runs:
    formatting_manager.set_font(run, font_name="仿宋", font_size=16)

# Save document
doc_manager.save_document("official_document.docx")
```

## 📚 Academic Paper Example (学术论文格式)

```python
from core.document import DocumentManager
from core.formatting import FormattingManager

# Create academic paper
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# Set page format
formatting_manager = FormattingManager(doc)
formatting_manager.set_page_format(
    page_width=21.0,
    page_height=29.7,
    left_margin=2.5,
    right_margin=2.5,
    top_margin=2.5,
    bottom_margin=2.5
)

# Add title (宋体，加黑，小二号，居中，首行缩进2字符)
title = doc_manager.add_paragraph("论文标题")
formatting_manager.set_paragraph_format(title, alignment="center",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in title.runs:
    formatting_manager.set_font(run, font_name="SimSun", font_size=18, bold=True)

# Add abstract (楷体，小五号，首行缩进2字符，行距22磅)
abstract = doc_manager.add_paragraph("摘要：这是摘要内容。")
formatting_manager.set_paragraph_format(abstract, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in abstract.runs:
    formatting_manager.set_font(run, font_name="KaiTi", font_size=9)

# Add keywords (楷体，小五号，首行缩进2字符，行距22磅)
keywords = doc_manager.add_paragraph("关键词：关键词1；关键词2；关键词3")
formatting_manager.set_paragraph_format(keywords, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in keywords.runs:
    formatting_manager.set_font(run, font_name="KaiTi", font_size=9)

# Add body heading (黑体，小四号，首行不缩进，行距22磅)
heading1 = doc_manager.add_paragraph("一、引言")
formatting_manager.set_paragraph_format(heading1, alignment="left",
                                       first_line_indent_chars=0,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in heading1.runs:
    formatting_manager.set_font(run, font_name="SimHei", font_size=12, bold=True)

# Add body text (宋体，五号，首行缩进2字符，行距22磅)
body = doc_manager.add_paragraph("这是正文内容。")
formatting_manager.set_paragraph_format(body, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in body.runs:
    formatting_manager.set_font(run, font_name="SimSun", font_size=10.5)

# Save document
doc_manager.save_document("academic_paper.docx")
```

## 📝 Notes

1. **🔤 Font Compatibility**: Ensure required fonts are installed on the system
2. **📄 Format Preservation**: Try to preserve original formatting when editing documents
3. **🤖 AI Functions**: Need to set DEEPSEEK_API_KEY environment variable
4. **💾 File Backup**: Recommend backing up important documents before editing
5. **⚡ Performance**: Large documents may take longer to process

## 🔗 Relationship with Original Skills

This skill combines the advantages of minimax-docx and docx-official:
- Preserves the powerful document processing capabilities of minimax-docx
- Preserves the official document format conversion function of docx-official
- Enhances font, format, paragraph typesetting control
- Deeply integrates DeepSeek API for intelligent analysis

The original two skills are still preserved and can continue to be used. This skill provides a more unified and powerful interface.

## 🆘 Technical Support

If you have questions or suggestions, please contact the development team.

---

**🎉 Enjoy using docx-master!**
