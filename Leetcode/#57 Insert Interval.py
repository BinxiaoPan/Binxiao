# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:40:32 2019

@author: binxi
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return [newInterval]
            exit
        
        for i in range(0,len(intervals),1):
            if intervals[i][1] < newInterval[0]:
                continue
            else:
                break

        if intervals[i][1] < newInterval[0]:
            return intervals + [newInterval]
            exit

        for j in range(len(intervals)-1,-1,-1):
            if intervals[j][0] > newInterval[1]:
                continue
            else:
                break

        if intervals[j][0] > newInterval[1]:
            return [newInterval] + intervals
            exit
            
        lst = []

        lst += intervals[:i]

        lst.append([min(intervals[i][0],newInterval[0]),\
                    max(intervals[j][1],newInterval[1])])

        lst += intervals[j+1:]
        
        return lst