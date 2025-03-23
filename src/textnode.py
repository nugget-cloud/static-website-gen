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
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode(value=text_node.text, tag="b")

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(value=text_node.text, tag="i")

    elif text_node.text_type == TextType.CODE:
        return LeafNode(value=text_node.text, tag="code")

    elif text_node.text_type == TextType.LINK:
        return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})

    else:
        raise ValueError("Unsupported TextType")
    
def split_code_delimiter(old_nodes , delimiter , text_type):
    new_nodes = []
    for node in old_nodes:
        new_nodes = node.split(delimiter)
    
        
        
