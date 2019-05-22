# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:19:22 2019

@author: binxi
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
            exit
        
        dp = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in reversed(range(i)):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)

        return max(dp)