# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:55:52 2019

@author: binxi
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        lst = []
        for i in dic:
            if dic[i] == 1:
                lst.append(i)
        
        return lst