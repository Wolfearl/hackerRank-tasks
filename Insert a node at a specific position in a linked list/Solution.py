#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        # fptr.write(str(node.data))
        print(str(node.data))

        node = node.next

        if node:
            print(sep)
            # fptr.write(sep)


#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    if llist is None:
        return llist
    if position == 0:
        new_node.next = llist
        return new_node
    current = llist
    prev = None
    current_position = 0
    while current and current_position < position:
        prev = current
        current = current.next
        current_position += 1
    new_node.next = current
    if prev:
        prev.next = new_node
    return llist


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = 3

    llist = SinglyLinkedList()
    ll = [16, 13, 7]
    for i in range(llist_count):
        llist_item = ll[i]
        llist.insert_node(llist_item)

    data = 1

    position = 2

    llist_head = insertNodeAtPosition(llist.head, data, position)
    fptr = 1
    print_singly_linked_list(llist_head, ' ', fptr)
    # fptr.write('\n')

    # fptr.close()
