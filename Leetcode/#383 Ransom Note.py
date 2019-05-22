# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:14:38 2019

@author: binxi
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lst1 = list(ransomNote)
        lst2 = list(magazine)
        
        while lst1 != []:
            if lst1[0] in lst2:
                lst2.remove(lst1[0])
                lst1 = lst1[1:]
            else:
                break
                
        return lst1 == []