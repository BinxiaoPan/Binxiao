# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:09:47 2019

@author: binxi
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        symbol = ['I','V','X','L','C','D','M']

        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 

        num=0


        while True:
            if len(s) == 0:
                break
            if len(s) == 1:
                num += dic[s]
            else:
                if symbol.index(s[0])<symbol.index(s[1]):
                    num += -dic[s[0]]
                else:
                    num += dic[s[0]]
            s = s[1:]

        return num

