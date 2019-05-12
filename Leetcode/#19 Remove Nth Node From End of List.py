# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:56:15 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        cp = head
        
        l = 1
        
        while cp.next is not None:
            cp = cp.next
            l +=1
        
        n = l + 1 - n 
        
        if n==1:
            return head.next
            exit
        
        cp  = head
        
        for i in range(1, n, 1):
            cp = cp.next
        
        cp_2 = head
        
        for i in range(1, n-1,1):
            
            cp_2 = cp_2.next
        
        cp_2.next = cp.next
        
        return head