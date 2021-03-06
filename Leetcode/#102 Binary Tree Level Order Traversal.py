# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:45:29 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
            exit
            
        lst = [[root]]
        
        while lst[-1] != []:
            lst.append([])
            for i in lst[-2]:
                if i.left != None:
                    lst[-1].append(i.left)
                if i.right != None:
                    lst[-1].append(i.right)
        
        lst = lst[:-1]
        
        lst1 = []
        
        for level in lst:
            lst1.append([])
            for node in level:
                lst1[-1].append(node.val)
        
        return lst1