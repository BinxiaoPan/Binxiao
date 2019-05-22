# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:30:57 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        lst = []
        
        def search(rt):
            if rt != None:
                lst.append(rt.val)
                search(rt.left)
                search(rt.right)
        
        search(root)
        
        lst.sort()
        
        return lst[k-1]
        