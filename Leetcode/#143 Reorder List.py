# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:25:57 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return []
            exit
            
        lst = []
        
        while head != None:
            lst.append(head)
            head = head.next
        
        i = -1
        j = len(lst)
        
        lst1 = []
        
        while True:
            i += 1
            j -= 1
            if i > j:
                break
            elif i == j:
                lst1.append(lst[i])
            else:
                lst1.append(lst[i])
                lst1.append(lst[j])
        
        for i in range(1,len(lst1)):
            lst1[i-1].next = lst1[i]
        
        lst1[-1].next = None