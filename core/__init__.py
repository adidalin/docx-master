# docx-master核心模块

from .document import DocumentManager
from .formatting import FormattingManager
from .styles import StyleManager
from .ai_integration import AIIntegration
from .utils import Utils
from .validation import DocumentValidator
from .toc import TableOfContents
from .placeholder import PlaceholderFiller

__version__ = "1.0.0"
__author__ = "OpenCode"

__all__ = [
    "DocumentManager",
    "FormattingManager", 
    "StyleManager",
    "AIIntegration",
    "Utils",
    "DocumentValidator",
    "TableOfContents",
    "PlaceholderFiller"
]