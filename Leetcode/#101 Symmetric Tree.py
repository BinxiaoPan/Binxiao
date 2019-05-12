# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:51:26 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
            exit
            
        if root.left == root.right == None:
            return True
            exit

        if (( root.left is None ) | ( root .right is None)):
            return False
            exit    

        if root.left.val != root.right.val:
            return False
            exit

        tree1 = TreeNode(root.val)
        tree1.left = root.left.left
        tree1.right = root.right.right

        tree2 = TreeNode(root.val)
        tree2.left = root.left.right
        tree2.right = root.right.left

        return (self.isSymmetric(tree1) & self.isSymmetric(tree2))