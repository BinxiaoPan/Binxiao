# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:32:35 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        copy = head

        a = head
        b = head
        
        while a != None:
            while b.val == a.val:
                b = b.next
                if b == None:
                    break
            a.next = b
            a = a.next

        
        return copy