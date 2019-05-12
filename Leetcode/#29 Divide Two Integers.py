# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:04:38 2019

@author: binxi
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == 0:
            return 0
            exit

        positive = ((dividend>0) == (divisor>0))*2-1

        dividend, divisor = abs(dividend),abs(divisor)

        zeros = []

        for i in range (0,len(str(dividend))-len(str(divisor)) + 1,1):
            zeros.append(int(str(divisor) + '0'*i))

        remainder, quotient = dividend, 0

        while remainder>=divisor:
            for i in range(len(zeros)-1,-1,-1):
                if zeros[i] <= remainder:
                    break
            while zeros[i] <= remainder:
                remainder -= zeros[i]
                quotient += int('1'+'0'*i)

        quotient = quotient*positive
        
        if (quotient > 2147483647) | (quotient < -2147483648):
            return 2147483647
        else:
            return quotient
