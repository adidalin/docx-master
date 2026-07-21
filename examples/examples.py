"""
docx-master 使用示例
展示如何使用docx-master技能创建和编辑Word文档
"""

import os
import sys
from pathlib import Path

# 添加core目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.document import DocumentManager
from core.formatting import FormattingManager
from core.styles import StyleManager
from core.ai_integration import AIIntegration


def example_create_official_document():
    """示例：创建公文"""
    print("示例：创建公文")
    
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
    title = doc_manager.add_heading("关于加强安全管理的通知", level=0)
    formatting_manager.set_paragraph_format(title, alignment="center")
    for run in title.runs:
        formatting_manager.set_font(run, font_name="方正小标宋简体", font_size=22)
    
    # 添加一级标题
    heading1 = doc_manager.add_heading("一、总体要求", level=1)
    for run in heading1.runs:
        formatting_manager.set_font(run, font_name="黑体", font_size=16)
    
    # 添加正文
    body1 = doc_manager.add_paragraph(
        "为加强安全管理，保障人民群众生命财产安全，根据有关法律法规，现就有关事项通知如下："
    )
    formatting_manager.set_paragraph_format(body1, first_line_indent=32, line_spacing=28)
    for run in body1.runs:
        formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=16)
    
    # 添加二级标题
    heading2 = doc_manager.add_heading("（一）提高思想认识", level=2)
    for run in heading2.runs:
        formatting_manager.set_font(run, font_name="楷体_GB2312", font_size=16)
    
    # 添加正文
    body2 = doc_manager.add_paragraph(
        "各级各部门要充分认识安全管理工作的重要性，牢固树立安全发展理念，切实增强责任感和紧迫感。"
    )
    formatting_manager.set_paragraph_format(body2, first_line_indent=32, line_spacing=28)
    for run in body2.runs:
        formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=16)
    
    # 添加三级标题
    heading3 = doc_manager.add_heading("1. 加强组织领导", level=3)
    for run in heading3.runs:
        formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=16, bold=True)
    
    # 添加正文
    body3 = doc_manager.add_paragraph(
        "成立安全管理工作领导小组，明确职责分工，确保各项工作落到实处。"
    )
    formatting_manager.set_paragraph_format(body3, first_line_indent=32, line_spacing=28)
    for run in body3.runs:
        formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=16)
    
    # 添加表格
    table = doc_manager.add_table(4, 3, [
        ["序号", "工作内容", "责任单位"],
        ["1", "安全检查", "安全部"],
        ["2", "隐患排查", "生产部"],
        ["3", "应急演练", "办公室"]
    ])
    
    formatting_manager.set_table_format(table, alignment="center", borders=True)
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                formatting_manager.set_paragraph_format(para, alignment="center")
                for run in para.runs:
                    formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=12)
    
    # 添加落款
    signature = doc_manager.add_paragraph("XXX公司")
    formatting_manager.set_paragraph_format(signature, alignment="right", right_indent=96)
    for run in signature.runs:
        formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=16)
    
    date = doc_manager.add_paragraph("2026年7月21日")
    formatting_manager.set_paragraph_format(date, alignment="right", right_indent=96)
    for run in date.runs:
        formatting_manager.set_font(run, font_name="仿宋_GB2312", font_size=16)
    
    # 保存文档
    output_path = Path(__file__).parent / "example_official.docx"
    doc_manager.save_document(str(output_path))
    print(f"公文已保存: {output_path}")


def example_create_academic_paper():
    """示例：创建学术论文"""
    print("\n示例：创建学术论文")
    
    # 创建文档管理器
    doc_manager = DocumentManager()
    doc = doc_manager.create_document()
    formatting_manager = doc_manager.formatting_manager
    
    # 设置页面格式
    formatting_manager.set_page_format(
        page_width=21.0,
        page_height=29.7,
        left_margin=2.5,
        right_margin=2.5,
        top_margin=2.5,
        bottom_margin=2.5
    )
    
    # 添加标题
    title = doc_manager.add_heading("基于深度学习的图像识别研究", level=0)
    formatting_manager.set_paragraph_format(title, alignment="center")
    for run in title.runs:
        formatting_manager.set_font(run, font_name="黑体", font_size=18, bold=True)
    
    # 添加作者
    author = doc_manager.add_paragraph("张三  李四  王五")
    formatting_manager.set_paragraph_format(author, alignment="center")
    for run in author.runs:
        formatting_manager.set_font(run, font_name="宋体", font_size=12)
    
    # 添加单位
    affiliation = doc_manager.add_paragraph("（某某大学 计算机学院，北京 100000）")
    formatting_manager.set_paragraph_format(affiliation, alignment="center")
    for run in affiliation.runs:
        formatting_manager.set_font(run, font_name="宋体", font_size=10)
    
    # 添加摘要标题
    abstract_title = doc_manager.add_heading("摘  要", level=1)
    formatting_manager.set_paragraph_format(abstract_title, alignment="center")
    for run in abstract_title.runs:
        formatting_manager.set_font(run, font_name="黑体", font_size=12, bold=True)
    
    # 添加摘要内容
    abstract = doc_manager.add_paragraph(
        "本文提出了一种基于深度学习的图像识别方法。该方法利用卷积神经网络提取图像特征，"
        "并通过改进的损失函数提高分类准确率。实验结果表明，该方法在多个数据集上取得了优异的性能。"
    )
    formatting_manager.set_paragraph_format(abstract, first_line_indent=24, line_spacing=1.5)
    for run in abstract.runs:
        formatting_manager.set_font(run, font_name="宋体", font_size=10)
    
    # 添加关键词
    keywords = doc_manager.add_paragraph("关键词：深度学习；图像识别；卷积神经网络；特征提取")
    formatting_manager.set_paragraph_format(keywords, first_line_indent=24)
    for run in keywords.runs:
        formatting_manager.set_font(run, font_name="宋体", font_size=10)
    
    # 添加英文标题
    en_title = doc_manager.add_heading("Research on Image Recognition Based on Deep Learning", level=1)
    formatting_manager.set_paragraph_format(en_title, alignment="center")
    for run in en_title.runs:
        formatting_manager.set_font(run, font_name="Times New Roman", font_size=14, bold=True)
    
    # 添加英文作者
    en_author = doc_manager.add_paragraph("ZHANG San  LI Si  WANG Wu")
    formatting_manager.set_paragraph_format(en_author, alignment="center")
    for run in en_author.runs:
        formatting_manager.set_font(run, font_name="Times New Roman", font_size=12)
    
    # 添加英文摘要
    en_abstract_title = doc_manager.add_heading("Abstract", level=1)
    formatting_manager.set_paragraph_format(en_abstract_title, alignment="center")
    for run in en_abstract_title.runs:
        formatting_manager.set_font(run, font_name="Times New Roman", font_size=12, bold=True)
    
    en_abstract = doc_manager.add_paragraph(
        "This paper proposes an image recognition method based on deep learning. "
        "The method uses convolutional neural networks to extract image features "
        "and improves classification accuracy through an improved loss function. "
        "Experimental results show that the method achieves excellent performance on multiple datasets."
    )
    formatting_manager.set_paragraph_format(en_abstract, first_line_indent=24, line_spacing=1.5)
    for run in en_abstract.runs:
        formatting_manager.set_font(run, font_name="Times New Roman", font_size=10)
    
    # 添加英文关键词
    en_keywords = doc_manager.add_paragraph(
        "Key words: deep learning; image recognition; convolutional neural network; feature extraction"
    )
    formatting_manager.set_paragraph_format(en_keywords, first_line_indent=24)
    for run in en_keywords.runs:
        formatting_manager.set_font(run, font_name="Times New Roman", font_size=10)
    
    # 添加正文标题
    heading1 = doc_manager.add_heading("1 引言", level=1)
    for run in heading1.runs:
        formatting_manager.set_font(run, font_name="黑体", font_size=14, bold=True)
    
    # 添加正文
    body1 = doc_manager.add_paragraph(
        "图像识别是计算机视觉领域的核心问题之一，广泛应用于人脸识别、自动驾驶、医疗诊断等领域。"
        "近年来，随着深度学习技术的快速发展，基于深度学习的图像识别方法取得了显著进展[1]。"
    )
    formatting_manager.set_paragraph_format(body1, first_line_indent=24, line_spacing=1.5)
    for run in body1.runs:
        formatting_manager.set_font(run, font_name="宋体", font_size=10)
    
    body2 = doc_manager.add_paragraph(
        "传统的图像识别方法主要依赖手工特征，如SIFT、HOG等。这些方法在特定场景下表现良好，"
        "但在复杂场景下泛化能力有限。深度学习方法能够自动学习图像特征，具有更强的表达能力[2]。"
    )
    formatting_manager.set_paragraph_format(body2, first_line_indent=24, line_spacing=1.5)
    for run in body2.runs:
        formatting_manager.set_font(run, font_name="宋体", font_size=10)
    
    # 添加二级标题
    heading2 = doc_manager.add_heading("1.1 研究背景", level=2)
    for run in heading2.runs:
        formatting_manager.set_font(run, font_name="黑体", font_size=12, bold=True)
    
    body3 = doc_manager.add_paragraph(
        "卷积神经网络（CNN）是深度学习中最重要的模型之一。自AlexNet在ImageNet竞赛中取得突破性成绩以来，"
        "CNN已经成为图像识别的主流方法。典型的CNN架构包括VGG、ResNet、Inception等。"
    )
    formatting_manager.set_paragraph_format(body3, first_line_indent=24, line_spacing=1.5)
    for run in body3.runs:
        formatting_manager.set_font(run, font_name="宋体", font_size=10)
    
    # 添加参考文献
    heading_ref = doc_manager.add_heading("参考文献", level=1)
    for run in heading_ref.runs:
        formatting_manager.set_font(run, font_name="黑体", font_size=14, bold=True)
    
    ref1 = doc_manager.add_paragraph("[1] Krizhevsky A, Sutskever I, Hinton G E. ImageNet classification with deep convolutional neural networks[J]. Communications of the ACM, 2017, 60(6): 84-90.")
    formatting_manager.set_paragraph_format(ref1, line_spacing=1.5)
    for run in ref1.runs:
        formatting_manager.set_font(run, font_name="Times New Roman", font_size=10)
    
    ref2 = doc_manager.add_paragraph("[2] LeCun Y, Bengio Y, Hinton G. Deep learning[J]. Nature, 2015, 521(7553): 436-444.")
    formatting_manager.set_paragraph_format(ref2, line_spacing=1.5)
    for run in ref2.runs:
        formatting_manager.set_font(run, font_name="Times New Roman", font_size=10)
    
    # 保存文档
    output_path = Path(__file__).parent / "example_academic.docx"
    doc_manager.save_document(str(output_path))
    print(f"学术论文已保存: {output_path}")


def example_edit_existing_document():
    """示例：编辑现有文档"""
    print("\n示例：编辑现有文档")
    
    # 创建示例文档
    doc_manager = DocumentManager()
    doc = doc_manager.create_document()
    
    # 添加内容
    doc_manager.add_paragraph("这是原始文档内容。")
    doc_manager.add_paragraph("包含一些需要修改的文本。")
    doc_manager.add_paragraph("比如这个错别字：己经。")
    
    # 保存原始文档
    original_path = Path(__file__).parent / "example_original.docx"
    doc_manager.save_document(str(original_path))
    
    # 打开并编辑文档
    edit_manager = DocumentManager()
    edit_manager.open_document(str(original_path))
    
    # 替换文本
    count = edit_manager.replace_text("己经", "已经")
    print(f"替换了 {count} 处文本")
    
    # 添加新内容
    edit_manager.add_paragraph("这是新添加的内容。")
    
    # 保存编辑后的文档
    edited_path = Path(__file__).parent / "example_edited.docx"
    edit_manager.save_document(str(edited_path))
    print(f"编辑后的文档已保存: {edited_path}")


def example_analyze_document():
    """示例：分析文档"""
    print("\n示例：分析文档")
    
    # 创建示例文档
    doc_manager = DocumentManager()
    doc = doc_manager.create_document()
    
    # 添加内容
    doc_manager.add_heading("文档标题", level=0)
    doc_manager.add_heading("一、一级标题", level=1)
    doc_manager.add_paragraph("这是正文内容。")
    doc_manager.add_heading("（一）二级标题", level=2)
    doc_manager.add_paragraph("这是更多正文内容。")
    
    # 分析文档
    analysis = doc_manager.analyze_document(use_ai=False)
    
    print(f"段落数量: {analysis['statistics']['paragraph_count']}")
    print(f"字符数量: {analysis['statistics']['character_count']}")
    
    # 显示段落信息
    for para in analysis['paragraphs']:
        print(f"段落 {para['index']}: {para['text'][:20]}... (样式: {para['style']})")


def example_use_styles():
    """示例：使用样式"""
    print("\n示例：使用样式")
    
    # 创建文档管理器
    doc_manager = DocumentManager()
    doc = doc_manager.create_document()
    style_manager = doc_manager.style_manager
    
    # 创建自定义样式
    title_style = style_manager.create_paragraph_style(
        "自定义标题",
        font_name="黑体",
        font_size=22,
        bold=True,
        alignment="center",
        space_before=24,
        space_after=12
    )
    
    body_style = style_manager.create_paragraph_style(
        "自定义正文",
        font_name="宋体",
        font_size=12,
        alignment="justify",
        first_line_indent=24,
        line_spacing=1.5
    )
    
    # 应用样式
    title = doc_manager.add_heading("使用自定义样式的文档", level=0)
    style_manager.apply_style(title, "自定义标题")
    
    body = doc_manager.add_paragraph("这是使用自定义样式的正文内容。")
    style_manager.apply_style(body, "自定义正文")
    
    # 保存文档
    output_path = Path(__file__).parent / "example_styles.docx"
    doc_manager.save_document(str(output_path))
    print(f"样式示例文档已保存: {output_path}")


def main():
    """主函数"""
    print("docx-master 使用示例")
    print("=" * 50)
    
    # 运行示例
    example_create_official_document()
    example_create_academic_paper()
    example_edit_existing_document()
    example_analyze_document()
    example_use_styles()
    
    print("\n" + "=" * 50)
    print("所有示例已完成！")


if __name__ == "__main__":
    main()