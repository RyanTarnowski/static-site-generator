import unittest
from htmlhelpers import markdown_to_html_node
from htmlnode import LeafNode, ParentNode 

class TestHtmlHelpers(unittest.TestCase):
    def test_markdown_to_html_quote(self):
        md = """
> This is a quote block
> This is another quote block
> And one more
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node.to_html())
        self.assertEqual(
        html,
        """<div><blockquote>This is a quote block
This is another quote block
And one more</blockquote></div>""",
    )

    def test_markdown_to_html_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node.to_html())
        self.assertEqual(
            html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_markdown_to_html_heading1(self):
        md = "# Heading 1 **With some bold text**"

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node.to_html())
        self.assertEqual(
            html,
            "<div><h1>Heading 1 <b>With some bold text</b></h1></div>",
        )

    def test_markdown_to_html_heading2(self):
        md = "## Heading 2"

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(node.to_html())
        self.assertEqual(
            html,
        "<div><h2>Heading 2</h2></div>",
        )

    def test_markdown_to_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_markdown_to_unordered_list(self):
        md = """
- List item 1 **Bold!**
- List item 2
- List item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
        "<div><ul><li>List item 1 <b>Bold!</b></li><li>List item 2</li><li>List item 3</li></ul></div>",
        )

    def test_markdown_to_ordered_list(self):
        md = """
1. List item 1 **Bold!**
2. List item 2
3. List item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
        "<div><ol><li>List item 1 <b>Bold!</b></li><li>List item 2</li><li>List item 3</li></ol></div>",
        )
