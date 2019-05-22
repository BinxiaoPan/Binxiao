# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:10:16 2019

@author: binxi
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]

        for i in dic:
            if len(dic[i]) > 1:
                lst = [abs(x-y) for x,y in zip(dic[i][:-1],dic[i][1:])]
                if min(lst) <= k:
                    return True
                    exit
        
        return False
