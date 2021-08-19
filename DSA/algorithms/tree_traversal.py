from typing import List

from data_structures.binary_search_tree import Node


def inorder(node: Node, nodes: List[Node]) -> None:
    """Inorder traversal.

    1. Traverse left
    2. Visit root
    3. Traverse right

    In a BST, gives nodes in ascending order.

           5
        /    \
       3      8
      / \    / \
     1   4  7  10

    1, 3, 4, 5, 7, 8, 10
    """

    if not node:
        return

    inorder(node.left, nodes)
    nodes.append(node.val)
    inorder(node.right, nodes)


def preorder(node: Node, nodes: List[Node]) -> None:
    """Preorder traversal.

    1. Visit root
    2. Traverse left
    3. Traverse right

    Can be used to create a copy of the tree.

           5
        /    \
       3      8
      / \    / \
     1   4  7  10

    5, 3, 1, 4, 8, 7, 10
    """

    if not node:
        return

    nodes.append(node.val)
    preorder(node.left, nodes)
    preorder(node.right, nodes)


def postorder(node: Node, nodes: List[Node]) -> None:
    """Preorder traversal.

    1. Traverse left
    2. Traverse right
    3. Visit root

    Can be used to delete the tree.

           5
        /    \
       3      8
      / \    / \
     1   4  7  10

    1, 4, 3, 7, 10, 8, 5
    """

    if not node:
        return

    postorder(node.left, nodes)
    postorder(node.right, nodes)
    nodes.append(node.val)
