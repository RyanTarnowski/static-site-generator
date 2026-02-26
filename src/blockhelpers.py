import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.strip().split("\n\n")
    blocks = [block.strip("\n") for block in blocks]
    return [block for block in blocks if block != '']

def block_to_block_type(block):
    lines = block.splitlines()
    type_matches: dict[BlockType, int] = {
        BlockType.CODE: 0,
        BlockType.HEADING: 0,
        BlockType.ORDERED_LIST: 0,
        BlockType.PARAGRAPH: 0,
        BlockType.UNORDERED_LIST: 0,
        BlockType.QUOTE: 0
    }
    ordered_list_count = 1
    for line in lines:
        if re.match(r"^(#)\1{0,5} ", line):
            type_matches[BlockType.HEADING] += 1 
        if re.match(r"^(> )", line):
            type_matches[BlockType.QUOTE] += 1
        if re.match(r"^(- )", line):
            type_matches[BlockType.UNORDERED_LIST] += 1
        if re.match(f"^({ordered_list_count}. )", line):
            type_matches[BlockType.ORDERED_LIST] += 1
            ordered_list_count += 1
        if re.match(r"^(```)", line):
            if re.match(r"^(```)", lines[-1]):
                return BlockType.CODE

    matching_type = [key for key, value in type_matches.items() if value == len(lines)]
    # print(type_matches)
    if len(matching_type) == 1:
        # print(matching_type[0])
        return matching_type[0]

    # print(BlockType.PARAGRAPH)
    return BlockType.PARAGRAPH

def strip_block_type(block, block_type):
    match block_type:
        case BlockType.QUOTE:
            return re.sub(r"(> )", "", block)
        case BlockType.HEADING:
            return re.sub(r"(#)\1{0,5} ", "", block)
        case BlockType.CODE:
            return re.sub("^(```\n)|(```)$", "", block)
        case BlockType.UNORDERED_LIST:
            return re.sub(r"(- )", "", block)
        case BlockType.ORDERED_LIST:
            # TODO: Figure out the regex for the order list 
            return re.sub("() ", "", block)
        case _:
            raise TypeError("Block type not recongnized")

def get_heading_size(block):
    matches = re.search(r"^(#)\1{0,5}", block)
    if matches:
        return len(matches[0])
    else:
        raise TypeError("Was not able to determine heading size")
