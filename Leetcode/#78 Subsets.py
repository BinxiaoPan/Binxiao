# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:21:25 2019

@author: binxi
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = [[]]
        for i in nums:
            new_lst = []
            for j in lst:
                new_lst.append(j)
                new_lst.append(j+[i])
            lst = new_lst
        
        return lst