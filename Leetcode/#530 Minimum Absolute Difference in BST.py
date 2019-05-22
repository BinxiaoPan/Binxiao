# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:26:47 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        lst = []
        
        def search(rt):
            if rt != None:
                lst.append(rt)
                search(rt.left)
                search(rt.right)
        
        search(root)
        
        lst = [x.val for x in lst]
        
        lst.sort()
        
        lst = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
        
        return min(lst)