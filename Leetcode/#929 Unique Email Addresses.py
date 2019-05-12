# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:56:56 2019

@author: binxi
"""

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        for i in range(0, len(emails),1):
            s = emails[i]
            sep = s.index('@')
            part1 = s[:sep]
            part2 = s[sep+1:]
            if '+' in part1:
                sep = part1.index('+')
                part1 = part1[:sep]
            part1 = part1.replace('.','')
            emails[i] = part1 + '@' + part2
            emails[i] = emails[i].lower()
        
        return len(list(set(emails)))