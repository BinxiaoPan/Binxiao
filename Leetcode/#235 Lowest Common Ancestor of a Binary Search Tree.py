# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:16:48 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        last = {}
        
        last[root] = None
        
        def research(root):
            if root != None:
                last[root.left] = root
                last[root.right] = root
                research(root.left)
                research(root.right)
        
        research(root)
        
        lst1 = []
        
        while p != None:
            lst1.append(p)
            p = last[p]
        
        while q not in lst1:
            q = last[q]
        
        return q