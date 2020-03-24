__author__ = 'A88253'

import os
import sys
import subprocess
from collections import deque
import graphviz as pgv

class LLRBT:
    root=None

    def put(self, key, val):
        self.root = self.put2(self.root, key, val)
        self.root.color=Node.BLACK

    def put2(self, node, key, val):
        if node is None:
            return Node(key, val,Node.RED)
        if key < node.key:
            node.left = self.put2(node.left, key, val)
        elif key > node.key:
            node.right = self.put2(node.right, key, val)
        else:
            node.val = val

        if self.isRed(node.right) and not self.isRed(node.left):
            node=self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node=self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)

        return node

    def isRed(self, n):
        if n is None:
            return False
        else:
            return n.color == Node.RED

    def rotateLeft(self, h):
        assert(self.isRed(h.right))
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = Node.RED
        return x

    def rotateRight(self,h):
        assert(self.isRed(h.left))
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = Node.RED
        return x

    def flipColors(self, h):
        assert(not self.isRed(h))
        assert(self.isRed(h.left))
        assert(self.isRed(h.right))
        h.color = Node.RED
        h.left.color = Node.BLACK
        h.right.color = Node.BLACK

    # draw the graph
    def drawTree(self, filename):
        # create an empty undirected graph
        G=pgv.AGraph('graph myGraph {}')

        # create queue for breadth first search
        q = deque([self.root])
        # breadth first search traversal of the tree
        while len(q) != 0:
            node = q.popleft()
            #G.add_node(node, label=node.key+":"+str(node.val))
            G.add_node(node, label="")
            if node.left is not None:
                # draw the left node and edge
                #G.add_node(node.left, label=node.left.key+":"+str(node.left.val))
                G.add_node(node.left, label="")
                G.add_edge(node, node.left)
                q.append(node.left)
            if node.right is not None:
                # draw the right node and edge
                # G.add_node(node.right, label=node.right.key+":"+str(node.right.val))
                G.add_node(node.right, label="")
                G.add_edge(node, node.right)
                q.append(node.right)

        # render graph into PNG file
        G.draw(filename,prog='dot')
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])

    def createTree(self):
        self.put("B",4)
        self.put("A",3)
        self.put("C",5)

class Node:
    RED = True
    BLACK = False
    left = None
    right = None
    key = 0
    val = 0
    color = None

    def __init__(self, key, val, color):
        self.key = key
        self.val = val
        self.color = color

llrbt = LLRBT()
llrbt.createTree()
llrbt.drawTree("demo-llrbt.png")


