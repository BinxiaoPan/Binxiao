# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:22:57 2019

@author: binxi
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        else:
            if (word[0] != word[0].upper()) | (word[1:] != word[1:].lower()):
                return False
            else:
                return True