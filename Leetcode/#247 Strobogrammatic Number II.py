# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:11:00 2019

@author: binxi
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['0','1','8']
            exit
            
        dic = {'6':'9','9':'6','0':'0','8':'8','1':'1'}

        lst = ['1','6','9','8']

        for i in range(1,n//2):
            lst1 = []
            for num in lst:
                for j in dic:
                    lst1.append(num + j)
            lst = lst1[:]

        lst1 = []

        for i in lst:
            num = list(i)[::-1]
            num = list(map(lambda x:dic[x], num))
            lst1.append(''.join(num))

        if n % 2 == 0:
            mid = ['']
        else:
            mid = ['0','8','1']

        lst2 = []

        for i in range(len(lst)):
            for m in mid:
                lst2.append(lst[i] + m +lst1[i])
        
        return lst2
