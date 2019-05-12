# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:38:12 2019

@author: binxi
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =='':
            return 0
            exit;
        
        slen=len(s)

        import numpy as np
        
        lenc = np.array([],dtype=int)

        while s != '':
            if len(s)==1:
                lenc = np.append(lenc,1)                       
                break;
            apd=s[1:].find(s[0])+1
            if apd == 0:
                apd = len(s)
            lenc = np.append(lenc,[apd])
            s = s[1:]

        end=np.array(range(0,len(lenc),1))

        end=end+lenc-1

        for i in range(0,slen,1):
            end[i] = min(end[i:end[i]+1])

        length= end+1-np.array(range(0,len(lenc),1))

        return max(length)