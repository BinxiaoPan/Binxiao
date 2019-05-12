# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:13:38 2019

@author: binxi
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        S = S.replace('-','')
        
        if S == '':
            return S
            exit
        
        S0 = S[:len(S)%K]
        
        S = S[len(S)%K:]
        
        while S != '':
            S0 += '-'
            S0 += S[:K]
            S = S[K:]
        
        if S0[0] == '-':
            S0 = S0[1:]

        S0 = S0.upper()
        
        return S0