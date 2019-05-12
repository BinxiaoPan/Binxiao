# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:33:18 2019

@author: binxi
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == '':
            return 1
            exit

        lst = [0 for i in range(len(s))]

        for i in range(1,len(s)+1,1):
            if s[-i] == '0':
                lst[-i] = 0
                continue
            if i == 1:
                lst[-i] = 1
                continue
            if i == 2:
                if int(s[-i:]) <= 26:
                    lst[-i] = lst[-i+1]+1
                else:
                    lst[-i] = lst[-i+1]
                continue
            if int(s[-i:2-i]) > 26:
                lst[-i] = lst[-i+1]
            else:
                lst[-i] = lst[-i+1] + lst[-i + 2]
        
        return lst[0]