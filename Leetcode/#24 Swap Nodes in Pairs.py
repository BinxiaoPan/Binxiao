# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:35:42 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        chaos = ListNode(0)

        chaos.next = head
        
        tail = chaos
        
        while True:
            if head is None:
                break
            if head.next is None:
                break
            tail.next = head.next
            copy = head.next.next
            head.next.next = head
            head.next = copy
            tail = head
            head = head.next                    
        return chaos.next