# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:39:21 2019

@author: binxi
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = map(lambda x:str(x),nums)

        nums = ''.join(nums)

        nums = nums.split('0')

        nums = map(lambda x:len(x),nums)

        return max(nums)