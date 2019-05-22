# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:05:01 2019

@author: binxi
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = [-1] + [2**31 for i in range(len(s))]

        for i in range(1,len(s)+1):
            for l in range(i,0,-1):
                if s[i-l:i] == s[i-l:i][::-1]:
                    dp[i] = min(dp[i],dp[i-l]+1)

        
        return dp[-1]