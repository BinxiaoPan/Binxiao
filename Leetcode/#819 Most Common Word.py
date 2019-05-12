# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:04:12 2019

@author: binxi
"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count = {}

        for i in "!?',;." :
            paragraph = paragraph.replace(i,' ')

        paragraph = paragraph.lower()

        words = paragraph.split()

        unbanned = list(set(words))

        for i in banned:
            if i in unbanned:
                unbanned.remove(i)

        for i in unbanned:
            count[i] = 0

        for i in words:
            if i in unbanned:
                count[i] += 1

        buzz = ''
        bench = 0
        for i in unbanned:
            if count[i] > bench:
                bench = count[i]
                buzz = i

        return buzz