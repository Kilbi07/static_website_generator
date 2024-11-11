import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("Hello, World", TextType.NORMAL)
        description = str(node)
        description_1 = f"TextNode({node.text}, {node.text_type}, {node.url})"
        self.assertEqual(description,description_1)
    def test_no_eq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)
if __name__ == "__main__":
    unittest.main()