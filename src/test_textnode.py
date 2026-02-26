import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_eq_defaults(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node1, node2)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.to_html_leaf()
        self.assertEqual(html_node.tag , None)
        self.assertEqual(html_node.value , "This is a text node")
        self.assertEqual(html_node.props, None)

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = node.to_html_leaf()
        self.assertEqual(html_node.tag , "b")
        self.assertEqual(html_node.value , "This is a bold node")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = node.to_html_leaf()
        self.assertEqual(html_node.tag , "i")
        self.assertEqual(html_node.value , "This is a italic node")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = node.to_html_leaf()
        self.assertEqual(html_node.tag , "code")
        self.assertEqual(html_node.value , "This is a code node")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://www.testsite.com")
        html_node = node.to_html_leaf()
        self.assertEqual(html_node.tag , "a")
        self.assertEqual(html_node.value , "This is a link node")
        self.assertEqual(html_node.props, {"href": "http://www.testsite.com"})
        self.assertEqual(html_node.to_html(), '<a href= "http://www.testsite.com">This is a link node</a>')

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "./testimage.png")
        html_node = node.to_html_leaf()
        self.assertEqual(html_node.tag , "img")
        self.assertEqual(html_node.value , "")
        self.assertEqual(html_node.props, {"src": "./testimage.png", "alt": "This is a image node"})
        self.assertEqual(html_node.to_html(), '<img src= "./testimage.png" alt= "This is a image node"></img>')


if __name__ == "__main__":
    unittest.main()
