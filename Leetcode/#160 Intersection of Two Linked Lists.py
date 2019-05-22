# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:01:05 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        lst1 = {}
        
        while headA != None:
            lst1[headA] = None
            headA = headA.next
        
        while headB != None: 
            if headB not in lst1:
                headB = headB.next
            else:
                break
        
        return headB