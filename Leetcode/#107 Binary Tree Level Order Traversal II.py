# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:44:54 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        l = self.levelOrderBottom(root.left)
        r = self.levelOrderBottom(root.right)
        
        l = l[::-1]
        r = r[::-1]
        
        root_leveled = [[root.val]]

        l_len = len(l)
        r_len = len(r)
        
        for i in range(1,max(l_len,r_len)+1,1):
            root_leveled.append([])
            if i <= l_len:
                root_leveled[i] += l[i-1]
            if i <= r_len:
                root_leveled[i] += r[i-1]
        
        return root_leveled[::-1]