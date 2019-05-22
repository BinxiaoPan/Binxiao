# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:36:51 2019

@author: binxi
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        dic = {}
        letter_count = []

        t0 = list(set(t))

        for i in range(len(t0)):
            dic[t0[i]] = i
            letter_count.append(0)

        for i in range(len(t)):
                letter_count[dic[t[i]]] -= 1

        l,r = 0,2**31
        i,j = 0,-1

        while i < len(s):
            while True in map(lambda x:x<0, letter_count):
                j += 1
                if j == len(s):
                    break
                if s[j] in dic:
                    letter_count[dic[s[j]]] += 1
            if j == len(s):
                break
            if j-i < r-l:
                r,l = j,i
            while True not in map(lambda x:x<0, letter_count):
                if s[i] in dic:
                    letter_count[dic[s[i]]] -= 1
                if j-i < r-l:
                    r,l = j,i        
                i += 1
                if i == len(s):
                    break
                    
        if r >= len(s):
            return ''
        else:
            return s[l:r+1]