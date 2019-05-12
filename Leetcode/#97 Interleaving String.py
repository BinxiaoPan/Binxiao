# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:07:14 2019

@author: binxi
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if (s1 == '')|(s2 == ''):
            return s1 + s2 == s3
            exit

        l1, l2, l3 = len(s1), len(s2), len(s3)

        if l1 + l2 != l3:
            return False
            exit    

        match = [[False for j in range(l2+1)] for i in range(l1+1)] 

        for i in range(1,l1+1,1):
            match[i][0] = (s1[-i:] == s3[-i:])
        for j in range(1,l2+1,1):
            match[0][j] = (s2[-j:] == s3[-j:])


        for i in range(1,l1+1,1):
            for j in range(1,l2+1,1):
                if (s1[-i:][0] == s3[-i-j:][0]) & match[i-1][j]:
                    match[i][j] = True
                if (s2[-j:][0] == s3[-i-j:][0]) & match[i][j-1]:
                    match[i][j] = True

        return match[l1][l2]