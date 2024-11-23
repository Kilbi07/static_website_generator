import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_no_eq(self):
        node = LeafNode("a", "Click me!",props={"href": "https://www.google.com"})
        node2 = LeafNode("div")
        self.assertNotEqual(node,node2)
    def test_to_html(self):
        node = LeafNode("a", "Click Me!",props={"href": "https://www.google.com"})
        description = node.to_html()
        props_string = node.props_to_html()
        description_1 = f"<{node.tag}{props_string}>{node.value}</{node.tag}>" 
        self.assertEqual(description,description_1)
        
if __name__ == "__main__":
    unittest.main()