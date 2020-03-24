__author__ = 'A88253'

import os
import sys
import subprocess
import pygraphviz as pgv
from collections import deque

class BST:
    root = None

    def put(self, key, val):
        self.root = self.put2(self.root, key, val)

    def put2(self, node, key, val):
        if node is None:
            #key is not in tree, create node and return node to parent
            return Node(key, val)
        if key < node.key:
            # key is in left subtree
            node.left = self.put2(node.left, key, val)
        elif key > node.key:
            # key is in right subtree
            node.right = self.put2(node.right, key, val)
        else:
            node.val = val
        return node

    # draw the graph
    def drawTree(self, filename):
        # create an empty undirected graph
        G = pgv.AGraph('graph myGraph {}')

        # create queue for breadth first search
        q = deque([self.root])
        # breadth first search traversal of the tree
        while len(q) != 0:
            node = q.popleft()
            G.add_node(node, label=node.key+":"+str(node.val))
            if node.left is not None:
                # draw the left node and edge
                G.add_node(node.left, label=node.left.key+":"+str(node.left.val))
                G.add_edge(node, node.left)
                q.append(node.left)
            if node.right is not None:
                # draw the right node and edge
                G.add_node(node.right, label=node.right.key+":"+str(node.right.val))
                G.add_edge(node, node.right)
                q.append(node.right)

        # render graph into PNG file
        G.draw(filename, prog='dot')
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])

    # Question 4
    def createTree(self):
        self.root = Node("F", 6)

        self.put("F", 6)
        self.put("D", 4)
        self.put("C", 3)
        self.put("E", 5)
        self.put("B", 2)
        self.put("A", 1)

        self.put("I", 9)
        self.put("G", 7)
        self.put("J", 10)
        self.put("H", 8)

        # self.inorderTraversal(self.root)

    # Question 5



class Node:
    left = None
    right = None
    key = 0
    val = 0

    def __init__(self, key, val):
        self.key = key
        self.val = val

bst = BST()
bst.createTree()
bst.drawTree("question4.png")

key_input = input("Please enter Key: ");
found = bst.get(key_input)
print(str(found))




