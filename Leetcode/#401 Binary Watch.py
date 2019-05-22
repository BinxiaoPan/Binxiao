# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:17:46 2019

@author: binxi
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        hr_led = {}
        min_led = {}

        def binary_led(n):
            count = 0
            while n != 0:
                count += n % 2
                n = n // 2
            return count

        for i in range(12):
            n = binary_led(i)
            if n not in hr_led:
                hr_led[n] = [str(i)]
            else:
                hr_led[n].append(str(i))

        for i in range(60):
            n = binary_led(i)
            if i >9:
                i1 = str(i)
            else:
                i1 = '0'+str(i)
            if n not in min_led:
                min_led[n] = [i1]
            else:
                min_led[n].append(i1)

        lst = []

        for i in set(hr_led):
            for j in set(min_led):
                if i+j == num:
                    for hr in hr_led[i]:
                        for min in min_led[j]:
                            lst.append(hr+':'+min)

        return lst        