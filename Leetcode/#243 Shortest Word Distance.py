# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:53:57 2019

@author: binxi
"""

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        lst1,lst2 = [],[]
        
        for i in range(len(words)):
            if words[i] == word1:
                lst1.append(i)
            if words[i] == word2:
                lst2.append(i)
        
        minimum = 2**31
        
        for i in lst1:
            for j in lst2:
                minimum = min(minimum,abs(i-j))
        
        return minimum