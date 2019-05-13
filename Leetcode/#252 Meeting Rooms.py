# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:58:42 2019

@author: binxi
"""

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key = lambda x: x[0])
        
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
                exit
        
        return True