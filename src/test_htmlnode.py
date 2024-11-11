import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "Hello World")
        description = str(node)
        description_1 = f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})"
        self.assertEqual(description,description_1)
    def test_no_eq(self):
        node = HTMLNode("a", "Click me!",props={"href": "https://www.google.com"})
        node2 = HTMLNode("div")
        self.assertNotEqual(node,node2)
    def test_props_to_html(self):
        node = HTMLNode("a", "Click me!",props={"href": "https://www.google.com"})
        description = node.props_to_html()
        description_1 = ""
        for k,v in node.props.items():
            description_1 += f' {k}="{v}"'
        self.assertEqual(description,description_1)
        
if __name__ == "__main__":
    unittest.main()