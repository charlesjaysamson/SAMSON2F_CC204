r"""Part C (Assessment 3.6): DFS Methods in Tree.

Tree (from Assessment 3.5):

                 C
              /     \
            H         A
           / \       / \
          R   L     E   S
         / \ / \   / \
        S  A M  S  O  N

DFS methods: Preorder, Inorder, Postorder.
"""
from common import show


class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def build_tree():
    root = TreeNode("C")
    root.left = TreeNode("H")
    root.right = TreeNode("A")

    root.left.left = TreeNode("R")
    root.left.right = TreeNode("L")
    root.right.left = TreeNode("E")
    root.right.right = TreeNode("S")

    root.left.left.left = TreeNode("S")
    root.left.left.right = TreeNode("A")
    root.left.right.left = TreeNode("M")
    root.left.right.right = TreeNode("S")
    root.right.left.left = TreeNode("O")
    root.right.left.right = TreeNode("N")
    return root


def _record(node, result):
    result.append(node.label)
    print(f"  Step {len(result):>2}: visit {node.label}")


def preorder(node, result):
    """Root -> Left -> Right"""
    if node is None:
        return
    _record(node, result)
    preorder(node.left, result)
    preorder(node.right, result)


def inorder(node, result):
    """Left -> Root -> Right"""
    if node is None:
        return
    inorder(node.left, result)
    _record(node, result)
    inorder(node.right, result)


def postorder(node, result):
    """Left -> Right -> Root"""
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    _record(node, result)


def run():
    print("\nPART C: DFS METHODS IN TREE\n")
    print("                 C")
    print("              /     \\")
    print("            H         A")
    print("           / \\       / \\")
    print("          R   L     E   S")
    print("         / \\ / \\   / \\")
    print("        S  A M  S  O  N\n")

    root = build_tree()
    results = {}
    for title, method in (("Preorder (Root -> Left -> Right)", preorder),
                          ("Inorder (Left -> Root -> Right)", inorder),
                          ("Postorder (Left -> Right -> Root)", postorder)):
        print(title)
        out = []
        method(root, out)
        results[title.split()[0]] = out
        print()

    print("RESULT")
    for key, out in results.items():
        print(f"  {key:<10}: {show(out)}")
