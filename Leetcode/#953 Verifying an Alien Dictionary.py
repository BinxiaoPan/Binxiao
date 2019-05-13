# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:41:53 2019

@author: binxi
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        dictionary = {}

        for  i in range(26):
            dictionary[order[i]] = chr(97+i)
        
        def translate(s):
            s = list(s)
            s = map(lambda x:dictionary[x],s)
            return ''.join(s)
        
        words = list(map(lambda x: translate(x),words))
        
        words1 = words[:]
        
        words1.sort()
        
        return words == words1