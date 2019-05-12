# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:03:13 2019

@author: binxi
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target <0:
            return []
            exit
            
        if len(candidates) == 1:
            if target == candidates[0]:
                return [candidates]
            else:
                return []
            exit
        
        candidates.sort()

        comb = []

        if candidates[0] == target:
            comb.append([candidates[0]])

        planA = self.combinationSum2(candidates[1:],target-candidates[0])
        for i in planA:
            if [candidates[0]]+i not in comb:
                comb.append([candidates[0]]+i)

        planB = self.combinationSum2(candidates[1:],target)
        for i in planB:
            if i not in comb:
                comb.append(i)

        return  comb