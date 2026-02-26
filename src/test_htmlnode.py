import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(tag="p", value="This is a paragraph node", props={"style" : "text-align:right"})
        node2 = HTMLNode(tag="p", value="This is a paragraph node", props={"style" : "text-align:right"})
        self.assertEqual(node1, node2)
    
    def test_not_eq(self):
        node1 = HTMLNode(tag="p", value="This is a paragraph node", props={"style" : "text-align:right"})
        node2 = HTMLNode(tag="p", value="This is a different paragraph node", props={"style" : "text-align:right"})
        self.assertNotEqual(node1, node2)
        
    def test_eq_defaults(self):
        node1 = HTMLNode(tag=None, value=None, children=None, props=None)
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_props_to_html(self):
        node =  HTMLNode(tag= "p", value="This is a paragraph node", props={"style" : "text-align:right"})
        expected_html_prop = ' style= "text-align:right"'
        self.assertEqual(node.props_to_html(), expected_html_prop)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is a node without tags", None)
        self.assertEqual(node.to_html(), "This is a node without tags")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a node with p tags", None)
        self.assertEqual(node.to_html(), "<p>This is a node with p tags</p>")

    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "This is a node with p tags and props", {"style" : "text-align:right"})
        self.assertEqual(node.to_html(), '<p style= "text-align:right">This is a node with p tags and props</p>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_no_tag(self):
        parent_node = ParentNode(None, [])
        with self.assertRaises(ValueError) as err:
             parent_node.to_html()
        self.assertEqual(str(err.exception), "Parent node must have a tag value")

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError) as err:
             parent_node.to_html()
        self.assertEqual(str(err.exception), "Parent node must have children")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode(None, "child1")
        child_node2 = LeafNode("i", "child2")
        child_node3 = LeafNode("b", "child3")
        child_node4 = LeafNode("span", "child4")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(parent_node.to_html(), "<div>child1<i>child2</i><b>child3</b><span>child4</span></div>")
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_multiple_grandchildren(self):
        grandchild_node1 = LeafNode(None, "grandchild1")
        grandchild_node2 = LeafNode("i", "grandchild2")
        grandchild_node3 = LeafNode("b", "grandchild3")
        grandchild_node4 = LeafNode("span", "grandchild4")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3, grandchild_node4])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>grandchild1<i>grandchild2</i><b>grandchild3</b><span>grandchild4</span></span></div>")

if __name__ == "__main__":
    unittest.main()
