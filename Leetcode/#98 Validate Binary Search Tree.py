# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:42:18 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def listed(root1):
            if root1 == None:
                return []
            else:
                return listed(root1.left) + [root1] + listed(root1.right)
        
        lst = listed(root)
        
        val_lst = []
        
        for i in lst:
            val_lst.append(i.val)
        
        copy = val_lst[:]
        copy.sort()
        
        for i in range(0,len(copy)-1,1):
            if copy[i] == copy[i+1]:
                return False
                exit
        
        return val_lst == copy