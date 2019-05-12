# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:29:40 2019

@author: binxi
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        dic = {'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
        
        if digits == '':
            return []
            exit
                
        first = dic[digits[0]]
        
        if len(digits) == 1:
            return first
            exit
        
        follower = self.letterCombinations(digits[1:])

        combination = []
        
        for i in first:
            for j in follower:
                combination.append(i+j)
        
        return combination