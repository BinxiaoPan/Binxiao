# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:38:15 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None
            exit
        
        lst = []
        while head != None:
            lst.append(head)
            head = head.next
        
        lst1 = []
        lst2 = []

        for i in lst:
            if i.val < x:
                lst1.append(i)
            else:
                lst2.append(i)

        lst_new = lst1 + lst2

        for i in range(0,len(lst_new)-1,1):
            lst_new[i].next = lst_new[i+1]

        lst_new[-1].next = None
        
        return lst_new[0]