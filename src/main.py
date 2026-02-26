from textnode import TextNode, TextType

def main():
    test_textnode = TextNode("this is some  anchor test", TextType.LINK, "http://www.boot.dev")
    print(test_textnode)

if __name__ == "__main__":
    main()

