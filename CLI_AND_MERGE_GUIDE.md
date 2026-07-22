# 🔧 CLI工具和多模板合并详解

## 📋 目录

1. [什么是CLI工具](#什么是cli工具)
2. [CLI工具的优势](#cli工具的优势)
3. [CLI工具的使用场景](#cli工具的使用场景)
4. [什么是多模板合并](#什么是多模板合并)
5. [多模板合并的应用场景](#多模板合并的应用场景)
6. [docx-master的替代方案](#docx-master的替代方案)

---

## 什么是CLI工具

### 📖 定义

**CLI（Command Line Interface）工具**是通过命令行界面操作的程序，用户可以在终端（Terminal）中输入命令来执行特定任务。

### 🔍 示例

#### minimax-docx的CLI工具
```bash
# 创建文档
dotnet run --project scripts/dotnet/MiniMaxAIDocx.Cli -- create --type report --output out.docx

# 编辑文档
dotnet run --project scripts/dotnet/MiniMaxAIDocx.Cli -- edit replace-text --input in.docx --output out.docx --find "OLD" --replace "NEW"

# 验证文档
dotnet run --project scripts/dotnet/MiniMaxAIDocx.Cli -- validate --input doc.docx

# 应用模板
dotnet run --project scripts/dotnet/MiniMaxAIDocx.Cli -- apply-template --input source.docx --template template.docx --output out.docx
```

#### 简化命令
```bash
# 使用别名
$CLI create --type report --output out.docx
$CLI edit replace-text --input in.docx --output out.docx --find "OLD" --replace "NEW"
```

---

## CLI工具的优势

### 1. 🚀 自动化

#### 批量处理
```bash
# 批量处理多个文件
for file in *.docx; do
    $CLI edit replace-text --input "$file" --output "processed_$file" --find "旧文本" --replace "新文本"
done
```

#### 脚本集成
```bash
#!/bin/bash
# 自动化脚本

# 1. 创建文档
$CLI create --type report --output report.docx

# 2. 填充内容
$CLI edit fill-placeholders --input report.docx --output report_filled.docx --data '{"name":"张三","date":"2026-07-21"}'

# 3. 验证文档
$CLI validate --input report_filled.docx

# 4. 发送邮件
send_email report_filled.docx
```

### 2. 🔄 可重复性

#### 一致的结果
```bash
# 每次执行都产生相同的结果
$CLI create --type memo --output memo.docx --config memo_config.json
```

#### 版本控制
```bash
# 命令可以保存在脚本中，便于版本控制
git add create_report.sh
git commit -m "添加报告生成脚本"
```

### 3. 🛠️ 集成性

#### CI/CD集成
```yaml
# GitHub Actions示例
name: Generate Report
on:
  schedule:
    - cron: '0 0 * * *'  # 每天执行

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate Report
        run: |
          $CLI create --type report --output daily_report.docx
          $CLI validate --input daily_report.docx
```

#### 其他工具集成
```bash
# 与Git集成
$CLI create --type changelog --output CHANGELOG.docx
git add CHANGELOG.docx
git commit -m "更新变更日志"
```

### 4. 📊 效率

#### 快速执行
```bash
# 一行命令完成复杂任务
$CLI create --type report --output report.docx --config config.json --validate
```

#### 并行处理
```bash
# 并行处理多个文件
$CLI batch-process --input-dir ./input --output-dir ./output --parallel 4
```

---

## CLI工具的使用场景

### 1. 📄 文档生成

#### 报告生成
```bash
# 生成日报
$CLI create --type daily_report --output daily_$(date +%Y%m%d).docx

# 生成周报
$CLI create --type weekly_report --output weekly_$(date +%Y%m%d).docx

# 生成月报
$CLI create --type monthly_report --output monthly_$(date +%Y%m).docx
```

#### 合同生成
```bash
# 生成合同
$CLI create --type contract --output contract.docx --data '{
    "party_a": "甲方公司",
    "party_b": "乙方公司",
    "amount": "100000",
    "date": "2026-07-21"
}'
```

### 2. ✏️ 文档编辑

#### 批量替换
```bash
# 批量替换文本
$CLI batch-replace --input-dir ./docs --output-dir ./output --replacements '{
    "旧公司名": "新公司名",
    "旧地址": "新地址",
    "旧电话": "新电话"
}'
```

#### 格式调整
```bash
# 调整格式
$CLI reformat --input doc.docx --output doc_formatted.docx --style official
```

### 3. ✅ 文档验证

#### 格式验证
```bash
# 验证公文格式
$CLI validate --input official.docx --type official

# 验证学术论文格式
$CLI validate --input paper.docx --type academic
```

#### 内容验证
```bash
# 验证内容完整性
$CLI validate --input doc.docx --check-content

# 验证格式一致性
$CLI validate --input doc.docx --check-formatting
```

### 4. 📑 模板操作

#### 应用模板
```bash
# 应用公文模板
$CLI apply-template --input draft.docx --template official.docx --output official.docx

# 应用学术论文模板
$CLI apply-template --input draft.docx --template academic.docx --output paper.docx
```

#### 模板合并
```bash
# 合并多个模板
$CLI merge-templates --templates template1.docx,template2.docx --output merged.docx
```

---

## 什么是多模板合并

### 📖 定义

**多模板合并**是将多个模板文件的不同部分组合成一个完整文档的技术。

### 🔍 示例

#### 场景：创建学术论文

需要合并的模板：
1. **封面模板** - 包含封面格式
2. **目录模板** - 包含目录格式
3. **正文模板** - 包含正文格式
4. **参考文献模板** - 包含参考文献格式

#### 合并过程
```bash
# 合并多个模板
$CLI merge-templates \
    --templates cover.docx,toc.docx,body.docx,references.docx \
    --output complete_paper.docx
```

---

## 多模板合并的应用场景

### 1. 📚 学术论文

#### 模板结构
```
论文模板/
├── 封面.docx          # 封面格式
├── 摘要.docx          # 摘要格式
├── 目录.docx          # 目录格式
├── 正文.docx          # 正文格式
├── 参考文献.docx      # 参考文献格式
└── 附录.docx          # 附录格式
```

#### 合并命令
```bash
$CLI merge-templates \
    --templates 封面.docx,摘要.docx,目录.docx,正文.docx,参考文献.docx,附录.docx \
    --output 论文.docx
```

### 2. 📜 公文

#### 模板结构
```
公文模板/
├── 红头.docx          # 红头格式
├── 正文.docx          # 正文格式
├── 附件.docx          # 附件格式
└── 落款.docx          # 落款格式
```

#### 合并命令
```bash
$CLI merge-templates \
    --templates 红头.docx,正文.docx,附件.docx,落款.docx \
    --output 公文.docx
```

### 3. 📊 商务报告

#### 模板结构
```
商务报告模板/
├── 封面.docx          # 封面格式
├── 目录.docx          # 目录格式
├── 执行摘要.docx      # 执行摘要格式
├── 正文.docx          # 正文格式
├── 图表.docx          # 图表格式
└── 结论.docx          # 结论格式
```

#### 合并命令
```bash
$CLI merge-templates \
    --templates 封面.docx,目录.docx,执行摘要.docx,正文.docx,图表.docx,结论.docx \
    --output 商务报告.docx
```

### 4. 📝 合同

#### 模板结构
```
合同模板/
├── 封面.docx          # 封面格式
├── 条款.docx          # 条款格式
├── 附件.docx          # 附件格式
└── 签署页.docx        # 签署页格式
```

#### 合并命令
```bash
$CLI merge-templates \
    --templates 封面.docx,条款.docx,附件.docx,签署页.docx \
    --output 合同.docx
```

---

## 多模板合并的技术细节

### 1. 📋 样式合并

#### 问题
不同模板可能有相同的样式名称，但格式不同。

#### 解决方案
```bash
# 样式合并策略
$CLI merge-templates \
    --templates template1.docx,template2.docx \
    --style-strategy merge  # merge, override, rename
```

#### 策略选项
- **merge** - 合并样式，保留所有样式
- **override** - 覆盖样式，后面的模板覆盖前面的
- **rename** - 重命名样式，避免冲突

### 2. 📄 内容合并

#### 问题
模板可能包含示例内容，需要替换为实际内容。

#### 解决方案
```bash
# 内容合并策略
$CLI merge-templates \
    --templates template1.docx,template2.docx \
    --content-strategy replace  # keep, replace, merge
```

#### 策略选项
- **keep** - 保留模板内容
- **replace** - 替换为实际内容
- **merge** - 合并内容

### 3. 📑 节合并

#### 问题
不同模板可能有不同的页面设置（页边距、纸张大小等）。

#### 解决方案
```bash
# 节合并策略
$CLI merge-templates \
    --templates template1.docx,template2.docx \
    --section-strategy preserve  # preserve,统一, custom
```

#### 策略选项
- **preserve** - 保留各模板的页面设置
- **统一** - 使用统一的页面设置
- **custom** - 自定义页面设置

---

## docx-master的替代方案

### 1. 🐍 Python脚本替代CLI

#### 创建CLI包装器
```python
# cli.py
import argparse
from core.document import DocumentManager
from core.formatting import FormattingManager

def main():
    parser = argparse.ArgumentParser(description='docx-master CLI')
    subparsers = parser.add_subparsers(dest='command')
    
    # 创建文档命令
    create_parser = subparsers.add_parser('create', help='创建文档')
    create_parser.add_argument('--type', required=True, help='文档类型')
    create_parser.add_argument('--output', required=True, help='输出文件')
    
    # 验证文档命令
    validate_parser = subparsers.add_parser('validate', help='验证文档')
    validate_parser.add_argument('--input', required=True, help='输入文件')
    
    args = parser.parse_args()
    
    if args.command == 'create':
        create_document(args.type, args.output)
    elif args.command == 'validate':
        validate_document(args.input)

def create_document(doc_type, output):
    doc_manager = DocumentManager()
    doc = doc_manager.create_document()
    # 根据类型添加内容
    doc_manager.save_document(output)

def validate_document(input_file):
    from core.validation import DocumentValidator
    doc_manager = DocumentManager()
    doc_manager.open_document(input_file)
    validator = DocumentValidator(doc_manager.document)
    result = validator.validate_structure()
    print(f"验证结果: {result['valid']}")

if __name__ == '__main__':
    main()
```

#### 使用方式
```bash
# 创建文档
python cli.py create --type report --output report.docx

# 验证文档
python cli.py validate --input report.docx
```

### 2. 📝 脚本替代多模板合并

#### 创建模板合并脚本
```python
# merge_templates.py
from core.document import DocumentManager
from core.toc import TableOfContents

def merge_templates(template_files, output_file):
    """合并多个模板"""
    doc_manager = DocumentManager()
    doc = doc_manager.create_document()
    
    for template_file in template_files:
        # 读取模板
        template_doc = DocumentManager()
        template_doc.open_document(template_file)
        
        # 复制内容
        for para in template_doc.document.paragraphs:
            doc_manager.add_paragraph(para.text)
    
    # 保存合并后的文档
    doc_manager.save_document(output_file)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("用法: python merge_templates.py template1.docx template2.docx ... output.docx")
        sys.exit(1)
    
    template_files = sys.argv[1:-1]
    output_file = sys.argv[-1]
    merge_templates(template_files, output_file)
```

#### 使用方式
```bash
# 合并模板
python merge_templates.py template1.docx template2.docx output.docx
```

### 3. 🔧 配置文件替代CLI参数

#### 创建配置文件
```json
{
    "create": {
        "type": "report",
        "output": "report.docx",
        "config": {
            "title": "报告标题",
            "author": "作者",
            "date": "2026-07-21"
        }
    },
    "validate": {
        "input": "report.docx",
        "type": "official"
    }
}
```

#### 使用方式
```bash
# 使用配置文件
python cli.py --config config.json
```

---

## 📊 功能对比

| 功能 | minimax-docx CLI | docx-master Python |
|------|------------------|-------------------|
| 命令行操作 | ✅ | ✅ (通过脚本) |
| 批量处理 | ✅ | ✅ (通过脚本) |
| 脚本集成 | ✅ | ✅ |
| 配置文件 | ✅ | ✅ |
| 自动化 | ✅ | ✅ |
| 跨平台 | ⚠️ (需要.NET) | ✅ (Python) |
| 学习曲线 | 中等 | 低 |
| 灵活性 | 高 | 高 |

---

## 🎯 总结

### CLI工具
- **定义**：通过命令行界面操作的程序
- **优势**：自动化、可重复性、集成性、效率
- **使用场景**：文档生成、编辑、验证、模板操作

### 多模板合并
- **定义**：将多个模板的不同部分组合成一个完整文档
- **应用场景**：学术论文、公文、商务报告、合同
- **技术细节**：样式合并、内容合并、节合并

### docx-master的替代方案
1. **Python脚本替代CLI** - 创建CLI包装器
2. **脚本替代多模板合并** - 创建模板合并脚本
3. **配置文件替代CLI参数** - 使用JSON配置文件

**结论**：虽然docx-master没有原生的CLI工具和多模板合并功能，但可以通过Python脚本实现相同的功能，而且更加灵活和跨平台。
