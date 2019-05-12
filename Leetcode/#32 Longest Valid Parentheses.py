# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:16:25 2019

@author: binxi
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == '':
            return 0
            exit
        
        l, r, longest = 0, 0, 0
        s0 = ''
        
        for i in s:
            if i == '(':
                l += 1
            else:
                r += 1
            if l < r:
                l,r = 0,0
                longest = max(longest, self.longestValidParentheses(s0))
                s0 = ''
            else:
                s0 += i
        
        if l == r:
            return max(longest,2*r)
        else:
            s1 = ''
            for i in s0[::-1]:
                if i =='(':
                    s1 += ')'
                else:
                    s1 += '('
            return max(longest,self.longestValidParentheses(s1))