# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:16:20 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root == None:
            return sum == ()
            exit
        
        if root.left == root.right == None:
            return sum == root.val
            exit
        
        if root.left == None:
            return self.hasPathSum(root.right, sum - root.val)
        elif root.right == None:
            return self.hasPathSum(root.left, sum - root.val)
        else:
            return (self.hasPathSum(root.left, sum - root.val) | self.hasPathSum(root.right, sum - root.val))
        
        