# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:04:47 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if root == None:
            return []
            exit
            
        lst = [[root]]

        while True:
            flag = True
            lst1 = []
            for path in lst:
                if path[-1].left != None:
                    lst1.append(path + [path[-1].left])
                    flag = False
                if path[-1].right != None:
                    lst1.append(path + [path[-1].right])
                    flag = False
                if path[-1].left == path[-1].right == None: 
                    lst1.append(path)
            lst = [x[:] for x in lst1]
            if flag:
                break

        def transform(node_lst):
            val_lst = [x.val for x in node_lst]
            s = str(val_lst[0])
            for val in val_lst[1:]:
                s += '->' + str(val)
            return s

        for i in range(len(lst)):
            lst[i] = transform(lst[i])
        
        return lst