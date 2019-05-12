# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:38:23 2019

@author: binxi
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        chaos = ListNode(666)

        chaos.next = head

        record = {}

        for i in range(0,k+1,1):
            record[i] = ''

        record[k] = chaos

        while True:
            record[0] = record[k]

            for i in range(1,k+1,1):
                record[i] = ''

            for i in range(1,k+1,1):
                record[i] = record[i-1].next
                if record[i] == None:
                    break

            if record[i] == None:
                break

            for i in range(1,int(k/2)+1,1):
                x = record[i]
                record[i] = record[k+1-i]
                record[k+1-i] = x

            record[k].next = record[1].next

            for i in range(0,k,1):
                record[i].next = record[i+1]

        return chaos.next