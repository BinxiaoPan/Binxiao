# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:24:53 2019

@author: binxi
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index1 = 0
        index2 = len(numbers)-1
        
        while True:
            if numbers[index1] + numbers[index2] > target:
                index2 -=1
            elif numbers[index1] + numbers[index2] < target:
                index1 +=1
            else: break
        
        return [index1+1,index2+1]