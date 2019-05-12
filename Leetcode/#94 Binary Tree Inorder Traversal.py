# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:45:23 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            exit
        
        return self.inorderTraversal(root.left)\
                + [root.val]\
                + self.inorderTraversal(root.right)