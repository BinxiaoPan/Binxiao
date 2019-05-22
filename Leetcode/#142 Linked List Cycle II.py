# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:02:02 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        lst = []

        while head != None:
            if head in lst:
                return head
                break
            else:
                lst.append(head)
                head = head.next