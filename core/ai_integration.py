"""
AI集成模块
提供与DeepSeek API的集成，用于文档分析和优化
"""

import os
import json
import requests
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class AIConfig:
    """AI配置"""
    api_url: str = "https://api.deepseek.com/chat/completions"
    api_key: str = ""
    model: str = "deepseek-chat"
    temperature: float = 0.1
    max_tokens: int = 4000
    timeout: int = 60


class AIIntegration:
    """AI集成类，提供与DeepSeek API的集成"""
    
    def __init__(self, config: Optional[AIConfig] = None):
        """
        初始化AI集成
        
        Args:
            config: AI配置，如果不提供则使用默认配置
        """
        self.config = config or AIConfig()
        
        # 从环境变量获取API密钥
        if not self.config.api_key:
            self.config.api_key = os.environ.get("DEEPSEEK_API_KEY", "")
            
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.api_key}"
        }
        
    def call_api(self, prompt: str, system_message: Optional[str] = None) -> Optional[str]:
        """
        调用DeepSeek API
        
        Args:
            prompt: 用户提示
            system_message: 系统消息
            
        Returns:
            API响应内容
        """
        if not self.config.api_key:
            print("API密钥未设置")
            return None
            
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
            
        messages.append({"role": "user", "content": prompt})
        
        data = {
            "model": self.config.model,
            "messages": messages,
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens
        }
        
        try:
            response = requests.post(
                self.config.api_url,
                headers=self.headers,
                json=data,
                timeout=self.config.timeout
            )
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            print(f"API调用失败: {e}")
            return None
        except (KeyError, IndexError) as e:
            print(f"API响应格式错误: {e}")
            return None
    
    def analyze_structure(self, document_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        分析文档结构
        
        Args:
            document_data: 文档数据
            
        Returns:
            分析结果
        """
        # 准备分析内容
        content_parts = []
        
        # 分析段落
        for para in document_data.get("paragraphs", [])[:50]:  # 限制前50段
            text = para.get("text", "").strip()
            if text:
                content_parts.append(f"[{para['index']}] {text}")
                
        content = "\n".join(content_parts)
        
        prompt = f"""请分析以下文档的结构，识别每个段落的类型和格式要求。

文档内容：
{content}

请以JSON格式返回分析结果，格式为：
{{
    "document_type": "文档类型（公文、学术、商务等）",
    "paragraphs": [
        {{
            "index": 0,
            "type": "段落类型（标题、一级标题、二级标题、正文、落款等）",
            "suggested_style": "建议的样式名称",
            "formatting_suggestions": {{
                "font_name": "建议字体",
                "font_size": "建议字号",
                "alignment": "建议对齐方式",
                "line_spacing": "建议行距",
                "first_line_indent": "建议首行缩进"
            }}
        }}
    ],
    "overall_suggestions": ["整体建议1", "整体建议2"]
}}"""
        
        system_message = """你是一个专业的文档排版助手，擅长分析文档结构和提供格式建议。
你熟悉各种文档格式标准，包括：
- 中国公文格式（GB/T 9704）
- 学术论文格式（APA、MLA、Chicago等）
- 商务文档格式
- 技术文档格式

请根据文档内容提供专业的格式建议。"""
        
        result = self.call_api(prompt, system_message)
        
        if result:
            try:
                # 尝试解析JSON
                analysis = json.loads(result)
                return analysis
            except json.JSONDecodeError:
                # 如果不是有效的JSON，返回原始文本
                return {"raw_response": result}
                
        return {}
    
    def correct_text(self, text: str) -> Dict[str, Any]:
        """
        文本纠错
        
        Args:
            text: 要纠错的文本
            
        Returns:
            纠错结果
        """
        prompt = f"""请检查以下文本，找出并纠正其中的错误，包括：
- 错别字（同音字、形近字错误）
- 漏字（如日期缺少"日"字）
- 明显的事实或格式错误
- 标点符号错误
- 数字与单位间多余空格清理

原文：
{text}

请以JSON格式返回纠错结果，格式为：
{{
    "corrected_text": "纠正后的文本",
    "corrections": [
        {{
            "original": "原文片段",
            "corrected": "纠正后片段",
            "type": "错误类型（错别字、漏字、格式错误等）",
            "explanation": "纠正原因"
        }}
    ],
    "statistics": {{
        "total_errors": 0,
        "error_types": {{
            "错别字": 0,
            "漏字": 0,
            "格式错误": 0,
            "标点错误": 0
        }}
    }}
}}"""
        
        system_message = """你是一个专业的文本纠错助手，擅长检查和纠正中文文本中的错误。
请仔细检查文本，找出所有可能的错误，并提供准确的纠正建议。"""
        
        result = self.call_api(prompt, system_message)
        
        if result:
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                return {"raw_response": result}
                
        return {}
    
    def optimize_formatting(self, document_data: Dict[str, Any], 
                           target_style: str = "公文") -> Dict[str, Any]:
        """
        优化文档格式
        
        Args:
            document_data: 文档数据
            target_style: 目标样式（公文、学术、商务等）
            
        Returns:
            优化建议
        """
        # 准备分析内容
        content_parts = []
        
        for para in document_data.get("paragraphs", [])[:30]:  # 限制前30段
            text = para.get("text", "").strip()
            if text:
                content_parts.append(f"[{para['index']}] {text}")
                
        content = "\n".join(content_parts)
        
        prompt = f"""请根据{target_style}格式要求，分析以下文档并提供格式优化建议。

文档内容：
{content}

请以JSON格式返回优化建议，格式为：
{{
    "target_style": "{target_style}",
    "current_issues": [
        {{
            "paragraph_index": 0,
            "issue": "问题描述",
            "suggestion": "优化建议"
        }}
    ],
    "formatting_plan": [
        {{
            "paragraph_index": 0,
            "current_format": "当前格式",
            "suggested_format": "建议格式",
            "reason": "原因"
        }}
    ],
    "overall_optimization": [
        "整体优化建议1",
        "整体优化建议2"
    ]
}}"""
        
        system_message = f"""你是一个专业的文档排版助手，擅长{target_style}格式的排版。
请根据{target_style}格式标准，提供详细的格式优化建议。

{target_style}格式标准：
- 纸张：A4 (210×297mm)
- 页边距：上3.7cm、下3.5cm、左2.8cm、右2.6cm
- 标题：方正小标宋简体 二号（22pt），居中，行距30磅
- 一级标题：黑体 三号（16pt）
- 二级标题：楷体 三号（16pt）
- 三级标题：仿宋 三号（16pt）加粗
- 四级标题：仿宋 三号（16pt）
- 正文：仿宋 三号（16pt），首行缩进2字符，行距28磅
- 落款：右空四字，阿拉伯数字日期
- 页码：宋体小四号（12pt），居中，-X-格式"""
        
        result = self.call_api(prompt, system_message)
        
        if result:
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                return {"raw_response": result}
                
        return {}
    
    def generate_content(self, topic: str, content_type: str = "公文",
                        length: str = "中等") -> Dict[str, Any]:
        """
        生成文档内容
        
        Args:
            topic: 主题
            content_type: 内容类型
            length: 内容长度（短、中等、长）
            
        Returns:
            生成的内容
        """
        prompt = f"""请根据以下要求生成{content_type}内容：

主题：{topic}
内容类型：{content_type}
长度：{length}

请以JSON格式返回生成的内容，格式为：
{{
    "title": "文档标题",
    "sections": [
        {{
            "heading": "章节标题",
            "content": "章节内容",
            "level": 1
        }}
    ],
    "full_content": "完整内容",
    "word_count": 0,
    "suggested_formatting": {{
        "title_style": "标题样式建议",
        "heading_styles": ["章节标题样式建议"],
        "body_style": "正文样式建议"
    }}
}}"""
        
        system_message = f"""你是一个专业的{content_type}写作助手，擅长撰写各类{content_type}文档。
请根据主题生成专业、规范的{content_type}内容。"""
        
        result = self.call_api(prompt, system_message)
        
        if result:
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                return {"raw_response": result}
                
        return {}
    
    def translate_formatting(self, source_format: str, target_format: str,
                            formatting_rules: Dict[str, Any]) -> Dict[str, Any]:
        """
        转换格式规则
        
        Args:
            source_format: 源格式
            target_format: 目标格式
            formatting_rules: 源格式规则
            
        Returns:
            目标格式规则
        """
        prompt = f"""请将以下{source_format}格式规则转换为{target_format}格式规则：

源格式规则：
{json.dumps(formatting_rules, ensure_ascii=False, indent=2)}

请以JSON格式返回转换后的规则，格式为：
{{
    "source_format": "{source_format}",
    "target_format": "{target_format}",
    "converted_rules": {{
        // 转换后的规则
    }},
    "conversion_notes": [
        "转换说明1",
        "转换说明2"
    ]
}}"""
        
        system_message = f"""你是一个专业的格式转换助手，擅长在不同文档格式标准之间进行转换。
请将{source_format}格式规则准确转换为{target_format}格式规则。"""
        
        result = self.call_api(prompt, system_message)
        
        if result:
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                return {"raw_response": result}
                
        return {}
    
    def batch_analyze(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量分析文档
        
        Args:
            documents: 文档数据列表
            
        Returns:
            分析结果列表
        """
        results = []
        
        for i, doc in enumerate(documents):
            print(f"分析文档 {i+1}/{len(documents)}...")
            analysis = self.analyze_structure(doc)
            results.append(analysis)
            
        return results
    
    def create_style_guide(self, document_type: str, 
                          examples: List[str]) -> Dict[str, Any]:
        """
        创建样式指南
        
        Args:
            document_type: 文档类型
            examples: 示例文本列表
            
        Returns:
            样式指南
        """
        examples_text = "\n\n".join([f"示例{i+1}:\n{example}" for i, example in enumerate(examples)])
        
        prompt = f"""请根据以下{document_type}示例，创建详细的样式指南：

{examples_text}

请以JSON格式返回样式指南，格式为：
{{
    "document_type": "{document_type}",
    "page_setup": {{
        "paper_size": "纸张大小",
        "margins": {{
            "top": "上边距",
            "bottom": "下边距",
            "left": "左边距",
            "right": "右边距"
        }}
    }},
    "font_styles": {{
        "title": {{
            "font_name": "字体",
            "font_size": "字号",
            "bold": true,
            "alignment": "对齐方式"
        }},
        "heading1": {{}},
        "heading2": {{}},
        "body": {{}}
    }},
    "paragraph_styles": {{
        "line_spacing": "行距",
        "first_line_indent": "首行缩进",
        "space_before": "段前间距",
        "space_after": "段后间距"
    }},
    "other_rules": [
        "其他规则1",
        "其他规则2"
    ]
}}"""
        
        system_message = f"""你是一个专业的文档排版助手，擅长创建{document_type}的样式指南。
请根据示例分析并创建详细的样式指南。"""
        
        result = self.call_api(prompt, system_message)
        
        if result:
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                return {"raw_response": result}
                
        return {}
    
    def apply_format_by_analysis(self, doc_manager, analysis_result: Dict[str, Any]) -> bool:
        """
        根据分析结果自动应用格式
        
        Args:
            doc_manager: 文档管理器
            analysis_result: 分析结果（来自analyze_structure）
            
        Returns:
            是否成功应用格式
        """
        try:
            from core.formatting import FormattingManager
            
            fm = FormattingManager(doc_manager.document)
            
            # 获取文档类型
            doc_type = analysis_result.get("document_type", "普通文档")
            
            # 根据文档类型设置页面格式
            if doc_type == "公文":
                fm.set_page_format(
                    page_width=21.0,
                    page_height=29.7,
                    left_margin=2.8,
                    right_margin=2.6,
                    top_margin=3.7,
                    bottom_margin=3.5
                )
            elif doc_type == "学术论文":
                fm.set_page_format(
                    page_width=21.0,
                    page_height=29.7,
                    left_margin=2.5,
                    right_margin=2.5,
                    top_margin=2.5,
                    bottom_margin=2.5
                )
            
            # 获取段落分析结果
            paragraphs_analysis = analysis_result.get("paragraphs", [])
            
            # 遍历段落并应用格式
            for para_info in paragraphs_analysis:
                index = para_info.get("index")
                para_type = para_info.get("type", "正文")
                suggestions = para_info.get("formatting_suggestions", {})
                
                # 获取对应段落
                if index is not None and index < len(doc_manager.document.paragraphs):
                    para = doc_manager.document.paragraphs[index]
                    
                    # 根据段落类型应用格式
                    font_name = suggestions.get("font_name", "仿宋")
                    font_size = suggestions.get("font_size", 16)
                    alignment = suggestions.get("alignment", "justify")
                    line_spacing = suggestions.get("line_spacing", 28)
                    first_line_indent = suggestions.get("first_line_indent", 2)
                    
                    # 设置段落格式
                    fm.set_paragraph_format(
                        para,
                        alignment=alignment,
                        first_line_indent_chars=first_line_indent,
                        line_spacing=line_spacing,
                        line_spacing_rule='exact',
                        space_before=0,
                        space_after=0
                    )
                    
                    # 设置字体
                    for run in para.runs:
                        fm.set_font(
                            run,
                            font_name=font_name,
                            font_size=font_size
                        )
            
            return True
            
        except Exception as e:
            print(f"应用格式失败: {e}")
            return False
    
    def analyze_and_apply_format(self, doc_manager, target_style: str = "公文") -> bool:
        """
        分析文档并自动应用格式
        
        Args:
            doc_manager: 文档管理器
            target_style: 目标样式（公文、学术、商务等）
            
        Returns:
            是否成功
        """
        try:
            # 获取文档数据
            doc_data = {
                "paragraphs": []
            }
            
            for i, para in enumerate(doc_manager.document.paragraphs):
                doc_data["paragraphs"].append({
                    "index": i,
                    "text": para.text
                })
            
            # 分析文档结构
            analysis = self.analyze_structure(doc_data)
            
            if not analysis:
                return False
            
            # 应用格式
            return self.apply_format_by_analysis(doc_manager, analysis)
            
        except Exception as e:
            print(f"分析并应用格式失败: {e}")
            return False