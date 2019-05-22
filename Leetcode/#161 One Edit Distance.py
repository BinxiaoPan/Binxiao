# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:07:36 2019

@author: binxi
"""

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < len(t):
            s,t = t,s
        ls,lt = len(s),len(t)
        if ls == lt:
            count = 0
            for i in range(ls):
                if s[i] != t[i]:
                    count += 1
                    if count == 2:
                        break
            return count == 1
        elif ls - lt == 1:
            if lt == 0:
                return True
            elif s[:-1] == t:
                return True
            else:
                for i in range(lt):
                    if s[i] != t[i]:
                        break
                return s[i+1:] == t[i:]
        else:
            return False