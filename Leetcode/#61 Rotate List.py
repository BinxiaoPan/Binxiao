# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:14:11 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
            exit
            
        lst = [head]
        
        while head.next != None:
            head = head.next
            lst.append(head)
        
        lst[-1].next = lst[0]

        length = len(lst)
        
        k = k % length
        
        node = lst[length - 1 - k].next
        
        lst[length - 1 - k].next = None
        
        return node