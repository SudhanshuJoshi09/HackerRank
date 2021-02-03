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
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    t1 = head1
    t2 = head2
    res = None
    
    if head1 is None and head2 is not None:
        return head2
    elif head2 is None and head1 is not None:
        return head1
    elif head1 is None and head2 is None:
        return None
    
    head_res = None
    
    while t1 is not None and t2 is not None:
        if res is None:
            if t1.data > t2.data:
                res = t2
                head_res = res
                t2 = t2.next
            else:
                res = t1
                head_res = res
                t1 = t1.next
        else:
            if t1.data > t2.data:
                res.next = t2
                res = res.next
                t2 = t2.next
            else:
                res.next = t1
                res = res.next
                t1 = t1.next
            
    if t1 is None:
        res.next = t2
    elif t2 is None:
        res.next = t1
                
    return head_res

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
