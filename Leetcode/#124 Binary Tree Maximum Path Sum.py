# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:17:13 2019

@author: binxi
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0
            exit
            
        level = [[root]]
        
        dic = {}
        dic[root] = {}
        
        while True:
            last = True
            level.append([])
            for node in level[-2]:
                if node.left != None:
                    level[-1].append(node.left)
                    dic[node.left] = {}
                    last = False
                if node.right != None:
                    level[-1].append(node.right)
                    dic[node.right] = {}
                    last = False
            if last:
                break
        
        level = level[:-1]
        
        l, r, b = 'left','right','branch'
        
        for i in reversed(range(len(level))):
            for node in level[i]:
                if node.left == None:
                    dic[node][l] = 0
                else:
                    dic[node][l] = dic[node.left][b]
                if node.right == None:
                    dic[node][r] = 0
                else:
                    dic[node][r] = dic[node.right][b]
                dic[node][b] = node.val + max(dic[node][l], dic[node][r], 0)
        
        max_path = -2**31
        
        for i in range(len(level)):
            for node in level[i]:
                path = node.val
                path += max(0,dic[node][l])
                path += max(0,dic[node][r])
                max_path = max(path, max_path)
        
        return max_path