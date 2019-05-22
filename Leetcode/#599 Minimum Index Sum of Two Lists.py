# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:57:44 2019

@author: binxi
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_sum = {}
        
        for i in (set(list1) & set(list2)):
            index_sum[i] = list1.index(i) + list2.index(i)
        
        max_index = min([index_sum[i] for i in index_sum])

        return list(filter(lambda x: index_sum[x] == max_index, index_sum))