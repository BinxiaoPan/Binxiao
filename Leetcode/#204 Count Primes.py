# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:50:09 2019

@author: binxi
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        dic = {}
        for i in range(2,n,1):
            dic[i] = True

        for i in dic:
            if dic[i] :
                for j in range(2, (n-1)//i+1, 1):
                    dic[j*i] = False
        
        count = 0
        
        for i in dic:
            if dic[i]:
                count += 1
        
        return count