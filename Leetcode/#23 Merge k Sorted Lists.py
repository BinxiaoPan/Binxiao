# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:14:38 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        lst=[]
        
        for i in range(0,len(lists),1):
            lst.append([])

        for i in range(0,len(lists),1):
            while lists[i] is not None:
                lst[i].append(lists[i].val)
                lists[i] = lists[i].next

        lstsum = []
        
        for i in lst:
            lstsum = lstsum +i
        
        lstsum.sort()
        
        lstsum = lstsum[::-1]
        
        tail = None
        head = None
        
        for i in lstsum:
            head = ListNode(i)
            head.next = tail
            tail = head
        
        return head   