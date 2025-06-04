#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        # fptr.write(str(node.data))
        print(str(node.data))

        node = node.next

        if node:
            print(sep)
            # fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    if not llist:
        return llist
    current = llist
    newHead = None
    ki = []
    while current:
        next_node = current.next
        current.next, current.prev = current.prev, current.next
        if current.next is None:
            ki.append([str(current.prev.data), str(current.data), None])
        elif current.prev is None:
            ki.append([None, str(current.data), str(current.next.data)])
        else:
            ki.append([str(current.prev.data), str(current.data), str(current.next.data)])
        newHead = current
        current = next_node
    return newHead

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    for t_itr in range(1):
        # llist_count = int(input())
        llist_count = 4

        llist = DoublyLinkedList()
        ll = [1, 2, 3, 4]
        for i in range(llist_count):
            llist_item = ll[i]
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)
        fptr = 1
        print_doubly_linked_list(llist1, ' ', fptr)
        # fptr.write('\n')

    # fptr.close()
