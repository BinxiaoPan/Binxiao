# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:50:52 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        lst = []
        
        def search(rt):
            if rt != None:
                lst.append(rt)
                search(rt.left)
                search(rt.right)
        
        search(root)
        
        return len(lst)