# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 02:42:25 2019

@author: binxi
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
                
        if words == []:
            return []
            exit

        m,n = len(words), len(words[0])
            
        l = m*n
        
        def match(s,words):
            word = words[:]
            while s != '':
                if s[:n] not in word:
                    return False
                    exit
                else:
                    word.remove(s[:n])
                    s = s[n:]
            return len(word) == 0
            
            
        index_lst = []
        
        for i in range(0,len(s)-l+1,1):
            if match(s[i:i+l],words):
                index_lst.append(i)
        
        return index_lst