#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用docx-master技能生成学术论文（本地版本，不依赖API）
"""

import sys
import os

# 添加core目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.document import DocumentManager
from core.formatting import FormattingManager


# 预设的论文内容
PAPER_CONTENT = {
    "title": "教育数字化转型的内涵特征与实践路径研究",
    "subtitle": "",
    "abstract": "随着数字技术的迅猛发展，教育数字化转型已成为全球教育改革的核心议题。本文基于系统文献综述与案例分析方法，深入探讨教育数字化转型的内涵特征、关键要素与实践路径。研究发现，教育数字化转型不仅是技术工具的应用，更是教育理念、教学模式、治理方式和文化价值的系统性变革。当前教育数字化转型面临数字鸿沟加剧、教师素养不足、数据安全隐忧、传统惯性制约等多重挑战。为此，研究提出构建多元协同的数字化转型生态体系、强化教师数字素养培训、完善数据安全保障机制、推动教学模式创新等实施策略。本文认为，教育数字化转型应以促进教育公平和可持续发展为根本价值取向，通过顶层设计与基层探索的有机融合，实现教育系统的整体性跃迁与活力重塑。本研究为教育数字化转型的决策者、学校管理者和一线教师提供了理论参考与实践指导。",
    "keywords": ["教育数字化转型", "数字素养", "智慧教育", "教育公平", "教育治理"],
    "sections": [
        {
            "title": "一、引言",
            "content": "当今世界正经历深刻的数字化变革，数字技术已渗透到社会各个领域，深刻改变着人类的生产生活方式。《教育强国建设规划纲要（2024—2035年）》明确提出实施"国家教育数字化战略"，坚持应用导向、治理为基，推动集成化、智能化、国际化，建强用好国家智慧教育公共服务平台，建立横纵贯通、协同服务的数字教育体系。教育数字化转型已成为教育现代化的必然选择和核心驱动力。然而，教育数字化转型是一项复杂的系统工程，涉及技术、组织、文化等多个维度的深刻变革。如何准确把握教育数字化转型的内涵特征，识别关键要素与实施路径，对于推进教育高质量发展具有重要的理论意义和实践价值。",
            "subsections": []
        },
        {
            "title": "二、教育数字化转型的理论基础",
            "content": "教育数字化转型的理论基础涉及多个学科领域，需要从技术哲学、组织变革理论和教育学等多重视角进行审视。",
            "subsections": [
                {
                    "title": "（一）数字化转型的概念演进",
                    "content": "数字化转型概念最早源于企业管理领域，指组织通过数字技术的深度应用，实现业务流程、组织结构和价值创造模式的根本性变革。",
                    "subsubsections": [
                        {
                            "title": "1.从数字化到数字化转型",
                            "content": "数字化（Digitization）主要指将模拟信息转换为数字格式的过程，而数字化转型（Digital Transformation）则是利用数字技术创造新的或修改现有的业务流程、文化和客户体验，以满足不断变化的业务和市场需求。在教育领域，数字化转型超越了简单的技术应用，指向教育系统的整体性变革。"
                        },
                        {
                            "title": "2.教育数字化转型的内涵界定",
                            "content": "教育数字化转型是指在数字技术赋能下，教育系统在理念、模式、结构、流程、文化等方面发生的系统性、根本性变革。它不仅关注技术工具的应用，更强调技术与教育的深度融合，推动教育生态的重构与优化。"
                        }
                    ]
                },
                {
                    "title": "（二）相关理论框架",
                    "content": "教育数字化转型的理论框架主要包括技术接受模型（TAM）、统一技术接受与使用理论（UTAUT）、社会技术系统理论等。这些理论从不同角度解释了技术采纳与扩散的机制，为理解教育数字化转型提供了重要的分析工具。",
                    "subsubsections": []
                }
            ]
        },
        {
            "title": "三、教育数字化转型的关键要素",
            "content": "教育数字化转型是一个多要素协同作用的复杂过程，涉及基础设施、数字资源、教学模式、教师素养、治理体系等多个方面。",
            "subsections": [
                {
                    "title": "（一）数字基础设施建设",
                    "content": "数字基础设施是教育数字化转型的物质基础，包括网络环境、终端设备、数据中心、云平台等。高速、稳定、安全的网络环境是支撑数字化教学的前提条件。",
                    "subsubsections": [
                        {
                            "title": "1.网络环境优化",
                            "content": "5G网络的商用为教育场景带来了低延迟、高带宽、大连接的技术特性，使得高清视频互动、虚拟现实教学、远程实验等应用成为可能。校园网络的全面覆盖和质量提升是教育数字化转型的基础工程。"
                        },
                        {
                            "title": "2.智慧学习空间构建",
                            "content": "智慧学习空间整合了物理环境与数字环境，支持多种教学模式的灵活切换。智能教室、创新实验室、虚拟仿真中心等新型学习空间为学生提供了更加丰富、多元的学习体验。"
                        }
                    ]
                },
                {
                    "title": "（二）数字教育资源体系",
                    "content": "优质数字教育资源是教育数字化转型的核心要素。国家智慧教育公共服务平台汇聚了海量的教育资源，覆盖各学段、各学科，为师生提供了丰富的学习材料。",
                    "subsubsections": []
                },
                {
                    "title": "（三）教师数字素养提升",
                    "content": "教师是教育数字化转型的关键主体。教师数字素养不仅包括技术操作能力，更重要的是技术与教学深度融合的能力，即运用数字技术优化教学设计、创新教学方法、提升教学效果的能力。",
                    "subsubsections": []
                }
            ]
        },
        {
            "title": "四、教育数字化转型的实践路径",
            "content": "教育数字化转型需要系统规划、分步实施，从顶层设计到基层探索形成有机联动。",
            "subsections": [
                {
                    "title": "（一）构建协同推进机制",
                    "content": "教育数字化转型需要政府、学校、企业、社会多方协同。政府负责顶层设计和政策引导，学校是实施主体，企业提供技术支持，社会营造良好的舆论环境。",
                    "subsubsections": [
                        {
                            "title": "1.政策保障体系",
                            "content": "完善的政策保障体系是教育数字化转型顺利推进的关键。需要从资金投入、标准规范、评估监督等方面建立健全政策框架，为数字化转型提供制度保障。"
                        }
                    ]
                },
                {
                    "title": "（二）推进教学模式创新",
                    "content": "教学模式创新是教育数字化转型的核心任务。要充分利用数字技术的优势，探索混合式教学、翻转课堂、项目式学习等新型教学模式，提升教学质量和学习效果。",
                    "subsubsections": []
                }
            ]
        },
        {
            "title": "五、结论与展望",
            "content": "教育数字化转型是一项长期的、复杂的系统工程，需要持续投入和不断创新。本研究系统梳理了教育数字化转型的内涵特征、关键要素和实践路径，为推进教育数字化转型提供了理论参考。展望未来，随着人工智能、大数据、区块链等新兴技术的不断发展，教育数字化转型将进入新的阶段。我们需要保持开放的心态，积极拥抱技术变革，同时坚守教育的本质和价值取向，确保技术服务于人的全面发展。教育数字化转型的最终目标是构建更加公平、更高质量、更加开放的教育体系，为每一个学习者提供适合的教育，促进人的全面发展和社会的可持续进步。",
            "subsections": []
        }
    ],
    "references": [
        "[1]祝智庭,胡姣.教育数字化转型的本质探析与研究展望[J].中国电化教育,2022,(4):1-8.",
        "[2]黄荣怀.教育数字化转型的内涵与实施路径[J].现代远程教育研究,2022,34(3):12-19.",
        "[3]杨宗凯.以教育数字化赋能教育强国建设[J].人民教育,2023,(1):27-30.",
        "[4]吴砥,陈敏.教育数字化转型的核心要素与推进策略[J].开放教育研究,2023,29(1):17-25.",
        "[5]余胜泉.教育数字化转型的关键问题与发展趋势[J].电化教育研究,2023,44(2):5-13.",
        "[6]顾小清,王炜.教师数字素养：概念、框架与培养路径[J].华东师范大学学报(教育科学版),2023,41(3):1-12.",
        "[7]刘邦奇.人工智能赋能教育数字化转型：机遇、挑战与对策[J].中国远程教育,2023,(5):1-10.",
        "[8]张治,朱益明.智慧教育公共服务体系建设研究[J].现代教育技术,2023,33(4):5-12.",
        "[9]UNESCO. Transforming education: The power of digital technologies[R]. Paris: UNESCO, 2023.",
        "[10]OECD. Digital education outlook 2023: Embracing the digital transformation in education[R]. Paris: OECD Publishing, 2023."
    ]
}


def create_paper_document(content, output_path):
    """按照论文格式模板创建Word文档"""
    
    # 创建文档管理器
    doc_manager = DocumentManager()
    doc = doc_manager.create_document()
    formatting_manager = FormattingManager(doc)
    
    # 设置页面格式（A4）
    formatting_manager.set_page_format(
        page_width=21.0,   # A4宽度
        page_height=29.7,  # A4高度
        left_margin=2.5,
        right_margin=2.5,
        top_margin=2.5,
        bottom_margin=2.5
    )
    
    # ========== 标题（宋体，加黑，小二号，左对齐） ==========
    title = doc_manager.add_paragraph()
    run = title.add_run(content.get("title", "论文标题"))
    formatting_manager.set_font(run, font_name="SimSun", font_size=18, bold=True)  # 小二号约18pt
    formatting_manager.set_paragraph_format(title, alignment="left")
    
    # ========== 副标题（如果有） ==========
    subtitle = content.get("subtitle", "")
    if subtitle:
        sub_para = doc_manager.add_paragraph()
        run = sub_para.add_run(f"——{subtitle}")
        formatting_manager.set_font(run, font_name="SimSun", font_size=16)  # 小三号约16pt
        formatting_manager.set_paragraph_format(sub_para, alignment="left")
    
    # ========== 摘要（宋体加黑标题 + 楷体内容，小五号） ==========
    abstract_para = doc_manager.add_paragraph()
    # 摘要标题
    run1 = abstract_para.add_run("摘要")
    formatting_manager.set_font(run1, font_name="SimSun", font_size=9, bold=True)  # 小五号约9pt
    # 摘要内容
    run2 = abstract_para.add_run("：" + content.get("abstract", ""))
    formatting_manager.set_font(run2, font_name="KaiTi", font_size=9)  # 楷体小五号
    formatting_manager.set_paragraph_format(abstract_para, alignment="left")
    
    # ========== 关键词 ==========
    keywords = content.get("keywords", [])
    keywords_text = "；".join(keywords)
    kw_para = doc_manager.add_paragraph()
    run1 = kw_para.add_run("关键词")
    formatting_manager.set_font(run1, font_name="SimSun", font_size=9, bold=True)
    run2 = kw_para.add_run("：" + keywords_text)
    formatting_manager.set_font(run2, font_name="KaiTi", font_size=9)
    formatting_manager.set_paragraph_format(kw_para, alignment="left")
    
    # ========== 中图分类号和文献标识码 ==========
    info_para = doc_manager.add_paragraph()
    run = info_para.add_run("中图分类号：G434    文献标识码：A")
    formatting_manager.set_font(run, font_name="SimSun", font_size=9)
    formatting_manager.set_paragraph_format(info_para, alignment="left")
    
    # 空行
    doc_manager.add_paragraph("")
    
    # ========== 正文部分 ==========
    sections = content.get("sections", [])
    for section in sections:
        # 一级标题（黑体，小四号）
        h1_para = doc_manager.add_paragraph()
        run = h1_para.add_run(section.get("title", ""))
        formatting_manager.set_font(run, font_name="SimHei", font_size=12, bold=True)  # 小四号约12pt
        formatting_manager.set_paragraph_format(h1_para, alignment="left")
        
        # 一级标题下的正文（宋体，五号）
        section_content = section.get("content", "")
        if section_content:
            body_para = doc_manager.add_paragraph()
            run = body_para.add_run(section_content)
            formatting_manager.set_font(run, font_name="SimSun", font_size=10.5)  # 五号约10.5pt
            formatting_manager.set_paragraph_format(body_para, alignment="left", first_line_indent=24, line_spacing=1.5)
        
        # 二级标题
        subsections = section.get("subsections", [])
        for subsection in subsections:
            h2_para = doc_manager.add_paragraph()
            run = h2_para.add_run(subsection.get("title", ""))
            formatting_manager.set_font(run, font_name="SimSun", font_size=10.5)  # 五号
            formatting_manager.set_paragraph_format(h2_para, alignment="left")
            
            # 二级标题下的正文
            sub_content = subsection.get("content", "")
            if sub_content:
                sub_body = doc_manager.add_paragraph()
                run = sub_body.add_run(sub_content)
                formatting_manager.set_font(run, font_name="SimSun", font_size=10.5)
                formatting_manager.set_paragraph_format(sub_body, alignment="left", first_line_indent=24, line_spacing=1.5)
            
            # 三级标题
            subsubsections = subsection.get("subsubsections", [])
            for subsubsection in subsubsections:
                h3_para = doc_manager.add_paragraph()
                run = h3_para.add_run(subsubsection.get("title", ""))
                formatting_manager.set_font(run, font_name="SimSun", font_size=10.5)
                formatting_manager.set_paragraph_format(h3_para, alignment="left")
                
                # 三级标题下的正文
                subsub_content = subsubsection.get("content", "")
                if subsub_content:
                    subsub_body = doc_manager.add_paragraph()
                    run = subsub_body.add_run(subsub_content)
                    formatting_manager.set_font(run, font_name="SimSun", font_size=10.5)
                    formatting_manager.set_paragraph_format(subsub_body, alignment="left", first_line_indent=24, line_spacing=1.5)
    
    # ========== 参考文献 ==========
    doc_manager.add_paragraph("")  # 空行
    
    # 参考文献标题（宋体，加黑，小五号）
    ref_title = doc_manager.add_paragraph()
    run = ref_title.add_run("参考文献")
    formatting_manager.set_font(run, font_name="SimSun", font_size=9, bold=True)
    formatting_manager.set_paragraph_format(ref_title, alignment="left")
    
    # 参考文献内容（宋体，小五号）
    references = content.get("references", [])
    for ref in references:
        ref_para = doc_manager.add_paragraph()
        run = ref_para.add_run(ref)
        formatting_manager.set_font(run, font_name="SimSun", font_size=9)
        formatting_manager.set_paragraph_format(ref_para, alignment="left")
    
    # 保存文档
    doc_manager.save_document(output_path)
    return True


def main():
    """主函数"""
    print("=" * 60)
    print("学术论文生成器")
    print("使用docx-master技能")
    print("=" * 60)
    
    content = PAPER_CONTENT
    
    print(f"\n论文标题: {content['title']}")
    print(f"摘要字数: {len(content['abstract'])}")
    print(f"关键词: {', '.join(content['keywords'])}")
    print(f"章节数: {len(content['sections'])}")
    print(f"参考文献数: {len(content['references'])}")
    
    # 创建Word文档
    output_path = os.path.join(os.path.dirname(__file__), "教育数字化转型论文.docx")
    print(f"\n正在创建Word文档...")
    
    if create_paper_document(content, output_path):
        print(f"\n论文已保存到: {output_path}")
        print("=" * 60)
        print("论文生成完成！")
        print("=" * 60)
    else:
        print("创建文档失败！")


if __name__ == "__main__":
    main()