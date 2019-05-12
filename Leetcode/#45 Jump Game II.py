# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:19:51 2019

@author: binxi
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)

        step = [None] * l

        step[0] = 0

        begin = 0

        for i in range(0,l,1):

            if step[i] is None:

                max_step = step[i-1]

                end = i-1

                for j in range(begin, i, 1):

                    end = max(end, j + nums[j])

                end = min(l-1, end)

                for j in range(i, end+1, 1):

                    step[j] = max_step +1

                begin = i

        return step[-1]
