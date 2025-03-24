from textnode import TextNode, TextType
import re

pattern_markdown_images_alt = re.compile(r"!\[[^\]]*\]", re.IGNORECASE)
pattern_markdown_images_url = re.compile(r"\([^)]*\)" , re.IGNORECASE)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) %2 == 0:
            raise ValueError("there is some error ")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i] , TextType.TEXT))
            
            else:
                new_nodes.append(TextNode(sections[i] , text_type))
    return new_nodes
        
def extract_markdown_images(text):
    pattern = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")
    matches = re.findall(pattern, text)
    print(matches)
    return matches


def extract_markdown_links(text):
    pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
    matches = re.findall(pattern, text)
    print(matches)
    return matches
