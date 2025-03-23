class HtmlNode():
    def __init__(self , tag=None , value=None , children=None , props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def __repr__(self):
        return f"HtmlNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        attributes = []
        for key , value in self.props.items():
            attributes.append(f'{key}="{value}"')
        return " " + " ".join(attributes)
    
class LeafNode(HtmlNode):
    def __init__(self , value ,  tag=None , props=None):
        super().__init__(tag=tag , value=value , props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag ==None:
            return f'{self.value}'
        elif self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
        
class ParentNode(HtmlNode):
    def __init__(self , tag , children , props=None):
        super().__init__(tag=tag , children=children , props=props)
        
    def to_html(self):

        
        children_html = "".join(child.to_html() for child in self.children)
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
        
        