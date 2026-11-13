"""Part B: Graph (SAMSON) with BFS and DFS."""
from collections import deque

from common import name, show, show_list

# Adjacency list. Edges: S-S, S-A, A-M, M-O, O-N, N-S
graph = {
    "S1": ["S2", "A"],
    "S2": ["S1", "N"],
    "A":  ["S1", "M"],
    "M":  ["A", "O"],
    "O":  ["M", "N"],
    "N":  ["O", "S2"],
}


def graph_bfs(start):
    visited = {start}
    queue = deque([start])
    result = []
    step = 1
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        print(f"  Step {step}: visit {name(vertex):<2} | queue = {show_list(queue)}")
        step += 1
    return result


def graph_dfs(start):
    visited = set()
    result = []
    step = [1]

    def visit(vertex):
        visited.add(vertex)
        result.append(vertex)
        print(f"  Step {step[0]}: visit {name(vertex)}")
        step[0] += 1
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return result


def run():
    print("\nPART B: GRAPH\n")
    print("                    M")
    print("    S____A_____/    |")
    print("    |              /")
    print("    S             /")
    print("   /      ____O__/")
    print(" N___/\n")
    print("Edges: S-S, S-A, A-M, M-O, O-N, N-S\n")

    print("Breadth-First Search (BFS)")
    bfs = graph_bfs("S1")
    print("\nDepth-First Search (DFS)")
    dfs = graph_dfs("S1")

    print("\nRESULT")
    print("  BFS:", show(bfs))
    print("  DFS:", show(dfs))
