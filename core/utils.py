"""
工具模块
提供各种工具函数
"""

import os
import re
import json
import shutil
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
from datetime import datetime


class Utils:
    """工具类，提供各种实用函数"""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        清洗文本
        
        Args:
            text: 原始文本
            
        Returns:
            清洗后的文本
        """
        if not text:
            return text
            
        # 删除Markdown符号
        text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)  # 标题
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # 加粗
        text = re.sub(r'^\s*>\s*', '', text, flags=re.MULTILINE)  # 引用
        
        # 去除多余空格
        text = re.sub(r' +', ' ', text)
        text = re.sub(r'[\u3000\u00a0\u200b\u200c\u200d\ufeff\t]', '', text)
        
        # 去除中文之间的空格
        text = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', text)
        
        # 处理非自然回车（保留段落间的回车）
        text = re.sub(r'([^\n])\n([^\n])', r'\1\2', text)
        
        return text.strip()
    
    @staticmethod
    def extract_paragraph_info(paragraph) -> Dict[str, Any]:
        """
        提取段落信息
        
        Args:
            paragraph: Paragraph对象
            
        Returns:
            段落信息字典
        """
        info = {
            "text": paragraph.text,
            "style": paragraph.style.name if paragraph.style else "Normal",
            "alignment": str(paragraph.alignment) if paragraph.alignment else None,
            "runs": []
        }
        
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
    
    @staticmethod
    def calculate_text_width(text: str, font_size: int) -> float:
        """
        计算文本宽度（近似值）
        
        Args:
            text: 文本内容
            font_size: 字体大小（磅）
            
        Returns:
            文本宽度（厘米）
        """
        # 简单估算：中文字符宽度约为字体大小，英文字符宽度约为字体大小的一半
        width = 0
        for char in text:
            if ord(char) > 127:  # 中文字符
                width += font_size
            else:  # 英文字符
                width += font_size * 0.6
                
        # 转换为厘米（1磅 ≈ 0.0353厘米）
        return width * 0.0353
    
    @staticmethod
    def format_file_size(size_bytes: int) -> str:
        """
        格式化文件大小
        
        Args:
            size_bytes: 文件大小（字节）
            
        Returns:
            格式化后的文件大小
        """
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"
    
    @staticmethod
    def get_file_info(file_path: str) -> Dict[str, Any]:
        """
        获取文件信息
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件信息字典
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
            
        stat = os.stat(file_path)
        
        return {
            "file_path": file_path,
            "file_name": os.path.basename(file_path),
            "file_size": stat.st_size,
            "file_size_formatted": Utils.format_file_size(stat.st_size),
            "created_time": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "modified_time": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "accessed_time": datetime.fromtimestamp(stat.st_atime).isoformat(),
            "is_file": os.path.isfile(file_path),
            "is_dir": os.path.isdir(file_path),
            "extension": os.path.splitext(file_path)[1].lower()
        }
    
    @staticmethod
    def ensure_directory(directory_path: str) -> bool:
        """
        确保目录存在
        
        Args:
            directory_path: 目录路径
            
        Returns:
            是否成功
        """
        try:
            os.makedirs(directory_path, exist_ok=True)
            return True
        except Exception as e:
            print(f"创建目录失败: {e}")
            return False
    
    @staticmethod
    def backup_file(file_path: str, backup_suffix: str = ".bak") -> Optional[str]:
        """
        备份文件
        
        Args:
            file_path: 文件路径
            backup_suffix: 备份后缀
            
        Returns:
            备份文件路径
        """
        if not os.path.exists(file_path):
            return None
            
        backup_path = file_path + backup_suffix
        
        try:
            shutil.copy2(file_path, backup_path)
            return backup_path
        except Exception as e:
            print(f"备份文件失败: {e}")
            return None
    
    @staticmethod
    def load_json(file_path: str) -> Optional[Any]:
        """
        加载JSON文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            JSON数据
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"加载JSON文件失败: {e}")
            return None
    
    @staticmethod
    def save_json(data: Any, file_path: str, indent: int = 2) -> bool:
        """
        保存JSON文件
        
        Args:
            data: 数据
            file_path: 文件路径
            indent: 缩进空格数
            
        Returns:
            是否成功
        """
        try:
            # 确保目录存在
            directory = os.path.dirname(file_path)
            if directory:
                Utils.ensure_directory(directory)
                
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
            return True
        except Exception as e:
            print(f"保存JSON文件失败: {e}")
            return False
    
    @staticmethod
    def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
        """
        合并字典
        
        Args:
            dict1: 字典1
            dict2: 字典2
            
        Returns:
            合并后的字典
        """
        result = dict1.copy()
        
        for key, value in dict2.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = Utils.merge_dicts(result[key], value)
            else:
                result[key] = value
                
        return result
    
    @staticmethod
    def flatten_dict(d: Dict, parent_key: str = '', sep: str = '.') -> Dict:
        """
        展平字典
        
        Args:
            d: 字典
            parent_key: 父键
            sep: 分隔符
            
        Returns:
            展平后的字典
        """
        items = []
        
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            
            if isinstance(v, dict):
                items.extend(Utils.flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
                
        return dict(items)
    
    @staticmethod
    def unflatten_dict(d: Dict, sep: str = '.') -> Dict:
        """
        反展平字典
        
        Args:
            d: 字典
            sep: 分隔符
            
        Returns:
            反展平后的字典
        """
        result = {}
        
        for key, value in d.items():
            keys = key.split(sep)
            current = result
            
            for k in keys[:-1]:
                if k not in current:
                    current[k] = {}
                current = current[k]
                
            current[keys[-1]] = value
            
        return result
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        验证邮箱格式
        
        Args:
            email: 邮箱地址
            
        Returns:
            是否有效
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        验证手机号格式
        
        Args:
            phone: 手机号
            
        Returns:
            是否有效
        """
        pattern = r'^1[3-9]\d{9}$'
        return bool(re.match(pattern, phone))
    
    @staticmethod
    def validate_id_card(id_card: str) -> bool:
        """
        验证身份证号格式
        
        Args:
            id_card: 身份证号
            
        Returns:
            是否有效
        """
        pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$'
        return bool(re.match(pattern, id_card))
    
    @staticmethod
    def generate_id(prefix: str = "", length: int = 8) -> str:
        """
        生成ID
        
        Args:
            prefix: 前缀
            length: 长度
            
        Returns:
            ID字符串
        """
        import random
        import string
        
        chars = string.ascii_letters + string.digits
        random_part = ''.join(random.choice(chars) for _ in range(length))
        
        return f"{prefix}{random_part}" if prefix else random_part
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
        """
        截断文本
        
        Args:
            text: 文本
            max_length: 最大长度
            suffix: 后缀
            
        Returns:
            截断后的文本
        """
        if len(text) <= max_length:
            return text
            
        return text[:max_length - len(suffix)] + suffix
    
    @staticmethod
    def remove_duplicates(lst: List) -> List:
        """
        去除列表重复项（保持顺序）
        
        Args:
            lst: 列表
            
        Returns:
            去重后的列表
        """
        seen = set()
        result = []
        
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
                
        return result
    
    @staticmethod
    def chunk_list(lst: List, chunk_size: int) -> List[List]:
        """
        分块列表
        
        Args:
            lst: 列表
            chunk_size: 块大小
            
        Returns:
            分块后的列表
        """
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    
    @staticmethod
    def flatten_list(lst: List) -> List:
        """
        展平列表
        
        Args:
            lst: 列表
            
        Returns:
            展平后的列表
        """
        result = []
        
        for item in lst:
            if isinstance(item, list):
                result.extend(Utils.flatten_list(item))
            else:
                result.append(item)
                
        return result
    
    @staticmethod
    def deep_get(obj: Any, path: str, default: Any = None) -> Any:
        """
        深度获取对象属性
        
        Args:
            obj: 对象
            path: 路径（如 "a.b.c"）
            default: 默认值
            
        Returns:
            属性值
        """
        keys = path.split('.')
        current = obj
        
        for key in keys:
            if isinstance(current, dict):
                if key in current:
                    current = current[key]
                else:
                    return default
            elif hasattr(current, key):
                current = getattr(current, key)
            else:
                return default
                
        return current
    
    @staticmethod
    def deep_set(obj: Any, path: str, value: Any) -> None:
        """
        深度设置对象属性
        
        Args:
            obj: 对象
            path: 路径（如 "a.b.c"）
            value: 值
        """
        keys = path.split('.')
        current = obj
        
        for key in keys[:-1]:
            if isinstance(current, dict):
                if key not in current:
                    current[key] = {}
                current = current[key]
            elif hasattr(current, key):
                current = getattr(current, key)
            else:
                return
                
        if isinstance(current, dict):
            current[keys[-1]] = value
        elif hasattr(current, keys[-1]):
            setattr(current, keys[-1], value)
    
    @staticmethod
    def safe_eval(expression: str, variables: Dict[str, Any] = None) -> Any:
        """
        安全计算表达式
        
        Args:
            expression: 表达式
            variables: 变量字典
            
        Returns:
            计算结果
        """
        import ast
        
        try:
            # 解析表达式
            tree = ast.parse(expression, mode='eval')
            
            # 检查是否包含危险操作
            for node in ast.walk(tree):
                if isinstance(node, (ast.Attribute, ast.Call, ast.Import, ast.ImportFrom)):
                    raise ValueError("不支持的表达式")
                    
            # 计算表达式
            if variables:
                return eval(compile(tree, '<string>', 'eval'), {"__builtins__": {}}, variables)
            else:
                return eval(compile(tree, '<string>', 'eval'), {"__builtins__": {}})
                
        except Exception as e:
            print(f"计算表达式失败: {e}")
            return None
    
    @staticmethod
    def retry(func, max_attempts: int = 3, delay: float = 1.0, *args, **kwargs) -> Any:
        """
        重试函数
        
        Args:
            func: 函数
            max_attempts: 最大尝试次数
            delay: 延迟时间（秒）
            *args: 函数参数
            **kwargs: 函数关键字参数
            
        Returns:
            函数结果
        """
        import time
        
        last_exception = None
        
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                if attempt < max_attempts - 1:
                    time.sleep(delay)
                    
        raise last_exception