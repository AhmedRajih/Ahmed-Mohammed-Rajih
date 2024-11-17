
-class Node:
def __init_(self, name):
self.name nane
self.children = []
def add child(self, child): self.children.append(child)
def build tree():
root Node("A")
node_b Node("8")
nodec Node("C") node_d Node("0")
node e Node("E")
node f Node("F")
node_g Node("G")
node_h Node("H")
root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)
node_c.add_child(node_g)
node_d.add_child(node_e)
node_e.add_child(node_h)
return root
def print tree(root, level=0): indent level
print(indent root.name)
for child in root.children:
print_tree(child, level +1)
def bfs(root):
queue [root]
result = [] while queue:
node queue.pop(8)
result.append(node.name) for child in node.children:
queue.append(child)
return result
def dfs(root):
stack [root]
result = [ ]
while stack:
node stack.pop()
result.append(node.name)
for child in reversed(node.children):
stack.append(child)
return result
#main program
root build_tree()
print("My Tree")
print tree(root)
ahile True:
print("Enter your choice: ")
print("1.BFS Algorithe")
print(*2.0FS Algorithm")