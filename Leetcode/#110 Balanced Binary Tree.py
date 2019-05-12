# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 23:01:11 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
            exit
            
        def depth(rt):
            if rt == None:
                return 0
            else:
                return 1 + max(depth(rt.left),depth(rt.right))
        
        if depth(root.left) + depth(root.right) <=1:
            return True
            exit
        
        if abs( depth(root.left) - depth(root.right) ) >1:
            return False
            exit
        
        return (self.isBalanced(root.left))&(self.isBalanced(root.right))