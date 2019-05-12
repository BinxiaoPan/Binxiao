# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:51:15 2019

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
        
        lst = []
        
        while head != None:
            lst.append(head)
            head = head.next
        
        dup = None
        
        distinct = []
        
        for i in range(0,len(lst),1):
            if i < len(lst)-1:
                if lst[i].val == lst[i+1].val:
                    dup = lst[i].val
            if lst[i].val != dup:
                distinct.append(i)
        
        for i in range(0,len(distinct),1):
            distinct[i] = lst[distinct[i]]
        
        for i in range(0,len(distinct)-1,1):
            distinct[i].next = distinct[i+1]
        
        if distinct == []:
            return None
            exit
            
        distinct[-1].next = None
        
        return distinct[0]