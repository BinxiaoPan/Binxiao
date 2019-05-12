# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:30:38 2019

@author: binxi
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        copy = strs[:]
        for i in range(0,len(copy),1):
            copy[i] = ''.join(sorted(copy[i]))
                
        dic = {}
        for unique in set(copy):
            dic[unique] = []
        
        for i in range(0,len(copy),1):
            dic[copy[i]].append(strs[i])

        group = []
        
        for i in dic:
            group.append(dic[i])

        return group
