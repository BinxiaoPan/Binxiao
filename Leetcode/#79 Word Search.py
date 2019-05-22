# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:49:54 2019

@author: binxi
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m,n = len(board), len(board[0])

        origin = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    origin.append((i,j))

        def dfp(board1,word1,x,y):
            if word1 == '':
                return True
                exit
            lst= []
            if x > 0:
                lst.append((x-1,y))
            if y > 0:
                lst.append((x,y-1))
            if x < m-1:
                lst.append((x+1,y))
            if y < n-1:
                lst.append((x,y+1))
            for x1,y1 in lst:
                if board1[x1][y1] == word1[0]:
                    board1[x1][y1] = None
                    if dfp(board1,word1[1:],x1,y1):
                        return True
                        exit
                    board1[x1][y1] = word1[0]
            return False

        for x,y in origin:
            board[x][y] = None
            if dfp(board,word[1:],x,y):
                return True
                exit
            board[x][y] = word[0]
        return False
