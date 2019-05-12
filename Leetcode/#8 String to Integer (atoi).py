# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:13:29 2019

@author: binxi
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """        
        
        if str in ['','+','-']:
            return 0
            exit
        
        while str[0] == ' ':
            return self.myAtoi(str[1:])
        
        nums = ['0','1','2','3',
                '4','5','6','7','8',
                '9']
        signs = ['+','-']
        
        if (str[0] not in nums) & (str[0] not in signs) :
            return 0
            exit

        positive = True
        
        if str[0] == '+':
            str=str[1:]
        elif str[0] == '-':
            positive = False
            str=str[1:]

        if str[0] not in nums:
            return 0
            exit
            
        for i in range(1,len(str),1):
            if str[i] not in nums:
                str = str[:i]
                break
                
        inted = int(str)
        
        if not positive:
            inted=-inted
        
        inted = min(inted, 2**31-1)
        inted = max(inted, -2**31)
        
        return inted