from node import *


# A class implementing Multiset as a linked list.

class Multiset:
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.nexts = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.nexts
        if current is not None:
            if previous is None:
                self._head = self._head.nexts
            else:
                previous.nexts = current.nexts

    def remove_all(self):
        self._head == None

    def __str__(self):
        s = ''
        tmp = self._head
        while tmp is not None:
            s += str(tmp.data)
            tmp = tmp.nexts
        return s

    def __len__(self):
        n = 0
        current, head = self._head, self._head
        while current != head:
            n += 1
            current = current.nexts
        return n

    def split_half(self):
        l = len(self)
        m1 = Multiset()
        m2 = Multiset()
        elem = self._head
        for i in range(l):
            m1.add(elem) if i < l // 2 else m2.add(elem)
        return m1, m2


if __name__ == "__main__":
    nd1 = Node(3)
    nd2 = Node("UCU")
    nd3 = Node("Arman")
    m = Multiset()
    m.add(nd1)
    m.add(nd2)
    m.add(nd3)
    m2, m3 = m.split_half()
    print(str(m2))
    nd1.next = nd2
    nd2.next = nd3
    temp_nd = nd1
    while temp_nd.next is not None:
        print(temp_nd, end='=> ')
        temp_nd = temp_nd.next
    print(temp_nd)

