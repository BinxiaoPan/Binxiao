# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:58:43 2019

@author: binxi
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        lst = []
        
        for i in range(0,n,1):
            lst.append(str(i+1))
        
        for i in range(1,(n//3)+1,1):
            lst[3*i-1] = 'Fizz'
        
        for i in range(1,(n//5)+1,1):
            lst[5*i -1] = 'Buzz'
        
        for i in range(1,(n//15)+1,1):
            lst[15*i-1] = 'FizzBuzz'
        
        return lst