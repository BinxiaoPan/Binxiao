# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 01:12:38 2019

@author: binxi
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []
            exit
        
        if n == 1:
            return ['()']
        
        comb = []
        
        for i in self.generateParenthesis(n-1):
            comb.append('('+i+')')
        
        for i in range(1,n,1):
            
            xs = self.generateParenthesis(i)
            ys = self.generateParenthesis(n-i)
            
            for x in xs:
                for y in ys:
                    comb.append(x+y)
        
        return set(comb)