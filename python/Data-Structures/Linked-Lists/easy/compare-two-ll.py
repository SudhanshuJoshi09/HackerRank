#!/bin/python3

import os
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
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    l1 = llist1
    l2 = llist2
    
    while l1 is not None and l2 is not None:
        if l1.data != l2.data:
            return 0
        l1 = l1.next
        l2 = l2.next
    
    if l1 is None and l2 is not None:
        return 0
    elif l1 is not None and l2 is None:
        return 0
    else:
        return 1

if __name__ == '__main__':