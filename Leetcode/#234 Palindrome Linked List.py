# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:47:17 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        lst = []
        
        while head != None:
            lst.append(head)
            head = head.next
        
        lst = map(lambda x:x.val,lst)
        
        return lst == lst[::-1]