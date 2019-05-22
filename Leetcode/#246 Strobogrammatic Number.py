# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:03:11 2019

@author: binxi
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'6':'9','9':'6','0':'0','8':'8','1':'1'}
        
        for i in num:
            if i not in dic:
                return False
                exit
                
        lst = list(num)
        lst1 = list(map(lambda x:dic[x],lst))
        
        return lst == lst1[::-1]