# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:30:42 2019

@author: binxi
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s = [x[::-1] for x in s]
        return ' '.join(s)