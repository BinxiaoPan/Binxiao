# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:09:25 2019

@author: binxi
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = 0
        for i in set(list(s)):
            if s.count(i) % 2 == 1:
                n += 1
                if n == 2:
                    return False
                    exit
        return True