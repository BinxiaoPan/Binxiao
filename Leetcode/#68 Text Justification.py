# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:16:38 2019

@author: binxi
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        lst = []

        while words != []:
            lst.append('')
            count = -1
            for i in range(0,len(words),1):
                count += 1 + len(words[i])
                if count > maxWidth:
                    count -= 1 + len(words[i])
                    i -= 1
                    break
            copy = words[:i+1]
            words = words[i+1:]

            if words == []:
                lst[-1] = copy[0]
                for i in copy[1:]:
                    lst[-1] += ' ' + i
                lst[-1] += ' ' * (maxWidth - len(lst[-1]))
                break

            if len(copy) == 1:
                lst[-1] = copy[0] + (maxWidth - len(copy[0]))*' '
            else:
                longer = (maxWidth - count) % (len(copy)-1)
                extra = (maxWidth - count) // (len(copy)-1) +1

                lst[-1] += copy[0]
                for i in range(1,len(copy),1):
                    if i <= longer:
                        lst[-1] += ' '
                    lst[-1] += extra * ' '
                    lst[-1] += copy[i]        
        
        return lst
    