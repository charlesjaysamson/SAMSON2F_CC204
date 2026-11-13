"""Shared helpers for Part A and Part B."""

LINE = "=" * 52


def name(node_id):
    """Both S nodes are stored as S1 and S2 internally but shown as S."""
    return "S" if node_id.startswith("S") else node_id


def show(items):
    return " - ".join(name(i) for i in items)


def show_list(items):
    return "[" + ", ".join(name(i) for i in items) + "]"
