# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:35:01 2019

@author: binxi
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return None
            exit
        
        nums = list(range(1,n+1,1))
        
        def gen2(lst):
            if lst == []:
                return [None]
                exit
            if len(lst) == 1:
                return [TreeNode(lst[0])]
            forest = []
            for i in range(0,len(lst),1):
                for l in gen2(lst[:i]):
                    for r in gen2(lst[1+i:]):
                        forest.append(TreeNode(lst[i]))
                        forest[-1].left = l
                        forest[-1].right = r
            return forest
        
        return gen2(nums)
