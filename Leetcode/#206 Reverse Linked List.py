# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:24:02 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None
            exit
            
        lst = []
        while head != None:
            lst.append(head)
            head = head.next 
        
        lst = lst[::-1]
        
        for i in range(1,len(lst)):
            lst[i-1].next = lst[i]
        
        lst[-1].next = None
        
        return lst[0]