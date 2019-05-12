# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:58:43 2019

@author: binxi
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if s1 == s2:
            return True
            exit
        
        for l in range(1,len(s1),1):
            if sorted(s1[:l]) == sorted(s2[:l]):
                if self.isScramble(s1[:l],s2[:l]) & self.isScramble(s1[l:], s2[l:]):
                    return True
                    exit
            if sorted(s1[:l]) == sorted(s2[-l:]):
                if self.isScramble(s1[:l],s2[-l:]) & self.isScramble(s1[l:], s2[:-l]):
                    return True
                    exit
        
        return False