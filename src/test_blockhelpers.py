import unittest
from blockhelpers import markdown_to_blocks, block_to_block_type, get_title, BlockType

class BlockHelpers(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            )
    
    def test_markdown_to_blocks_empty(self):
        md = """
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
            )

    def test_markdown_to_blocks_exta_blocks(self):
        md = """
       This is block one





This is block two
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is block one",
                "This is block two",
             ]
            )
    
    def test_block_to_block_type_paragraph(self):
        block = "This is a standard paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_heading_1(self):
        block = "# This is a standard paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading_2(self):
        block = "## This is a standard paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading_3(self):
        block = "### This is a standard paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading_4(self):
        block = "#### This is a standard paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading_5(self):
        block = "##### This is a standard paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading_6(self):
        block = "###### This is a standard paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_quotes(self):
        block = """> This is a quote block
> This is another quote block
> And one more"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = """- list item 1
- list item 2
- list item 3"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = """1. list item 1
2. list item 2
3. list item 3"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_code(self):
        block = """```
This is a code block
this is more code...
```
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_get_title(self):
        block = """# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts
"""
        title = get_title(block)
        self.assertEqual(title, "Tolkien Fan Club")


    def test_get_title_empty(self):
        block = """## Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts
"""
        # title = get_title(block)
        with self.assertRaises(TypeError):
            title = get_title(block)

