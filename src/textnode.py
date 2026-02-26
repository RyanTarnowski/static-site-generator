from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def to_html_leaf(self):
        tag = None
        value = None
        props = None

        match self.text_type:
            case TextType.TEXT:
                value = self.text
            case TextType.BOLD:
                tag = "b"
                value = self.text
            case TextType.ITALIC:
                tag = "i"
                value = self.text
            case TextType.CODE:
                tag = "code"
                value = self.text
            case TextType.LINK:
                tag = "a"
                value = self.text
                props = {"href": self.url}
            case TextType.IMAGE:
                tag = "img"
                value = ""
                props = {"src": self.url, "alt": self.text}
            case _:
                raise TypeError("Text type not recognized")

        return LeafNode(tag=tag, value=value, props=props)
