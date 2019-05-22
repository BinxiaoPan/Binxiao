# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:51:55 2019

@author: binxi
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if wordDict == []:
            return s == ''
            exit
            
        len_lst = list(set(map(lambda x:len(x),wordDict)))
        longest = max(len_lst)

        dp = [True] + [False for i in range(len(s))]

        gap = 0

        for i in range(1,len(s)+1):
            for j in len_lst:
                if j <= i:
                    if dp[i-j] & (s[i-j:i] in wordDict):
                        dp[i] = True
                        gap = 0
                        break
            if dp[i]:
                continue
            else:
                gap += 1
                if gap > longest:
                    return False
                    exit

        return dp[-1]