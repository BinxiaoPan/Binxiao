# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:11:39 2019

@author: binxi
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        rawlst = list(range(1,n+1,1))
        
        factorial = {}
        factorial[0] = 1
        factorial[1] = 1
        for i in range(2,n,1):
            factorial[i] = factorial[i-1]*i
        
        perm = ''
        
        while rawlst != []:
            l = len(rawlst)
            perm += str(rawlst[(k-1)//factorial[l-1]])
            k = k % factorial[l-1]
            rawlst.remove(int(perm[-1]))
        
        return perm
