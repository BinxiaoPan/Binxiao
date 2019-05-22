# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:09:39 2019

@author: binxi
"""

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        l = len(grid)
        if grid == [[grid[0][0] for i in range(l)] for j in range(l)]:
            return Node(grid[0][0], True, None, None, None, None)
        else:
            tl = self.construct([x[:l//2] for x in grid[:l//2]])
            tr = self.construct([x[l//2:] for x in grid[:l//2]])
            bl = self.construct([x[:l//2] for x in grid[l//2:]])
            br = self.construct([x[l//2:] for x in grid[l//2:]])
            return Node('*',False,tl,tr,bl,br)