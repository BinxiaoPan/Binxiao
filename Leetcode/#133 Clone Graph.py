# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:28:02 2019

@author: binxi
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if node == None:
            return None
            exit
            
        lst = []
        sys.setrecursionlimit(5000)
        def search(node):
            if node not in lst:
                lst.append(node)
                for i in node.neighbors:
                    search(i)
                
        search(node)
        lst1 = []
        dic = {}
        
        for i in range(len(lst)):
            lst1.append(Node(lst[i].val,lst[i].neighbors))
            dic[lst[i]] = lst1[i]
        
        for i in range(len(lst)):
            lst1[i].neighbors = list(map(lambda x: dic[x], lst1[i].neighbors))
        
        return lst1[0]