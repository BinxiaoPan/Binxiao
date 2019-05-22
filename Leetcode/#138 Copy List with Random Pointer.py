# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:14:48 2019

@author: binxi
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
            exit
        
        lst = []
        while head != None:
            lst.append(head)
            head = head.next
        
        dic = {}
        lst1 = []
        for i in range(len(lst)):
            lst1.append(Node(lst[i].val,None,None))
            lst1[i].random = lst[i].random
            dic[lst[i]] = lst1[i]
        
        dic[None] = None
        
        for i in range(len(lst1)):
            lst1[i].random = dic[lst1[i].random]
        
        for i in range(len(lst1)-1):
            lst1[i].next = lst1[i+1]
        
        return lst1[0]