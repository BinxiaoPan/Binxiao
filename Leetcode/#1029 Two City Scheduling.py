# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:37:35 2019

@author: binxi
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        n = len(costs)

        costs.sort(key = lambda x:x[1]-x[0])

        cost1, cost2 = costs[: n//2],costs[n//2 :]

        return sum(map(lambda x: x[1], cost1)) + sum(map(lambda x: x[0], cost2))