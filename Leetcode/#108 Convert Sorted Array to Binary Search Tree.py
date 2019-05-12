# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:05:33 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        
        l = len(nums)
        center = int(l/2)
        tree = TreeNode(nums[center])
        
        
        
        tree.left = self.sortedArrayToBST(nums[:center])
        tree.right = self.sortedArrayToBST(nums[center + 1 : ])
        
        return tree