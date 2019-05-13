# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:24:16 2019

@author: binxi
"""

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
            exit

        count = 0
        
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
        
        dup = len(A) != len(set(A))
        
        if count == 2:
            return sorted(A) == sorted(B)
        elif count == 0:
            return dup
        else:
            return False