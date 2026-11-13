"""Part A: Binary Tree (SAMSON) with BFS and DFS."""
from collections import deque

from common import name, show, show_list


class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def build_tree():
    root = TreeNode("S1")
    root.left = TreeNode("A")
    root.right = TreeNode("M")
    root.left.left = TreeNode("S2")
    root.left.right = TreeNode("O")
    root.right.left = TreeNode("N")
    return root


def tree_bfs(root):
    """Level order using a queue."""
    result = []
    queue = deque([root])
    step = 1
    while queue:
        node = queue.popleft()
        result.append(node.label)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print(f"  Step {step}: visit {name(node.label):<2} | queue = "
              f"{show_list([n.label for n in queue])}")
        step += 1
    return result


def tree_dfs(root):
    """Pre-order: Root, Left, Right."""
    result = []
    step = [1]

    def visit(node):
        if node is None:
            return
        result.append(node.label)
        print(f"  Step {step[0]}: visit {name(node.label)}")
        step[0] += 1
        visit(node.left)
        visit(node.right)

    visit(root)
    return result


def run():
    print("\nPART A: BINARY TREE\n")
    print("            S")
    print("           / \\")
    print("          A   M")
    print("         / \\  |")
    print("        S   O N\n")

    root = build_tree()
    print("Breadth-First Search (BFS)")
    bfs = tree_bfs(root)
    print("\nDepth-First Search (DFS, pre-order)")
    dfs = tree_dfs(root)

    print("\nRESULT")
    print("  BFS:", show(bfs))
    print("  DFS:", show(dfs))
