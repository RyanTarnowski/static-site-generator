from blockhelpers import markdown_to_blocks, block_to_block_type, strip_block_type, get_heading_size, BlockType
from htmlnode import LeafNode, ParentNode
from nodehelpers import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        match block_type:
            case BlockType.HEADING:
                text_node = text_to_textnodes(strip_block_type(block, BlockType.HEADING))
                header_value = ""

                for node in text_node:
                    header_value += node.to_html_leaf().to_html()

                child_nodes.append(
                    LeafNode(f"h{get_heading_size(block)}", header_value)
                )
            case BlockType.QUOTE:
                child_nodes.append(
                    LeafNode("blockquote", strip_block_type(block, BlockType.QUOTE))
                )
            case BlockType.PARAGRAPH:
                text_node = text_to_textnodes(block)
                para_value = ""

                for node in text_node:
                    para_value += node.to_html_leaf().to_html()
               
                para_value = para_value.replace("\n", " ")
                child_nodes.append(
                    LeafNode("p", para_value)
                )
            case BlockType.CODE:
                child_nodes.append(
                    ParentNode(
                      "pre", [LeafNode("code", strip_block_type(block, BlockType.CODE))]
                    )
                )
            case BlockType.UNORDERED_LIST:
                list_nodes = []

                for node in block.split("\n"):
                    text_node = text_to_textnodes(strip_block_type(node, BlockType.UNORDERED_LIST))
                
                    list_value = ""
                    for node in text_node:
                        list_value += node.to_html_leaf().to_html()

                    list_nodes.append(
                        LeafNode("li", list_value) 
                    )

                child_nodes.append(
                    ParentNode(
                        "ul", list_nodes
                    )
                )
            case BlockType.ORDERED_LIST:
                list_nodes = []

                for node in block.split("\n"):
                    text_node = text_to_textnodes(strip_block_type(node, BlockType.ORDERED_LIST))
                
                    list_value = ""
                    for node in text_node:
                        list_value += node.to_html_leaf().to_html()

                    list_nodes.append(
                        LeafNode("li", list_value) 
                    )

                child_nodes.append(
                    ParentNode(
                        "ol", list_nodes
                    )
                )

            case _:
                raise TypeError("Block type not recongnized")

    return ParentNode("div", child_nodes)        





