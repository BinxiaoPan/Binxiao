# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:42:13 2019

@author: binxi
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s == s[::-1]:
            return s
            exit

        l=len(s)

        for i in range(1,l+1,1):
            for j in range(0,i,1):
                txt = s[j:j+l-i+1]
                if txt == txt[::-1]:
                    return txt
                    exit
