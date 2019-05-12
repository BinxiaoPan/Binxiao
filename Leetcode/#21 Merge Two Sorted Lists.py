# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:12:37 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        lst1 = []
        lst2 = []

        while l1 is not None:
            lst1.append(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            lst2.append(l2.val)
            l2 = l2.next
        
        lst = lst1 + lst2
        
        lst.sort()
        
        lst = lst[::-1]
        
        tail = None
        head = None
        
        for i in lst:
            head = ListNode(i)
            head.next = tail
            tail = head
        
        return head