# -*- coding: utf-8 -*-
"""
Created on Sun May 12 22:51:03 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            exit
            
        path_lst = []
        
        def flatter(root):
            if (root.left == None) & (root.right == None):
                return [str(root.val)]
                exit
            lst = []  
            if root.left != None:
                lst_left = flatter(root.left)
                for i in lst_left:
                    lst.append(str(root.val) + i)
            if root.right != None:
                lst_right = flatter(root.right)
                for i in lst_right:
                    lst.append(str(root.val) + i)
            return lst
        
        path_lst = flatter(root)
        path_lst = list(map(lambda x:int(x),path_lst))
        
        return sum(path_lst)