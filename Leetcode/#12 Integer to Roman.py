# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:09:49 2019

@author: binxi
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman = ''

        k = int(num/1000)
        h = (int(num/100)%10)
        t = (int(num/10)%10)
        u = num%10

        def generator(n,one,five,ten):
            ro=''
            if n<=3:
                for i in range(1,n+1,1):
                    ro=ro+one
                return ro
            elif n==4:
                return one+five
            elif n<=8:
                return five + generator(n-5,one,five,ten)
            else:
                return one+ten

        roman += generator(k,'M','','')
        roman += generator(h,'C','D','M')
        roman += generator(t,'X','L','C')
        roman += generator(u,'I','V','X')

        return roman        