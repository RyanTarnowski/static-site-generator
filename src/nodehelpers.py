import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid Markdown syntax")

        sections = node.text.split(delimiter)
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

    return split_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    split_nodes = []

    for node in old_nodes:
        if node.text == "":
            continue

        images = extract_markdown_images(node.text)

        if len(images) == 0:
            split_nodes.append(node)
            continue
        
        node_text = node.text       
        
        for alt_text, image_link in images:
            image_markdown = f"![{alt_text}]({image_link})"
            sections = node_text.split(image_markdown,1)

            if len(sections) != 2:
               raise ValueError("Invalid markdown, image not closed")

            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))

            split_nodes.append(TextNode(alt_text, TextType.IMAGE, image_link))
            node_text = sections[1]

    return split_nodes

def split_nodes_links(old_nodes):
    split_nodes = []

    for node in old_nodes:
        if node.text == "":
            continue

        links = extract_markdown_links(node.text)

        if len(links) == 0:
            split_nodes.append(node)
            continue
        
        node_text = node.text       
        
        for text, href in links:
            link_markdown = f"[{text}]({href})"
            sections = node_text.split(link_markdown,1)

            if len(sections) != 2:
                raise ValueError("Invalid markdown, link not closed")

            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))

            split_nodes.append(TextNode(text, TextType.LINK, href))
            node_text = sections[1]

    return split_nodes

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE) 
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes


