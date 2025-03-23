from textnode import TextNode , TextType

def main():
    a = TextNode("This is some anchor text" , TextType.BOLD)
    b = TextNode("This is some anchor text" , TextType.BOLD)
    print(a)
    
main()