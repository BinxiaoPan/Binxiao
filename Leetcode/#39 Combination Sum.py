# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:41:35 2019

@author: binxi
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 1:
            if target % candidates[0] == 0:
                return [candidates*int(target/candidates[0])]
            else:
                return []
            exit
        
        comb = []
        for i in range(0,int(target/candidates[0])+1,1):
            rest = self.combinationSum(candidates[1:],target-i*candidates[0])
            for j in rest:
                comb += [i*[candidates[0]]+j]
        
        return comb
    