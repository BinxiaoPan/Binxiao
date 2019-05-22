# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:56:28 2019

@author: binxi
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
            exit
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])

        h = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]
        area = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

        h[0] = matrix[0][:]

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                h[i][j] = (h[i-1][j] + 1)* matrix[i][j]

        def largestRectangleArea(heights):

            if heights == []:
                return 0
                exit

            lo = min(heights)
            index = heights.index(lo)

            base = lo*len(heights)
            area1 = largestRectangleArea(heights[:index])
            area2 = largestRectangleArea(heights[index+1:])
            return max(base,area1,area2)

        max_area = 0
        for i in range(0,len(matrix)):
            max_area = max(max_area,largestRectangleArea(h[i]))
        
        return max_area