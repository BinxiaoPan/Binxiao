# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:02:02 2019

@author: binxi
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def ListNodeConverter(lst):
    
    origin = ListNode(lst[0])
    head = origin
    for i in lst[1:]:
        head.next = ListNode(i)
        head = head.next
    
    return origin
