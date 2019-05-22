# -*- coding: utf-8 -*-
"""
Created on Mon May 20 20:16:35 2019

@author: binxi
"""

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        grid = list(filter(lambda x: sum(x) >1, grid))

        grid = list(map(list,zip(*grid)))

        grid = list(filter(lambda x: sum(x) >1, grid))
        
        if len(grid) <= 1:
            return 0
            exit        
        
        m, n = len(grid), len(grid[0])

        count = 0

        for i in range(m):
            for j in range(i+1,m):
                lst = [ grid[i][t]+grid[j][t] for t in range(n)]
                num = lst.count(2)
                count += num*(num-1)//2

        return count