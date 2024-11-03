from enum import Enum

class TextType(Enum):
    NORMAL = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "links"
    IMAGE = "images"

class TextNode:
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.url == other.url and self.text_type == other.text_type

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"