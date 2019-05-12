# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:46:13 2019

@author: binxi
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
            exit
        
        s = s.lower()
        
        s_clear = ''
        
        for i in s:
            if ('a' <= i <= 'z') | ('0' <= i <= '9'):
                s_clear += i        
                
        return s_clear == s_clear[::-1]