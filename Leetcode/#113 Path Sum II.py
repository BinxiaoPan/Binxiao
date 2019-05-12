# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:17:52 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path_dic = {}
        
        def dict_gen(path, root1):
            if root1 != None:
                path_dic[root1] = path + [root1]
                dict_gen(path_dic[root1],root1.left)
                dict_gen(path_dic[root1],root1.right)
        
        dict_gen([],root)
        
        lst = []
        
        for i in path_dic:
            if (i.left == None) & (i.right == None):
                numeric_path = []
                for j in path_dic[i]:
                    numeric_path.append(j.val)
                total = 0
                for j in numeric_path:
                    total += j
                if total == sum:    
                    lst.append(numeric_path)
        
        return lst