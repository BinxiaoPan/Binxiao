# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:29:18 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            exit
            
        def listed(root1):
            if root1 == None:
                return [[]]
            else:
                flat = []
                for r in listed(root1.right):
                    flat.append([root1.val]+r)
                for l in listed(root1.left):
                    flat.append([root1.val]+l)
                return flat
        
        flated = listed(root)
        
        right_view = []
        
        while flated != []:
            right_view += flated[0]
            k = len(flated[0])
            for i in range(0,len(flated),1):
                flated[i] = flated[i][k:]
            while [] in flated:
                flated.remove([])
        
        return right_view