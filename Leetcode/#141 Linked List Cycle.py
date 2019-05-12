# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:57:23 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        lst = []
        
        while head != None:
            lst.append(head)
            head = head.next
            if head in lst:
                return True
                exit
        
        return False