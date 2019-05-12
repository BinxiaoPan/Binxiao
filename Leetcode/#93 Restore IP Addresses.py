# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:21:29 2019

@author: binxi
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lst = []
        for a in range(0,256,1):
            a1 = str(a)
            if a1 not in s:
                continue
            if s.index(a1) != 0:
                continue

            for b in range(0,256,1):
                b1 = str(b)
                if a1 + b1 not in s:
                    continue
                if s.index(a1 + b1) != 0:
                    continue

                for c in range(0,256,1):
                    c1 = str(c)
                    if a1 + b1 + c1 not in s:
                        continue
                    if s.index(a1 + b1 + c1) != 0:
                        continue

                    for d in range(0,256,1):
                        d1 = str(d)
                        if a1 + b1 + c1 + d1 == s:
                            lst.append(a1+'.'+b1+'.'+c1+'.'+d1)        
        return lst