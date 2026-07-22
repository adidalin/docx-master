# 📝 docx-master

<div align="center">

**🎯 专业Word文档处理技能**

*合并minimax-docx和docx-official的优点，提供完整的文档创建、编辑、格式化和AI智能分析功能*

[![GitHub stars](https://img.shields.io/github/stars/adidalin/docx-master?style=social)](https://github.com/adidalin/docx-master/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/adidalin/docx-master?style=social)](https://github.com/adidalin/docx-master/network/members)
[![GitHub issues](https://img.shields.io/github/issues/adidalin/docx-master)](https://github.com/adidalin/docx-master/issues)
[![GitHub license](https://img.shields.io/github/license/adidalin/docx-master)](https://github.com/adidalin/docx-master/blob/master/LICENSE)

</div>

---

## 🌟 特性亮点

### 🚀 核心功能
- **📄 文档创建** - 从零创建专业Word文档，支持多种模板
- **✏️ 文档编辑** - 修改现有文档内容，保留格式
- **🎨 格式控制** - 精确控制字体、段落、页面格式
- **📐 样式管理** - 创建、修改、应用自定义样式
- **🤖 AI集成** - 集成DeepSeek API，提供智能分析和优化
- **✅ 文档验证** - 验证文档结构、格式，自动修复问题
- **📑 目录生成** - 自动生成和更新目录
- **📝 占位符填充** - 查找和填充文档中的占位符

### 🎨 格式控制
- **🔤 字体设置** - 中英文字体、字号、颜色、加粗、斜体、上标、下标等
- **📝 段落格式** - 对齐方式、行距、缩进、间距等
- **📐 页面设置** - 纸张大小、页边距、页眉页脚等
- **📊 表格格式** - 边框、对齐、单元格样式等
- **🔤 引号替换** - 自动替换英文引号为中文引号

### 🤖 AI功能
- **🔍 文档结构分析** - 自动识别标题、正文、落款等
- **💡 智能格式建议** - 根据文档类型推荐格式
- **✏️ 文本纠错** - 检查错别字、语法错误
- **📝 内容生成** - 根据主题生成文档内容

---

## 📋 格式规范

### 🎯 默认格式规则
| 项目 | 设置值 |
|------|--------|
| 段前间距 | 0行 |
| 段后间距 | 0行 |
| 首行缩进 | 2字符 |
| 行间距 | 22磅固定值 |
| 标题格式 | 居中，首行缩进2字符，行距22磅 |
| 公文行间距 | 28磅固定值 |

### 🔤 引号使用规则（重要）
**⚠️ 注意：引号必须使用中文板式！**

| 类型 | 正确（中文板式） | 错误（英文板式） |
|------|------------------|------------------|
| 双引号 | "" | "" |
| 单引号 | '' | '' |
| 书名号 | 《》 | <> |
| 括号 | （） | () |
| 冒号 | ： | : |
| 分号 | ； | ; |
| 逗号 | ， | , |
| 句号 | 。 | . |
| 顿号 | 、 | , |

**示例：**
- ✅ 正确：《教育强国建设规划纲要（2024—2035年）》提出实施"国家教育数字化战略"
- ❌ 错误：《教育强国建设规划纲要(2024-2035年)》提出实施"国家教育数字化战略"

**在代码中处理：**
```python
# 替换英文引号为中文引号
text = text.replace('"', '\u201c').replace('"', '\u201d')
text = text.replace("'", '\u2018').replace("'", '\u2019')
text = text.replace('(', '（').replace(')', '）')
```

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

---

## 🚀 使用情境

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

---

## 📦 安装依赖

```bash
pip install python-docx requests
```

## 🔑 环境变量（可选）

设置DeepSeek API密钥可启用AI功能：

```bash
# Windows
set DEEPSEEK_API_KEY=your-api-key

# Linux/Mac
export DEEPSEEK_API_KEY=your-api-key
```

---

## 🚀 快速开始

### 1. 📄 创建新文档

```python
from core.document import DocumentManager

# 创建文档管理器
doc_manager = DocumentManager()

# 创建新文档
doc = doc_manager.create_document()

# 添加内容
doc_manager.add_heading("文档标题", level=0)
doc_manager.add_paragraph("这是正文内容。")

# 保存文档
doc_manager.save_document("output.docx")
```

### 2. ✏️ 打开并编辑现有文档

```python
from core.document import DocumentManager

# 打开文档
doc_manager = DocumentManager()
doc_manager.open_document("input.docx")

# 替换文本
doc_manager.replace_text("旧文本", "新文本")

# 保存文档
doc_manager.save_document("output.docx")
```

### 3. 🎨 设置格式

```python
from core.document import DocumentManager
from core.formatting import FormattingManager

# 创建文档
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# 添加段落
para = doc_manager.add_paragraph("这是测试段落")

# 设置格式
formatting_manager = FormattingManager(doc)
formatting_manager.set_paragraph_format(
    para,
    alignment="justify",           # 两端对齐
    line_spacing=29,               # 行距29磅
    line_spacing_rule="exact",     # 固定值
    space_before=0,                # 段前0行
    space_after=0,                 # 段后0行
    first_line_indent_chars=2      # 首行缩进2字符
)

# 设置字体
for run in para.runs:
    formatting_manager.set_font(
        run,
        font_name="SimSun",
        font_size=12,
        bold=True,
        color="#FF0000"
    )
```

### 4. 🤖 使用AI分析

```python
from core.document import DocumentManager
from core.ai_integration import AIIntegration

# 打开文档
doc_manager = DocumentManager()
doc_manager.open_document("input.docx")

# 分析文档
analysis = doc_manager.analyze_document(use_ai=True)
print(analysis)
```

### 5. ✅ 验证文档

```python
from core.document import DocumentManager
from core.validation import DocumentValidator

# 打开文档
doc_manager = DocumentManager()
doc_manager.open_document("input.docx")

# 验证文档
validator = DocumentValidator(doc_manager.document)
structure_result = validator.validate_structure()
formatting_result = validator.validate_formatting()

print(f"结构验证: {structure_result['valid']}")
print(f"格式验证: {formatting_result['valid']}")
```

### 6. 📑 生成目录

```python
from core.document import DocumentManager
from core.toc import TableOfContents

# 打开文档
doc_manager = DocumentManager()
doc_manager.open_document("input.docx")

# 生成目录
toc = TableOfContents(doc_manager.document)
toc.generate(title="目录", max_level=3)

# 保存文档
doc_manager.save_document("output_with_toc.docx")
```

### 7. 📝 填充占位符

```python
from core.document import DocumentManager
from core.placeholder import PlaceholderFiller

# 打开文档
doc_manager = DocumentManager()
doc_manager.open_document("template.docx")

# 填充占位符
filler = PlaceholderFiller(doc_manager.document)
data = {
    "name": "张三",
    "date": "2026年7月21日",
    "company": "XXX公司"
}
result = filler.fill(data)

print(f"已填充: {len(result['filled'])} 个占位符")

# 保存文档
doc_manager.save_document("output.docx")
```

---

## 🧩 核心模块

### 📄 DocumentManager
文档管理器，提供文档的核心操作功能：
- `create_document()` - 创建新文档
- `open_document()` - 打开现有文档
- `save_document()` - 保存文档
- `analyze_document()` - 分析文档结构
- `replace_text()` - 替换文本
- `add_paragraph()` - 添加段落
- `add_heading()` - 添加标题
- `add_table()` - 添加表格

### 🎨 FormattingManager
格式管理器，提供格式控制功能：
- `set_font()` - 设置字体格式
- `set_paragraph_format()` - 设置段落格式
- `set_page_format()` - 设置页面格式
- `set_table_format()` - 设置表格格式
- `set_cell_format()` - 设置单元格格式
- `create_custom_style()` - 创建自定义样式

### 📐 StyleManager
样式管理器，提供样式管理功能：
- `get_style()` - 获取样式
- `create_paragraph_style()` - 创建段落样式
- `create_character_style()` - 创建字符样式
- `create_table_style()` - 创建表格样式
- `apply_style()` - 应用样式
- `modify_style()` - 修改样式
- `import_styles()` - 导入样式

### 🤖 AIIntegration
AI集成类，提供AI功能：
- `analyze_structure()` - 分析文档结构
- `correct_text()` - 文本纠错
- `optimize_formatting()` - 优化格式
- `generate_content()` - 生成内容
- `translate_formatting()` - 转换格式规则
- `apply_format_by_analysis()` - 根据分析结果应用格式
- `analyze_and_apply_format()` - 分析并自动应用格式

### ✅ DocumentValidator
文档验证器，提供验证功能：
- `validate_structure()` - 验证文档结构
- `validate_formatting()` - 验证文档格式
- `validate_for_official_document()` - 验证公文格式
- `auto_fix()` - 自动修复问题

### 📑 TableOfContents
目录生成器：
- `generate()` - 生成目录
- `update()` - 更新目录
- `add_toc_entry()` - 添加目录条目
- `extract_headings()` - 提取文档标题
- `generate_simple_toc()` - 生成简单目录文本

### 📝 PlaceholderFiller
占位符填充器：
- `find_placeholders()` - 查找占位符
- `fill()` - 填充占位符
- `fill_from_json()` - 从JSON文件填充
- `replace_text()` - 替换文本

---

## 📜 公文格式示例

```python
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from core.document import DocumentManager
from core.formatting import FormattingManager

# 创建公文
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# 设置页面格式（A4公文格式）
formatting_manager = FormattingManager(doc)
formatting_manager.set_page_format(
    page_width=21.0,  # A4宽度
    page_height=29.7,  # A4高度
    left_margin=2.8,
    right_margin=2.6,
    top_margin=3.7,
    bottom_margin=3.5
)

# 添加标题（方正小标宋简体，二号，居中）
title = doc_manager.add_paragraph("关于XXX的通知")
formatting_manager.set_paragraph_format(title, alignment="center", 
                                       first_line_indent_chars=2,
                                       line_spacing=28, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in title.runs:
    formatting_manager.set_font(run, font_name="方正小标宋简体", font_size=22)

# 添加一级标题（黑体，三号）
heading1 = doc_manager.add_paragraph("一、总体要求")
formatting_manager.set_paragraph_format(heading1, alignment="left",
                                       first_line_indent_chars=2,
                                       line_spacing=28, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in heading1.runs:
    formatting_manager.set_font(run, font_name="黑体", font_size=16)

# 添加正文（仿宋，三号，首行缩进2字符，行距28磅）
body = doc_manager.add_paragraph("这是正文内容，需要首行缩进2字符。")
formatting_manager.set_paragraph_format(body, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=28, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in body.runs:
    formatting_manager.set_font(run, font_name="仿宋", font_size=16)

# 保存文档
doc_manager.save_document("official_document.docx")
```

---

## 📚 学术论文示例

```python
from core.document import DocumentManager
from core.formatting import FormattingManager

# 创建学术论文
doc_manager = DocumentManager()
doc = doc_manager.create_document()

# 设置页面格式
formatting_manager = FormattingManager(doc)
formatting_manager.set_page_format(
    page_width=21.0,
    page_height=29.7,
    left_margin=2.5,
    right_margin=2.5,
    top_margin=2.5,
    bottom_margin=2.5
)

# 添加标题（宋体，加黑，小二号，居中，首行缩进2字符）
title = doc_manager.add_paragraph("论文标题")
formatting_manager.set_paragraph_format(title, alignment="center",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in title.runs:
    formatting_manager.set_font(run, font_name="SimSun", font_size=18, bold=True)

# 添加摘要（楷体，小五号，首行缩进2字符，行距22磅）
abstract = doc_manager.add_paragraph("摘要：这是摘要内容。")
formatting_manager.set_paragraph_format(abstract, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in abstract.runs:
    formatting_manager.set_font(run, font_name="KaiTi", font_size=9)

# 添加关键词（楷体，小五号，首行缩进2字符，行距22磅）
keywords = doc_manager.add_paragraph("关键词：关键词1；关键词2；关键词3")
formatting_manager.set_paragraph_format(keywords, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in keywords.runs:
    formatting_manager.set_font(run, font_name="KaiTi", font_size=9)

# 添加正文标题（黑体，小四号，首行不缩进，行距22磅）
heading1 = doc_manager.add_paragraph("一、引言")
formatting_manager.set_paragraph_format(heading1, alignment="left",
                                       first_line_indent_chars=0,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in heading1.runs:
    formatting_manager.set_font(run, font_name="SimHei", font_size=12, bold=True)

# 添加正文（宋体，五号，首行缩进2字符，行距22磅）
body = doc_manager.add_paragraph("这是正文内容。")
formatting_manager.set_paragraph_format(body, alignment="justify",
                                       first_line_indent_chars=2,
                                       line_spacing=22, 
                                       line_spacing_rule="exact",
                                       space_before=0, space_after=0)
for run in body.runs:
    formatting_manager.set_font(run, font_name="SimSun", font_size=10.5)

# 保存文档
doc_manager.save_document("academic_paper.docx")
```

---

## 📝 注意事项

1. **🔤 字体兼容性** - 确保系统中安装了所需的字体
2. **📄 格式保留** - 编辑文档时，尽量保留原有格式
3. **🤖 AI功能** - 需要设置DEEPSEEK_API_KEY环境变量
4. **💾 文件备份** - 编辑重要文档前建议备份
5. **⚡ 性能考虑** - 大文档处理可能需要较长时间

---

## 🔗 与其他技能的关系

本技能合并了minimax-docx和docx-official的优点：
- 保留了minimax-docx的强大文档处理能力
- 保留了docx-official的公文格式转换功能
- 增强了字体、格式、段落排版控制
- 深度集成了DeepSeek API进行智能分析

原有的两个技能仍然保留，可以继续使用。本技能提供了更统一、更强大的接口。

---

## 📁 目录结构

```
docx-master/
├── 📄 SKILL.md                    # 技能说明文档
├── 📄 README.md                   # 项目说明文档
├── 📄 requirements.txt            # Python依赖
├── 📁 core/                       # 核心模块
│   ├── 📄 __init__.py             # 模块初始化
│   ├── 📄 document.py             # 文档管理器
│   ├── 📄 formatting.py           # 格式管理器
│   ├── 📄 styles.py               # 样式管理器
│   ├── 📄 ai_integration.py       # AI集成
│   ├── 📄 validation.py           # 文档验证
│   ├── 📄 toc.py                  # 目录生成
│   ├── 📄 placeholder.py          # 占位符填充
│   └── 📄 utils.py                # 工具函数
├── 📁 examples/                   # 示例文件
│   ├── 📄 __init__.py
│   └── 📄 examples.py             # 使用示例
├── 📁 scripts/                    # 脚本文件
│   └── 📁 python/
│       └── 📄 convert_official.py # 公文格式转换
└── 📁 tests/                      # 测试文件
    └── 📄 __init__.py
```

---

## 🆘 技术支持

如有问题或建议，请联系开发团队。

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

<div align="center">

**🎉 感谢使用 docx-master！**

**如果觉得有用，请给个 ⭐ Star 支持一下！**

</div>
