# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:41:37 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
            exit
            
        root = TreeNode(preorder[0])
        
        index = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:1+index],inorder[:index])
        root.right = self.buildTree(preorder[1+index:],inorder[index+1:])
        
        return root