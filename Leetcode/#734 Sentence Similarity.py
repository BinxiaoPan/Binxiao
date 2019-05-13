# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:38:48 2019

@author: binxi
"""

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
            exit
        
        pairs1 = []
        for i in pairs:
            pairs1.append(i[::-1])
        
        pairs += pairs1
        
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                if [words1[i], words2[i]] not in pairs:
                    return False
                    exit
        
        return True