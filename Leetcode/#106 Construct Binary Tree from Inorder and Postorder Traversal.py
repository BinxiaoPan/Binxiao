# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:08:31 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        if inorder == []:
            return None
            exit
        
        root = TreeNode(postorder[-1])
        
        index = inorder.index(postorder[-1])
        
        l_inorder = inorder[:index]
        r_inorder = inorder[index+1:]
        
        l_postorder = postorder[:len(l_inorder)]
        r_postorder = postorder[len(l_inorder):-1]
        
        root.left = self.buildTree(l_inorder,l_postorder)
        root.right = self.buildTree(r_inorder,r_postorder)
        
        return root