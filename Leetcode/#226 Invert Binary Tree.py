# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:32:33 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return None
            exit
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        
        return root