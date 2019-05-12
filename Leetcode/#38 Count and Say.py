# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:07:29 2019

@author: binxi
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
            exit
            
        previous = self.countAndSay(n-1)
            
        def Say(s):
            if s == '':
                return s
            s0 = s[0]
            l = 0
            for i in s:
                if i == s0:
                    l += 1
                else:
                    break
            return str(l)+s0+Say(s[l:])
        
        return Say(previous)