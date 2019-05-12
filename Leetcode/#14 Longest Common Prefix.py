# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:28:51 2019

@author: binxi
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
            exit
        
        l=2**31-1
        
        for i in range(0,len(strs),1):
            if len(strs[i])<l:
                l = len(strs[i])
                s = strs[i]
        
        while True:
            
            if s == '':
                return s
                exit
                
            flag = True  
            
            for i in strs:
                if s != i[:l]:
                    flag = False
                    break;
            
            if flag:
                return s
                exit
                
            s = s[:-1]
            l -= 1