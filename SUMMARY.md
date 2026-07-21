# docx-master 技能总结

## 概述

docx-master是一个专业Word文档处理技能，合并了minimax-docx和docx-official的优点，提供完整的文档创建、编辑、格式化和AI智能分析功能。

## 功能特点

### 核心功能
- **文档创建**：从零创建专业Word文档，支持多种模板
- **文档编辑**：修改现有文档内容，保留格式
- **格式控制**：精确控制字体、段落、页面格式
- **样式管理**：创建、修改、应用自定义样式
- **AI集成**：集成DeepSeek API，提供智能分析和优化

### 格式控制
- 字体设置：中英文字体、字号、颜色、加粗、斜体等
- 段落格式：对齐方式、行距、缩进、间距等
- 页面设置：纸张大小、页边距、页眉页脚等
- 表格格式：边框、对齐、单元格样式等

### AI功能
- 文档结构分析：自动识别标题、正文、落款等
- 智能格式建议：根据文档类型推荐格式
- 文本纠错：检查错别字、语法错误
- 内容生成：根据主题生成文档内容

## 技术架构

### 技术栈
- **核心语言**：Python
- **文档处理**：python-docx
- **AI集成**：DeepSeek API
- **测试框架**：pytest

### 目录结构
```
docx-master/
├── SKILL.md                    # 技能说明
├── requirements.txt            # 依赖文件
├── core/                       # 核心Python模块
│   ├── __init__.py
│   ├── document.py             # 文档操作核心
│   ├── formatting.py           # 格式控制
│   ├── styles.py               # 样式管理
│   ├── ai_integration.py       # AI集成
│   └── utils.py                # 工具函数
├── templates/                  # 模板文件
│   ├── official/               # 公文模板
│   ├── academic/               # 学术模板
│   └── business/               # 商务模板
├── scripts/                    # 脚本文件
│   ├── python/                 # Python脚本
│   │   └── convert_official.py # 公文格式转换
│   └── dotnet/                 # .NET脚本（保留原有）
├── examples/                   # 示例文件
│   └── examples.py             # 使用示例
└── tests/                      # 测试用例
    └── test_core.py            # 核心测试
```

## 核心模块

### DocumentManager
文档管理器，提供文档的核心操作功能：
- `create_document()`: 创建新文档
- `open_document()`: 打开现有文档
- `save_document()`: 保存文档
- `analyze_document()`: 分析文档结构
- `replace_text()`: 替换文本
- `add_paragraph()`: 添加段落
- `add_heading()`: 添加标题
- `add_table()`: 添加表格

### FormattingManager
格式管理器，提供格式控制功能：
- `set_font()`: 设置字体格式
- `set_paragraph_format()`: 设置段落格式
- `set_page_format()`: 设置页面格式
- `set_table_format()`: 设置表格格式
- `set_cell_format()`: 设置单元格格式
- `create_custom_style()`: 创建自定义样式

### StyleManager
样式管理器，提供样式管理功能：
- `get_style()`: 获取样式
- `create_paragraph_style()`: 创建段落样式
- `create_character_style()`: 创建字符样式
- `create_table_style()`: 创建表格样式
- `apply_style()`: 应用样式
- `modify_style()`: 修改样式
- `import_styles()`: 导入样式

### AIIntegration
AI集成类，提供AI功能：
- `analyze_structure()`: 分析文档结构
- `correct_text()`: 文本纠错
- `optimize_formatting()`: 优化格式
- `generate_content()`: 生成内容
- `translate_formatting()`: 转换格式规则

## 使用示例

### 创建公文
```python
from core.document import DocumentManager
from core.formatting import FormattingManager

# 创建文档管理器
doc_manager = DocumentManager()
doc = doc_manager.create_document()
formatting_manager = doc_manager.formatting_manager

# 设置页面格式
formatting_manager.set_page_format(
    page_width=21.0,  # A4宽度
    page_height=29.7,  # A4高度
    left_margin=2.8,
    right_margin=2.6,
    top_margin=3.7,
    bottom_margin=3.5
)

# 添加标题
title = doc_manager.add_heading("关于XXX的通知", level=0)
formatting_manager.set_paragraph_format(title, alignment="center")
for run in title.runs:
    formatting_manager.set_font(run, font_name="方正小标宋简体", font_size=22)

# 添加正文
body = doc_manager.add_paragraph("这是正文内容。")
formatting_manager.set_paragraph_format(body, first_line_indent=32, line_spacing=28)
for run in body.runs:
    formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=16)

# 保存文档
doc_manager.save_document("official_document.docx")
```

### 使用AI分析
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

## 测试

运行测试用例：
```bash
cd docx-master
python -m pytest tests/test_core.py -v
```

## 依赖安装

```bash
pip install -r requirements.txt
```

## 环境变量

设置DeepSeek API密钥可启用AI功能：
```bash
# Windows
set DEEPSEEK_API_KEY=your-api-key

# Linux/Mac
export DEEPSEEK_API_KEY=your-api-key
```

## 与原有技能的关系

本技能合并了minimax-docx和docx-official的优点：
- 保留了minimax-docx的强大文档处理能力
- 保留了docx-official的公文格式转换功能
- 增强了字体、格式、段落排版控制
- 深度集成了DeepSeek API进行智能分析

原有的两个技能仍然保留，可以继续使用。本技能提供了更统一、更强大的接口。

## 未来扩展

1. **模板系统**：添加更多文档模板
2. **批量处理**：支持批量文档处理
3. **格式转换**：支持更多格式之间的转换
4. **协作功能**：支持多人协作编辑
5. **版本控制**：支持文档版本管理

## 总结

docx-master技能成功合并了两个原有技能的优点，提供了更强大、更易用的Word文档处理功能。通过Python实现，具有良好的跨平台兼容性和扩展性。集成了DeepSeek API，提供了智能分析能力，可以大大提高文档处理效率。