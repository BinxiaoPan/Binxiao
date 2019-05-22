# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:48:32 2019

@author: binxi
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        dic = {}

        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        s = []
        for i in dic:
            s.append(dic[i]*i)

        s.sort(key= lambda x:len(x),reverse = True)

        s = ''.join(s)
        
        return s