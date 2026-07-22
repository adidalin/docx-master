"""
格式管理模块
提供字体、段落、页面等格式控制功能
"""

from typing import Dict, List, Optional, Union, Any
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


class FormattingManager:
    """格式管理器，提供文档格式控制功能"""
    
    def __init__(self, document: Document):
        """
        初始化格式管理器
        
        Args:
            document: Document对象
        """
        self.document = document
        
    def set_font(self, run, font_name: Optional[str] = None, 
                 font_size: Optional[int] = None, bold: Optional[bool] = None,
                 italic: Optional[bool] = None, color: Optional[str] = None,
                 underline: Optional[bool] = None, strikethrough: Optional[bool] = None):
        """
        设置字体格式
        
        Args:
            run: Run对象
            font_name: 字体名称
            font_size: 字体大小（磅）
            bold: 是否加粗
            italic: 是否斜体
            color: 颜色（十六进制）
            underline: 是否下划线
            strikethrough: 是否删除线
        """
        if font_name:
            run.font.name = font_name
            # 设置东亚字体
            run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
            
        if font_size:
            run.font.size = Pt(font_size)
            
        if bold is not None:
            run.font.bold = bold
            
        if italic is not None:
            run.font.italic = italic
            
        if color:
            # 移除#号（如果有）
            color = color.lstrip('#')
            run.font.color.rgb = RGBColor.from_string(color)
            
        if underline is not None:
            run.font.underline = underline
            
        if strikethrough is not None:
            run.font.strikethrough = strikethrough
    
    def set_paragraph_format(self, paragraph, alignment: Optional[str] = None,
                            line_spacing: Optional[float] = None,
                            line_spacing_rule: Optional[str] = None,
                            space_before: Optional[int] = None,
                            space_after: Optional[int] = None,
                            first_line_indent: Optional[int] = None,
                            first_line_indent_chars: Optional[int] = None,
                            left_indent: Optional[int] = None,
                            left_indent_chars: Optional[int] = None,
                            right_indent: Optional[int] = None,
                            right_indent_chars: Optional[int] = None,
                            keep_together: Optional[bool] = None,
                            keep_with_next: Optional[bool] = None,
                            page_break_before: Optional[bool] = None,
                            widow_control: Optional[bool] = None):
        """
        设置段落格式
        
        Args:
            paragraph: Paragraph对象
            alignment: 对齐方式（left, center, right, justify）
            line_spacing: 行距（倍数或磅值）
            line_spacing_rule: 行距规则（auto:倍数, at_least:最小值, exact:固定值）
            space_before: 段前间距（磅）
            space_after: 段后间距（磅）
            first_line_indent: 首行缩进（磅）
            first_line_indent_chars: 首行缩进（字符数，如2表示2个字符）
            left_indent: 左缩进（磅）
            left_indent_chars: 左缩进（字符数）
            right_indent: 右缩进（磅）
            right_indent_chars: 右缩进（字符数）
            keep_together: 段前分页
            keep_with_next: 与下段同页
            page_break_before: 段前分页
            widow_control: 孤行控制
        """
        if alignment:
            alignment_map = {
                "left": WD_ALIGN_PARAGRAPH.LEFT,
                "center": WD_ALIGN_PARAGRAPH.CENTER,
                "right": WD_ALIGN_PARAGRAPH.RIGHT,
                "justify": WD_ALIGN_PARAGRAPH.JUSTIFY
            }
            if alignment.lower() in alignment_map:
                paragraph.alignment = alignment_map[alignment.lower()]
                
        if line_spacing is not None:
            # 设置行距
            if line_spacing_rule is None:
                # 默认使用倍数行距
                line_spacing_rule = "auto"
            
            if line_spacing_rule.lower() == "auto":
                # 倍数行距（如1.5倍行距）
                paragraph.paragraph_format.line_spacing = line_spacing
            elif line_spacing_rule.lower() == "exact":
                # 固定行距（磅值）
                paragraph.paragraph_format.line_spacing = Pt(line_spacing)
                pPr = paragraph._element.get_or_add_pPr()
                spacing = pPr.find(qn('w:spacing'))
                if spacing is None:
                    spacing = OxmlElement('w:spacing')
                    pPr.append(spacing)
                spacing.set(qn('w:lineRule'), 'exact')
            elif line_spacing_rule.lower() == "at_least":
                # 最小行距（磅值）
                paragraph.paragraph_format.line_spacing = Pt(line_spacing)
                pPr = paragraph._element.get_or_add_pPr()
                spacing = pPr.find(qn('w:spacing'))
                if spacing is None:
                    spacing = OxmlElement('w:spacing')
                    pPr.append(spacing)
                spacing.set(qn('w:lineRule'), 'atLeast')
            
        # 段前段后间距（默认为0行）
        if space_before is not None:
            # 使用行单位（1行 = 240 DXA，约12pt）
            pPr = paragraph._element.get_or_add_pPr()
            spacing = pPr.find(qn('w:spacing'))
            if spacing is None:
                spacing = OxmlElement('w:spacing')
                pPr.append(spacing)
            # 设置段前间距（行单位）
            spacing.set(qn('w:beforeLines'), str(int(space_before * 100)))
            # 同时设置DXA单位作为备用
            spacing.set(qn('w:before'), str(int(space_before * 240)))
        else:
            # 默认0行
            pPr = paragraph._element.get_or_add_pPr()
            spacing = pPr.find(qn('w:spacing'))
            if spacing is None:
                spacing = OxmlElement('w:spacing')
                pPr.append(spacing)
            spacing.set(qn('w:beforeLines'), '0')
            spacing.set(qn('w:before'), '0')
            
        if space_after is not None:
            # 使用行单位（1行 = 240 DXA，约12pt）
            pPr = paragraph._element.get_or_add_pPr()
            spacing = pPr.find(qn('w:spacing'))
            if spacing is None:
                spacing = OxmlElement('w:spacing')
                pPr.append(spacing)
            # 设置段后间距（行单位）
            spacing.set(qn('w:afterLines'), str(int(space_after * 100)))
            # 同时设置DXA单位作为备用
            spacing.set(qn('w:after'), str(int(space_after * 240)))
        else:
            # 默认0行
            pPr = paragraph._element.get_or_add_pPr()
            spacing = pPr.find(qn('w:spacing'))
            if spacing is None:
                spacing = OxmlElement('w:spacing')
                pPr.append(spacing)
            spacing.set(qn('w:afterLines'), '0')
            spacing.set(qn('w:after'), '0')
            
        # 首行缩进：优先使用字符单位
        if first_line_indent_chars is not None:
            # 使用字符单位（如2表示缩进2个字符宽度）
            pPr = paragraph._element.get_or_add_pPr()
            ind = pPr.find(qn('w:ind'))
            if ind is None:
                ind = OxmlElement('w:ind')
                pPr.append(ind)
            # 字符单位：200 = 2个字符宽度（百分之一字符）
            ind.set(qn('w:firstLineChars'), str(first_line_indent_chars * 100))
            # 同时设置DXA单位作为备用（五号字约10.5pt，2字符约420 DXA）
            ind.set(qn('w:firstLine'), str(first_line_indent_chars * 420))
        elif first_line_indent is not None:
            paragraph.paragraph_format.first_line_indent = Pt(first_line_indent)
            
        if left_indent_chars is not None:
            # 使用字符单位
            pPr = paragraph._element.get_or_add_pPr()
            ind = pPr.find(qn('w:ind'))
            if ind is None:
                ind = OxmlElement('w:ind')
                pPr.append(ind)
            ind.set(qn('w:leftChars'), str(left_indent_chars * 100))
            ind.set(qn('w:left'), str(left_indent_chars * 420))
        elif left_indent is not None:
            paragraph.paragraph_format.left_indent = Pt(left_indent)
            
        if right_indent_chars is not None:
            # 使用字符单位
            pPr = paragraph._element.get_or_add_pPr()
            ind = pPr.find(qn('w:ind'))
            if ind is None:
                ind = OxmlElement('w:ind')
                pPr.append(ind)
            ind.set(qn('w:rightChars'), str(right_indent_chars * 100))
            ind.set(qn('w:right'), str(right_indent_chars * 420))
        elif right_indent is not None:
            paragraph.paragraph_format.right_indent = Pt(right_indent)
            
        if keep_together is not None:
            paragraph.paragraph_format.keep_together = keep_together
            
        if keep_with_next is not None:
            paragraph.paragraph_format.keep_with_next = keep_with_next
            
        if page_break_before is not None:
            paragraph.paragraph_format.page_break_before = page_break_before
            
        if widow_control is not None:
            paragraph.paragraph_format.widow_control = widow_control
    
    def set_page_format(self, section=None, page_width: Optional[int] = None,
                       page_height: Optional[int] = None,
                       left_margin: Optional[int] = None,
                       right_margin: Optional[int] = None,
                       top_margin: Optional[int] = None,
                       bottom_margin: Optional[int] = None,
                       orientation: Optional[str] = None,
                       header_distance: Optional[int] = None,
                       footer_distance: Optional[int] = None,
                       gutter: Optional[int] = None):
        """
        设置页面格式
        
        Args:
            section: Section对象，如果不提供则使用第一个节
            page_width: 页面宽度（厘米）
            page_height: 页面高度（厘米）
            left_margin: 左边距（厘米）
            right_margin: 右边距（厘米）
            top_margin: 上边距（厘米）
            bottom_margin: 下边距（厘米）
            orientation: 页面方向（portrait, landscape）
            header_distance: 页眉距离（厘米）
            footer_distance: 页脚距离（厘米）
            gutter: 装订线（厘米）
        """
        if section is None:
            if self.document.sections:
                section = self.document.sections[0]
            else:
                return
                
        if page_width is not None:
            section.page_width = Cm(page_width)
            
        if page_height is not None:
            section.page_height = Cm(page_height)
            
        if left_margin is not None:
            section.left_margin = Cm(left_margin)
            
        if right_margin is not None:
            section.right_margin = Cm(right_margin)
            
        if top_margin is not None:
            section.top_margin = Cm(top_margin)
            
        if bottom_margin is not None:
            section.bottom_margin = Cm(bottom_margin)
            
        if orientation:
            if orientation.lower() == "landscape":
                section.orientation = WD_ORIENT.LANDSCAPE
            else:
                section.orientation = WD_ORIENT.PORTRAIT
                
        if header_distance is not None:
            section.header_distance = Cm(header_distance)
            
        if footer_distance is not None:
            section.footer_distance = Cm(footer_distance)
            
        if gutter is not None:
            section.gutter = Cm(gutter)
    
    def set_table_format(self, table, alignment: Optional[str] = None,
                        borders: Optional[bool] = None,
                        border_color: Optional[str] = None,
                        border_size: Optional[int] = None,
                        cell_padding: Optional[int] = None,
                        cell_spacing: Optional[int] = None):
        """
        设置表格格式
        
        Args:
            table: Table对象
            alignment: 表格对齐方式（left, center, right）
            borders: 是否显示边框
            border_color: 边框颜色（十六进制）
            border_size: 边框大小（磅）
            cell_padding: 单元格内边距（磅）
            cell_spacing: 单元格间距（磅）
        """
        if alignment:
            alignment_map = {
                "left": WD_TABLE_ALIGNMENT.LEFT,
                "center": WD_TABLE_ALIGNMENT.CENTER,
                "right": WD_TABLE_ALIGNMENT.RIGHT
            }
            if alignment.lower() in alignment_map:
                table.alignment = alignment_map[alignment.lower()]
                
        if borders is not None:
            if borders:
                # 添加边框
                tbl = table._tbl
                tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement('w:tblPr')
                
                borders_element = OxmlElement('w:tblBorders')
                for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
                    border = OxmlElement(f'w:{border_name}')
                    border.set(qn('w:val'), 'single')
                    
                    if border_color:
                        border.set(qn('w:color'), border_color.lstrip('#'))
                        
                    if border_size:
                        border.set(qn('w:sz'), str(border_size * 2))  # 转换为半磅
                        
                    border.set(qn('w:space'), '0')
                    borders_element.append(border)
                    
                tblPr.append(borders_element)
            else:
                # 移除边框
                tbl = table._tbl
                tblPr = tbl.tblPr
                if tblPr is not None:
                    borders_element = tblPr.find(qn('w:tblBorders'))
                    if borders_element is not None:
                        tblPr.remove(borders_element)
                        
        if cell_padding is not None:
            # 设置单元格内边距
            for row in table.rows:
                for cell in row.cells:
                    tc = cell._tc
                    tcPr = tc.get_or_add_tcPr()
                    
                    mar = OxmlElement('w:tcMar')
                    for side in ['top', 'left', 'bottom', 'right']:
                        margin = OxmlElement(f'w:{side}')
                        margin.set(qn('w:w'), str(cell_padding * 20))  # 转换为DXA
                        margin.set(qn('w:type'), 'dxa')
                        mar.append(margin)
                        
                    tcPr.append(mar)
                    
        if cell_spacing is not None:
            # 设置单元格间距
            tbl = table._tbl
            tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement('w:tblPr')
            
            cell_spacing_element = OxmlElement('w:tblCellSpacing')
            cell_spacing_element.set(qn('w:w'), str(cell_spacing * 20))  # 转换为DXA
            cell_spacing_element.set(qn('w:type'), 'dxa')
            tblPr.append(cell_spacing_element)
    
    def set_cell_format(self, cell, width: Optional[int] = None,
                       height: Optional[int] = None,
                       vertical_alignment: Optional[str] = None,
                       background_color: Optional[str] = None,
                       text_direction: Optional[str] = None):
        """
        设置单元格格式
        
        Args:
            cell: Cell对象
            width: 单元格宽度（厘米）
            height: 单元格高度（厘米）
            vertical_alignment: 垂直对齐方式（top, center, bottom）
            background_color: 背景颜色（十六进制）
            text_direction: 文字方向（lr, tb, rl）
        """
        if width is not None:
            cell.width = Cm(width)
            
        if height is not None:
            cell.height = Cm(height)
            
        if vertical_alignment:
            alignment_map = {
                "top": "top",
                "center": "center",
                "bottom": "bottom"
            }
            if vertical_alignment.lower() in alignment_map:
                cell.vertical_alignment = alignment_map[vertical_alignment.lower()]
                
        if background_color:
            # 设置背景颜色
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            shd.set(qn('w:fill'), background_color.lstrip('#'))
            tcPr.append(shd)
            
        if text_direction:
            # 设置文字方向
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            
            text_direction_element = OxmlElement('w:textDirection')
            text_direction_element.set(qn('w:val'), text_direction)
            tcPr.append(text_direction_element)
    
    def add_page_break(self, paragraph):
        """
        添加分页符
        
        Args:
            paragraph: Paragraph对象
        """
        run = paragraph.add_run()
        br = OxmlElement('w:br')
        br.set(qn('w:type'), 'page')
        run._element.append(br)
    
    def add_section_break(self, paragraph, break_type: str = "next_page"):
        """
        添加分节符
        
        Args:
            paragraph: Paragraph对象
            break_type: 分节符类型（next_page, continuous, even_page, odd_page）
        """
        type_map = {
            "next_page": "nextPage",
            "continuous": "continuous",
            "even_page": "evenPage",
            "odd_page": "oddPage"
        }
        
        if break_type not in type_map:
            raise ValueError(f"不支持的分节符类型: {break_type}")
            
        pPr = paragraph._element.get_or_add_pPr()
        sectPr = OxmlElement('w:sectPr')
        
        # 设置分节符类型
        type_element = OxmlElement('w:type')
        type_element.set(qn('w:val'), type_map[break_type])
        sectPr.append(type_element)
        
        pPr.append(sectPr)
    
    def remove_formatting(self, paragraph):
        """
        移除段落格式
        
        Args:
            paragraph: Paragraph对象
        """
        # 移除段落格式
        pPr = paragraph._element.pPr
        if pPr is not None:
            paragraph._element.remove(pPr)
            
        # 移除run格式
        for run in paragraph.runs:
            rPr = run._element.rPr
            if rPr is not None:
                run._element.remove(rPr)
    
    def copy_formatting(self, source_paragraph, target_paragraph):
        """
        复制段落格式
        
        Args:
            source_paragraph: 源段落
            target_paragraph: 目标段落
        """
        # 复制段落格式
        source_pPr = source_paragraph._element.pPr
        if source_pPr is not None:
            target_pPr = target_paragraph._element.get_or_add_pPr()
            target_pPr.clear()
            target_pPr.append(source_pPr.clone())
            
        # 复制run格式
        for i, source_run in enumerate(source_paragraph.runs):
            if i < len(target_paragraph.runs):
                target_run = target_paragraph.runs[i]
                source_rPr = source_run._element.rPr
                if source_rPr is not None:
                    target_rPr = target_run._element.get_or_add_rPr()
                    target_rPr.clear()
                    target_rPr.append(source_rPr.clone())
    
    def apply_style(self, paragraph, style_name: str):
        """
        应用样式
        
        Args:
            paragraph: Paragraph对象
            style_name: 样式名称
        """
        try:
            paragraph.style = self.document.styles[style_name]
        except KeyError:
            print(f"样式不存在: {style_name}")
    
    def create_custom_style(self, style_name: str, style_type: str = "paragraph",
                           font_name: Optional[str] = None, font_size: Optional[int] = None,
                           bold: Optional[bool] = None, italic: Optional[bool] = None,
                           color: Optional[str] = None, alignment: Optional[str] = None,
                           line_spacing: Optional[float] = None,
                           space_before: Optional[int] = None,
                           space_after: Optional[int] = None,
                           first_line_indent: Optional[int] = None):
        """
        创建自定义样式
        
        Args:
            style_name: 样式名称
            style_type: 样式类型（paragraph, character, table）
            font_name: 字体名称
            font_size: 字体大小
            bold: 是否加粗
            italic: 是否斜体
            color: 颜色
            alignment: 对齐方式
            line_spacing: 行距
            space_before: 段前间距
            space_after: 段后间距
            first_line_indent: 首行缩进
        """
        from docx.enum.style import WD_STYLE_TYPE
        
        type_map = {
            "paragraph": WD_STYLE_TYPE.PARAGRAPH,
            "character": WD_STYLE_TYPE.CHARACTER,
            "table": WD_STYLE_TYPE.TABLE
        }
        
        if style_type not in type_map:
            raise ValueError(f"不支持的样式类型: {style_type}")
            
        # 检查样式是否已存在
        if style_name in [s.name for s in self.document.styles]:
            print(f"样式已存在: {style_name}")
            return
            
        # 创建样式
        style = self.document.styles.add_style(style_name, type_map[style_type])
        
        # 设置字体格式
        if font_name:
            style.font.name = font_name
            style.font.element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
            
        if font_size:
            style.font.size = Pt(font_size)
            
        if bold is not None:
            style.font.bold = bold
            
        if italic is not None:
            style.font.italic = italic
            
        if color:
            color = color.lstrip('#')
            style.font.color.rgb = RGBColor.from_string(color)
            
        # 设置段落格式
        if style_type == "paragraph":
            if alignment:
                alignment_map = {
                    "left": WD_ALIGN_PARAGRAPH.LEFT,
                    "center": WD_ALIGN_PARAGRAPH.CENTER,
                    "right": WD_ALIGN_PARAGRAPH.RIGHT,
                    "justify": WD_ALIGN_PARAGRAPH.JUSTIFY
                }
                if alignment.lower() in alignment_map:
                    style.paragraph_format.alignment = alignment_map[alignment.lower()]
                    
            if line_spacing is not None:
                style.paragraph_format.line_spacing = line_spacing
                
            if space_before is not None:
                style.paragraph_format.space_before = Pt(space_before)
                
            if space_after is not None:
                style.paragraph_format.space_after = Pt(space_after)
                
            if first_line_indent is not None:
                style.paragraph_format.first_line_indent = Pt(first_line_indent)
                
        return style
    
    def get_formatting_info(self, paragraph) -> Dict[str, Any]:
        """
        获取段落格式信息
        
        Args:
            paragraph: Paragraph对象
            
        Returns:
            格式信息字典
        """
        info = {
            "paragraph": {},
            "runs": []
        }
        
        # 段落格式
        pPr = paragraph._element.pPr
        if pPr is not None:
            # 对齐方式
            jc = pPr.find(qn('w:jc'))
            if jc is not None:
                info["paragraph"]["alignment"] = jc.get(qn('w:val'))
                
            # 行距
            spacing = pPr.find(qn('w:spacing'))
            if spacing is not None:
                info["paragraph"]["line_spacing"] = spacing.get(qn('w:line'))
                info["paragraph"]["space_before"] = spacing.get(qn('w:before'))
                info["paragraph"]["space_after"] = spacing.get(qn('w:after'))
                
            # 缩进
            ind = pPr.find(qn('w:ind'))
            if ind is not None:
                info["paragraph"]["first_line_indent"] = ind.get(qn('w:firstLine'))
                info["paragraph"]["left_indent"] = ind.get(qn('w:left'))
                info["paragraph"]["right_indent"] = ind.get(qn('w:right'))
                
        # Run格式
        for run in paragraph.runs:
            run_info = {
                "text": run.text,
                "font_name": run.font.name,
                "font_size": run.font.size,
                "bold": run.font.bold,
                "italic": run.font.italic,
                "color": str(run.font.color.rgb) if run.font.color and run.font.color.rgb else None
            }
            info["runs"].append(run_info)
            
        return info