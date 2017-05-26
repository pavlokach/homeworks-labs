class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return "<Node %s> " % str(self.data)

if __name__ == "__main__":
    nd1 = Node(3)
    nd2 = Node("UCU")
    nd3 = Node("Arman")
    nd1.next = nd2
    nd2.next = nd3
    temp_nd = nd1
    while temp_nd.next is not None:
        print(temp_nd, end='=> ')
        temp_nd = temp_nd.next
    print(temp_nd)