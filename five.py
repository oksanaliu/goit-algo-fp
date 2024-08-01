import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def get_color(step, max_steps):
    # Генеруємо кольори від темних до світлих
    ratio = step / max_steps
    r = int(255 * ratio)
    g = int(100 + (155 * ratio))
    b = int(255 - (100 * ratio))
    return f"#{r:02X}{g:02X}{b:02X}"

def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Застосування кольорів
    node_colors = [colors.get(node, "#FFFFFF") for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, node_size=3000, node_color=node_colors, with_labels=True, arrows=False)
    plt.show()

def dfs(tree_root):
    stack = [tree_root]
    colors = {}
    step = 0
    max_steps = 7  # Задаємо максимальну кількість кроків для зміни кольору
    while stack:
        node = stack.pop()
        if node.id not in colors:
            colors[node.id] = get_color(step, max_steps)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return colors

def bfs(tree_root):
    queue = deque([tree_root])
    colors = {}
    step = 0
    max_steps = 7  # Задаємо максимальну кількість кроків для зміни кольору
    while queue:
        node = queue.popleft()
        if node.id not in colors:
            colors[node.id] = get_color(step, max_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return colors

# Створення дерева
root = Node(12)
root.left = Node(10)
root.right = Node(8)
root.left.left = Node(6)
root.left.right = Node(4)
root.right.left = Node(2)
root.right.right = Node(1)

# Візуалізація обходу в глибину (DFS)
print("DFS Traversal:")
dfs_colors = dfs(root)
draw_tree(root, dfs_colors)

# Візуалізація обходу в ширину (BFS)
print("BFS Traversal:")
bfs_colors = bfs(root)
draw_tree(root, bfs_colors)