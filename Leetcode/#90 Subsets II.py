# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:17:36 2019

@author: binxi
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = {}
        for i in set(nums):
            count[i] = nums.count(i)
        
        lst = [[]]
        for i in count:
            new_lst = []
            for j in range(0,count[i]+1,1):
                for t in lst:
                    new_lst.append(t+[i for n in range(j)])
            lst = new_lst
        
        return lst