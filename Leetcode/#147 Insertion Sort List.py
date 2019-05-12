# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:45:52 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
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
        
        lst.sort(key = lambda x: x.val)
        
        for i in range(0,len(lst)-1,1):
            lst[i].next = lst[i+1]
        
        lst[-1].next = None
        
        return lst[0]