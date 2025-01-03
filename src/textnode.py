from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text: str,text_type: TextType,url: str = None):
        if isinstance(text_type, str):
            text_type = TextType(text_type)
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.url == other.url and self.text_type == other.text_type

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
