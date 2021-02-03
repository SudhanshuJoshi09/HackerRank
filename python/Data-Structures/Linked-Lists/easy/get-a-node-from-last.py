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

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    list_len = 0
    temp_ptr = head
    
    while temp_ptr is not None:
        temp_ptr = temp_ptr.next
        list_len += 1
        
    positionFromHead = list_len - positionFromTail - 1
    temp_ptr = head
    
    while positionFromHead != 0:
        temp_ptr = temp_ptr.next
        positionFromHead -= 1
        
    return temp_ptr.data
        

if __name__ == '__main__':