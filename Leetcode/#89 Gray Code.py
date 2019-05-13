# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:52:03 2019

@author: binxi
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        lst = [None for i in range(n+2)]

        lst[0], lst[1] = ['0'], ['0','1']

        for i in range(2,n+1,1):
            lst[i] = []
            for j in lst[i-1]:
                lst[i].append('0'+j)
            for j in lst[i-1][::-1]:
                lst[i].append('1'+j)

        num_lst = []

        for i in lst[n]:
            num = 0
            for j in i[::-1]:
                num = num*2 + int(j)
            num_lst.append(num)

        return num_lst