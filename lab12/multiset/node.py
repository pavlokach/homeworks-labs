"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""

class Node(object):

    def __init__(self, data, nexts = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = nexts

class TwoWayNode(Node):

    def __init__(self, data, previous = None, nexts = None):
        Node.__init__(self, data, nexts)
        self.previous = previous

# Just an empty link
node1 = None

# A node containing data and an empty link
node2 = Node("A", None)

# A node containing data and a link to node2
node3 = Node("B", node2)
