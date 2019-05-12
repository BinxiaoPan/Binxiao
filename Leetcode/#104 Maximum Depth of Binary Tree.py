# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:13:55 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            exit
        
        return (1 + max(self.maxDepth(root.left),self.maxDepth(root.right)))