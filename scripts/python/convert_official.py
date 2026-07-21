"""
公文格式转换脚本
基于docx-official的功能，使用新的docx-master技能实现
"""

import os
import sys
import argparse
from pathlib import Path

# 添加core目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.document import DocumentManager
from core.formatting import FormattingManager
from core.styles import StyleManager
from core.ai_integration import AIIntegration


def convert_to_official_format(input_path: str, output_path: str = None, 
                              use_ai: bool = True) -> bool:
    """
    将文档转换为公文格式
    
    Args:
        input_path: 输入文档路径
        output_path: 输出文档路径，如果不提供则自动生成
        use_ai: 是否使用AI分析
        
    Returns:
        是否转换成功
    """
    try:
        # 检查输入文件
        if not os.path.exists(input_path):
            print(f"输入文件不存在: {input_path}")
            return False
            
        # 生成输出路径
        if not output_path:
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}_公文格式.docx"
            
        print(f"开始转换: {input_path}")
        print(f"输出文件: {output_path}")
        
        # 创建文档管理器
        doc_manager = DocumentManager()
        doc = doc_manager.open_document(input_path)
        
        # 分析文档结构
        print("正在分析文档结构...")
        analysis = doc_manager.analyze_document(use_ai=use_ai)
        
        # 应用公文格式
        print("正在应用公文格式...")
        apply_official_formatting(doc_manager, analysis)
        
        # 保存文档
        print("正在保存文档...")
        if doc_manager.save_document(output_path):
            print(f"转换完成: {output_path}")
            return True
        else:
            print("保存文档失败")
            return False
            
    except Exception as e:
        print(f"转换失败: {e}")
        return False


def apply_official_formatting(doc_manager: DocumentManager, analysis: dict):
    """
    应用公文格式
    
    Args:
        doc_manager: 文档管理器
        analysis: 文档分析结果
    """
    formatting_manager = doc_manager.formatting_manager
    doc = doc_manager.document
    
    # 设置页面格式
    formatting_manager.set_page_format(
        page_width=21.0,  # A4宽度
        page_height=29.7,  # A4高度
        left_margin=2.8,
        right_margin=2.6,
        top_margin=3.7,
        bottom_margin=3.5
    )
    
    # 获取段落类型映射
    paragraph_types = {}
    if "ai_analysis" in analysis and "paragraphs" in analysis["ai_analysis"]:
        for para_info in analysis["ai_analysis"]["paragraphs"]:
            paragraph_types[para_info["index"]] = para_info["type"]
    
    # 遍历段落并应用格式
    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        if not text:
            continue
            
        # 获取段落类型
        para_type = paragraph_types.get(i, "正文")
        
        # 根据类型应用格式
        if para_type == "标题":
            apply_title_format(para, formatting_manager)
        elif para_type == "一级标题":
            apply_heading1_format(para, formatting_manager)
        elif para_type == "二级标题":
            apply_heading2_format(para, formatting_manager)
        elif para_type == "三级标题":
            apply_heading3_format(para, formatting_manager)
        elif para_type == "四级标题":
            apply_heading4_format(para, formatting_manager)
        elif para_type == "落款":
            apply_signature_format(para, formatting_manager)
        else:
            apply_body_format(para, formatting_manager)
    
    # 处理表格
    for table in doc.tables:
        apply_table_format(table, formatting_manager)


def apply_title_format(paragraph, formatting_manager: FormattingManager):
    """应用标题格式"""
    formatting_manager.set_paragraph_format(
        paragraph,
        alignment="center",
        line_spacing=30,  # 30磅
        space_before=0,
        space_after=0
    )
    
    for run in paragraph.runs:
        formatting_manager.set_font(
            run,
            font_name="方正小标宋简体",
            font_size=22,  # 二号
            bold=False,
            color="#000000"
        )


def apply_heading1_format(paragraph, formatting_manager: FormattingManager):
    """应用一级标题格式"""
    formatting_manager.set_paragraph_format(
        paragraph,
        alignment="left",
        line_spacing=28,  # 28磅
        space_before=12,
        space_after=6,
        first_line_indent=0
    )
    
    for run in paragraph.runs:
        formatting_manager.set_font(
            run,
            font_name="黑体",
            font_size=16,  # 三号
            bold=False,
            color="#000000"
        )


def apply_heading2_format(paragraph, formatting_manager: FormattingManager):
    """应用二级标题格式"""
    formatting_manager.set_paragraph_format(
        paragraph,
        alignment="left",
        line_spacing=28,
        space_before=6,
        space_after=6,
        first_line_indent=0
    )
    
    for run in paragraph.runs:
        formatting_manager.set_font(
            run,
            font_name="楷体_GB2312",
            font_size=16,  # 三号
            bold=False,
            color="#000000"
        )


def apply_heading3_format(paragraph, formatting_manager: FormattingManager):
    """应用三级标题格式"""
    formatting_manager.set_paragraph_format(
        paragraph,
        alignment="left",
        line_spacing=28,
        space_before=6,
        space_after=6,
        first_line_indent=0
    )
    
    for run in paragraph.runs:
        formatting_manager.set_font(
            run,
            font_name="仿宋_GB2312",
            font_size=16,  # 三号
            bold=True,  # 加粗
            color="#000000"
        )


def apply_heading4_format(paragraph, formatting_manager: FormattingManager):
    """应用四级标题格式"""
    formatting_manager.set_paragraph_format(
        paragraph,
        alignment="left",
        line_spacing=28,
        space_before=6,
        space_after=6,
        first_line_indent=0
    )
    
    for run in paragraph.runs:
        formatting_manager.set_font(
            run,
            font_name="仿宋_GB2312",
            font_size=16,  # 三号
            bold=False,
            color="#000000"
        )


def apply_body_format(paragraph, formatting_manager: FormattingManager):
    """应用正文格式"""
    formatting_manager.set_paragraph_format(
        paragraph,
        alignment="justify",  # 两端对齐
        line_spacing=28,  # 28磅
        space_before=0,
        space_after=0,
        first_line_indent=32  # 首行缩进2字符
    )
    
    for run in paragraph.runs:
        formatting_manager.set_font(
            run,
            font_name="仿宋_GB2312",
            font_size=16,  # 三号
            bold=False,
            color="#000000"
        )


def apply_signature_format(paragraph, formatting_manager: FormattingManager):
    """应用落款格式"""
    formatting_manager.set_paragraph_format(
        paragraph,
        alignment="right",
        line_spacing=28,
        space_before=0,
        space_after=0,
        right_indent=96  # 右空四字
    )
    
    for run in paragraph.runs:
        formatting_manager.set_font(
            run,
            font_name="仿宋_GB2312",
            font_size=16,  # 三号
            bold=False,
            color="#000000"
        )


def apply_table_format(table, formatting_manager: FormattingManager):
    """应用表格格式"""
    # 设置表格格式
    formatting_manager.set_table_format(
        table,
        alignment="center",
        borders=True,
        border_color="000000",
        border_size=1
    )
    
    # 设置单元格格式
    for row in table.rows:
        for cell in row.cells:
            # 设置单元格内边距
            formatting_manager.set_cell_format(
                cell,
                vertical_alignment="center"
            )
            
            # 设置单元格内段落格式
            for para in cell.paragraphs:
                formatting_manager.set_paragraph_format(
                    para,
                    alignment="center",
                    line_spacing=28,
                    space_before=0,
                    space_after=0
                )
                
                for run in para.runs:
                    formatting_manager.set_font(
                        run,
                        font_name="仿宋_GB2312",
                        font_size=12,  # 小四号
                        bold=False,
                        color="#000000"
                    )


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="公文格式转换工具")
    parser.add_argument("input", help="输入文档路径")
    parser.add_argument("-o", "--output", help="输出文档路径")
    parser.add_argument("--no-ai", action="store_true", help="不使用AI分析")
    
    args = parser.parse_args()
    
    # 转换文档
    success = convert_to_official_format(
        args.input,
        args.output,
        use_ai=not args.no_ai
    )
    
    if success:
        print("转换成功！")
        sys.exit(0)
    else:
        print("转换失败！")
        sys.exit(1)


if __name__ == "__main__":
    main()