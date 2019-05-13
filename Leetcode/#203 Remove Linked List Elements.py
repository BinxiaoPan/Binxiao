# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:47:56 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
            
        lst = []
        
        while head != None:
            if head.val != val:
                lst.append(head)
            head = head.next

        if lst == []:
            return None
            exit
        for i in range(1,len(lst)):
            lst[i-1].next = lst[i]
        
        lst[-1].next = None
        
        return lst[0]