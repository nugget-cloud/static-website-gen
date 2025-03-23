import unittest
from htmlnode import HtmlNode , LeafNode , ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_multiple_attributes(self):
        node = HtmlNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HtmlNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_attribute(self):
        node = HtmlNode(tag="img", props={"src": "image.png"})
        self.assertEqual(node.props_to_html(), ' src="image.png"')

    def test_default_values(self):
        node = HtmlNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_repr(self):
        node = HtmlNode(tag="div", value="Hello", children=[], props={"class": "container"})
        expected_repr = "HtmlNode(tag=div, value=Hello, children=[], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html_not_implemented(self):
        node = HtmlNode(tag="p", value="Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

class TestLeafNode(unittest.TestCase):
    def test_leafNode(self):
        node= LeafNode(value="Hello" , tag="p" , props=None)
        expected = "<p>Hello</p>"
        self.assertEqual(node.to_html() , expected)
        
        
class TestParentNode(unittest.TestCase):
    def test_parentNode(self):
        node = ParentNode("p" , 
        [
            LeafNode("Bold text", "b"),
            LeafNode("Normal text"),
            LeafNode("italic text", "i"),
            LeafNode("Normal text"),
        ])
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html() , expected)
if __name__ == "__main__":
    unittest.main()
