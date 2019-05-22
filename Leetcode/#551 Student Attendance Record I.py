# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:30:02 2019

@author: binxi
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not (s.count('A') > 1 or 'LLL' in s)