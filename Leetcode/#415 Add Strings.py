# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:32:06 2019

@author: binxi
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num1,num2 = num2,num1
        
        num1 = '0'*(len(num2)-len(num1)) + num1
        num1,num2 = '0' + num1,'0' + num2
        lst1,lst2 = list(num1),list(num2)
        lst1 = map(lambda x:int(x),lst1)
        lst2 = map(lambda x:int(x),lst2)
        for i in range(len(lst1)):
            lst1[i] += lst2[i]
        upgrade = 0
        for i in reversed(range(len(lst1))):
            lst1[i] += upgrade
            upgrade = lst1[i] // 10
            lst1[i] = lst1[i] % 10
        
        if lst1[0] == 0:
            lst1 = lst1[1:]
        
        lst1 = map(lambda x: str(x),lst1)
        
        if lst1 == []:
            lst1.append('0')
        
        return ''.join(lst1)