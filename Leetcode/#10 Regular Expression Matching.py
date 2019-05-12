# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:04:29 2019

@author: binxi
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0:
            return len(s)==0
            exit
        
        if len(p)==1:
            if ( p == '.' ):
                return len(s) == 1
                exit
            else:
                return p==s
                exit
                
        if p[1] != '*':

            if s=='':
                return False
                exit

            if p[0] == '.':
                return self.isMatch(s[1:],p[1:])
                exit

            if p[0] != s[0]:
                return False
                exit
            else:
                return self.isMatch(s[1:],p[1:])
                
        else:

            if p[0] == '.':
                
                s_copy = s
                
                while True:
                    if s_copy == '':
                        return self.isMatch(s_copy, p[2:])
                        exit
                    if self.isMatch(s_copy, p[2:]):
                        return True
                        exit
                    s_copy = s_copy[1:]
                
                return self.isMatch

            else:
                
                s_copy = s
                
                while True:
                    if self.isMatch(s_copy, p[2:]):
                        return True
                        exit
                    if s_copy == '':
                        return False
                        exit
                    if s_copy[0] == p[0]:
                        s_copy = s_copy[1:]
                    else:
                        return False
                        exit