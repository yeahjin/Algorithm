import string
import sys
class Node:
    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self,node):
        if node:
            print(node.item, end= "")
            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    def inorder(self, node):
        if node:
            if node.left:
                self.inorder(node.left)
            print(node.item, end = "")
        if node.right:
            self.inorder(node.right)

    def postorder(self,node):
        if node:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            print(node.item, end = "")


l = list(string.ascii_uppercase)
t = int(input())
nodes = {}
for i in range(t):
    nodes[l[i]] = (Node(l[i]))
bt = BinaryTree()
bt.root = nodes["A"]
for _ in range(t):
    a, b, c = map(str,sys.stdin.readline().split())
    if b != ".":
        nodes[a].left = nodes[b]
    if c != ".":
        nodes[a].right = nodes[c]


bt.preorder(bt.root)
print()
bt.inorder(bt.root)
print()
bt.postorder(bt.root)