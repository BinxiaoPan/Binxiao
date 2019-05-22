# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:58:36 2019

@author: binxi
"""

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A1,A2 = [], []
        for i in A:
            if i%2 == 0:
                A1.append(i)
            else:
                A2.append(i)
        
        l = len(A)
        lst = []
        while A1 != []:
            lst.append(A1[0])
            A1 = A1[1:]
            if A2 != []:
                lst.append(A2[0])
                A2 = A2[1:]
        
        return lst