# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:10:18 2019

@author: binxi
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        change = [0,0]
        
        for i in bills:
            if i == 5:
                change[0] += 1
            elif i == 10:
                change[0] -= 1
                change[1] += 1
            else:
                if change[1] == 0:
                    change[0] -= 3
                else:
                    change[0] -= 1
                    change[1] -= 1
            if change[0] <0 :
                return False
                exit
        return True