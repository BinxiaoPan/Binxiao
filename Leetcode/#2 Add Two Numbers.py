# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:38:11 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        l3 = l1.val + l2.val
        
        if l1.val + l2.val <10:
            l3 = ListNode(l3)
            l3.next = self.addTwoNumbers(l1.next,l2.next)
            return l3
        else: 
            l3 = ListNode(l3-10)
            l4_addup = ListNode(1)
            l4 = self.addTwoNumbers(l1.next,l2.next)
            l3.next = self.addTwoNumbers(l4_addup,l4)
            return l3