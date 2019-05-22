# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:36:06 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]