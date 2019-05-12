# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:12:33 2019

@author: binxi
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        lst1, lst2 = list(num1), list(num2)
        lst1, lst2 = lst1[::-1], lst2[::-1]

        for i in range(0,len(num1)):
            lst1[i] = int(lst1[i])

        for i in range(0,len(num2)):
            lst2[i] = int(lst2[i])

        lst3 = [0 for i in range(len(num1)+len(num2))]

        for i in range(0,len(num1)):
            for j in range(0,len(num2)):
                lst3[i+j] += lst1[i]* lst2[j]

        forwarder = 0
        for i in range(0,len(lst3),1):
            lst3[i] += forwarder
            forwarder = lst3[i]//10
            lst3[i] = lst3[i]%10

        lst3 = lst3[::-1]
        for i in range(0,len(lst3),1):
            if lst3[i] != 0:
                break

        multipled = ''
        for i in lst3[i:]:
            multipled += str(i)        
        
        return multipled