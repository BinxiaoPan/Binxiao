# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:55:49 2019

@author: binxi
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
            
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]