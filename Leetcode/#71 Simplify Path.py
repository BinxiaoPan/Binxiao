# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:19:13 2019

@author: binxi
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        while '//' in path:
            path = path.replace('//','/')

        lst = []

        while path != '':
            if path.count('/') == 1:
                lst.append(path)
                path = ''
            else:
                index = path.index('/',1)
                lst.append(path[:index])
                path = path[index:]

        while '/.' in lst:
            lst.remove('/.')

        while '/..' in lst:
            index = lst.index('/..')
            if index == 0:
                lst = lst[1:]
            else:
                lst = lst[:index-1]+ lst[index+1:]

        simple = ''.join(lst)

        if simple == '':
            return '/'
            exit
            
        if simple == '/':
            return simple
        else:
            if simple[-1] =='/':
                return simple[:-1]
            else:
                return simple