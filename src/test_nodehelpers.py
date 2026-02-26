import unittest

from textnode import TextNode, TextType
from nodehelpers import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_links, text_to_textnodes 

class TextNodeHelpers(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **Bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ])

    def test_bold_bold(self):
        node = TextNode("This is text with a **Bold block** and another **Bold block!**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Bold block", TextType.BOLD),
                TextNode(" and another ", TextType.TEXT),
                TextNode("Bold block!", TextType.BOLD),
            ])

    def test_bold_code(self):
        node1 = TextNode("This is text with a **Bold block** word", TextType.TEXT)
        node2 = TextNode("This is text with a **Bold block2** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Bold block2", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ])
    
    def test_non_test(self):
        node = TextNode("This is bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is bold text", TextType.BOLD),])

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT, )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
           [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    
    def test_split_images_no_leading_text(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT, )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
           [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_text(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT, )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
           [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("This is a text node without images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
           [
                TextNode("This is a text node without images", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_multi_nodes(self):
        node1 = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT, )
        node2 = TextNode("This is the second node. ![node2image](https://a.realURL.com.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
           [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This is the second node. ", TextType.TEXT),
                TextNode("node2image", TextType.IMAGE, "https://a.realURL.com.png"),
            ],
            new_nodes,
        )
        
    def test_split_links(self):
        node = TextNode("This is text with an [TestURL1](https://TestURL1.com) and another [TestURL2](https://TestURL2.com)", TextType.TEXT, )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
           [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("TestURL1", TextType.LINK, "https://TestURL1.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("TestURL2", TextType.LINK, "https://TestURL2.com"),
            ],
            new_nodes,
        )
        
    def test_split_links_no_leading_text(self):
        node = TextNode("[TestURL1](https://TestURL1.com) and another [TestURL2](https://TestURL2.com)", TextType.TEXT, )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
           [
                TextNode("TestURL1", TextType.LINK, "https://TestURL1.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("TestURL2", TextType.LINK, "https://TestURL2.com"),
            ],
            new_nodes,
        )

    def test_split_links_no_text(self):
        node = TextNode("[TestURL1](https://TestURL1.com)[TestURL2](https://TestURL2.com)", TextType.TEXT, )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
           [
                TextNode("TestURL1", TextType.LINK, "https://TestURL1.com"),
                TextNode("TestURL2", TextType.LINK, "https://TestURL2.com"),
            ],
            new_nodes,
        )
        
    def test_split_links_no_links(self):
        node = TextNode("This is just text without links!", TextType.TEXT, )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
           [
                TextNode("This is just text without links!", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_multi_nodes(self):
        node1 = TextNode("This is text with an [TestURL1](https://TestURL1.com) and another [TestURL2](https://TestURL2.com)", TextType.TEXT, )
        node2 = TextNode("This is the second node [TestURL3](https://TestURL3.com)", TextType.TEXT, )
        new_nodes = split_nodes_links([node1, node2])
        self.assertListEqual(
           [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("TestURL1", TextType.LINK, "https://TestURL1.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("TestURL2", TextType.LINK, "https://TestURL2.com"),
                TextNode("This is the second node ", TextType.TEXT),
                TextNode("TestURL3", TextType.LINK, "https://TestURL3.com"),
            ],
            new_nodes,
        )
 
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
                ],
            new_nodes,
        )


