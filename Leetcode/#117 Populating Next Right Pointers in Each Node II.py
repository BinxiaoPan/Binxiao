# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:51:57 2019

@author: binxi
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root == None:
            return None
            exit
            
        lst = []
        
        def flater(root1,n):
            if root1 != None:
                if len(lst) < n:
                    lst.append([])
                lst[n-1].append(root1)
                flater(root1.left, n+1)
                flater(root1.right, n+1)
        
        flater(root,1)
        
        for level in range(0,len(lst),1):
            for i in range(0,len(lst[level])-1,1):
                lst[level][i].next = lst[level][i+1]
        
        return lst[0][0]