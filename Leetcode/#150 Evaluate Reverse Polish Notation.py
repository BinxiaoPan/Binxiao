# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:48:21 2019

@author: binxi
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
    
        operation = ['+','-','*','/']

        lst = []
        
        for i in tokens:
            if i not in operation:
                lst.append(int(i))
            else:
                if i == '+':
                    lst = lst[:-2] + [lst[-2] + lst[-1]]
                elif i == '-':
                    lst = lst[:-2] + [lst[-2] - lst[-1]]                
                elif i == '*':
                    lst = lst[:-2] + [lst[-2] * lst[-1]]                
                else:
                    positive = lst[-2] / lst[-1] >=0
                    positive = positive*2-1
                    lst = lst[:-2] + [positive*(abs(lst[-2]) // abs(lst[-1]))]

        return lst[0]