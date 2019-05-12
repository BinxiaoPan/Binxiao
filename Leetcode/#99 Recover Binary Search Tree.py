# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:26:26 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def listed(root0):
            if root0 == None:
                return []
            else:
                return listed(root0.left) + [root0] + listed(root0.right)
        
        lst = listed(root)
        
        lst_num = []
        
        for i in lst:
            lst_num.append(i.val)
        
        lst_num.sort()
        
        for i in range(0,len(lst),1):
            lst[i].val = lst_num[i]