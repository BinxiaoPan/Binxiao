# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:40:52 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None:
            return q == None
            exit
        
        if q == None:
            return p == None
            exit
        
        return (p.val == q.val) & self.isSameTree(p.left,q.left) & \
                                self.isSameTree(p.right,q.right)