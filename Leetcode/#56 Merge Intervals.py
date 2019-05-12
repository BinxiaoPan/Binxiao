# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:51:48 2019

@author: binxi
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []
            exit
            
        merged = [intervals[0]]
        ovlap = False
        
        for interval in intervals[1:]:
            overlap = False
            for i in range(0,len(merged),1):
                if (merged[i][0]<= interval[1]) & (merged[i][0]>= interval[0]):
                    merged[i][0] = interval[0]
                    overlap = True
                if (merged[i][1] >= interval[0]) & (merged[i][1]<= interval[1]):
                    merged[i][1] = interval[1]
                    overlap = True
                if (merged[i][0] >= interval[0]) & (merged[i][1]<= interval[1]):
                    merged[i][0], merged[i][1] = interval[0], interval[1]
                    overlap = True
                if (merged[i][0] <= interval[0]) & (merged[i][1]>= interval[1]):
                    overlap = True

            if not overlap:
                merged.append(interval)
            ovlap = ovlap|overlap
        
        if not ovlap:
            return merged
        else:
            return self.merge(merged)