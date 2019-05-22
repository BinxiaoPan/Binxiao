# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:36:59 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        lst = []
        
        def search(rt):
            if rt != None:
                lst.append(rt.val)
                search(rt.left)
                search(rt.right)
        
        search(root)
        
        lst.sort(key = lambda x:abs(x-target))
        
        return lst[0]