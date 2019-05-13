# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:29:54 2019

@author: binxi
"""

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        direction = 0
        
        distance = [0 for i in range(4)]
        
        instructions = instructions * 4
        
        while instructions != '':
            if instructions[0] == 'G':
                distance[direction] += 1
            elif instructions[0] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            instructions = instructions[1:]
        
        return distance[0] == distance[2] and distance[1] == distance[3]