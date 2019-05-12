# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:07:40 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if root == None:
            return None
            exit
        
        def listed(root1):
            if root1 == None:
                return []
            else:
                return [root1] + listed(root1.left) + listed(root1.right)
        
        lst = listed(root)
        
        for i in range(0,len(lst)-1,1):
            lst[i].left = None
            lst[i].right = lst[i+1]
        
        lst[-1].left = None
        lst[-1].right = None