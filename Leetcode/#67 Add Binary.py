# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:32:57 2019

@author: binxi
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        gap = abs(len(a) - len(b)) * '0'

        if len(a) > len(b):
            b = gap + b
        else:
            a = gap + a

        c =''

        for i in range(0,len(a),1):
            x = int(a[i])
            y = int(b[i])
            c += str(x+y)

        c = '00' + c

        l = len(c)


        for i in range(l-1,1,-1):
            if int(c[i])>1:
                c = c[:i]+ str(int(c[i])-2) + c[i+1:]
                c = c[:i-1]+ str(int(c[i-1])+1) + c[i:]

        while c[0] == '0':
            if c == '0':
                break
            c = c[1:]
        
        return c