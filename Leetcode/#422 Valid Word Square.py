# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:45:29 2019

@author: binxi
"""

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = max(len(words), max(map(lambda x:len(x),words)))
        words += [' '*n for j in range(n-len(words))]
        
        for i in range(n):
            words[i] += ' '*(n-len(words[i]))
            
        for i in range(n):
            for j in range(i+1,n):
                if words[i][j] != words[j][i]:
                    return False
                    exit
        return True