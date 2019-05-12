# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:58:54 2019

@author: binxi
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = len(s)

        if s == l*' ':
            return 0
            exit
        
        last = ' '
        
        while s != '':
            if (last[-1] == ' ') & (s[0] != ' '):
                last = s[0]
            else:
                last += s[0]
            s = s[1:]
        

        last = last.replace(' ','')

        return len(last)