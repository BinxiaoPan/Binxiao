# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:00:11 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        lst = []

        while head != None:
            lst.append(head)
            head = head.next

        lst[m-1:n] = lst[m-1:n][::-1]

        for i in range(0,len(lst)-1,1):
            lst[i].next = lst[i+1]

        lst[-1].next = None

        return lst[0]