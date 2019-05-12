# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 22:38:58 2019

@author: binxi
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        missing = []

        for i in range(0,9,1):
            for j in range(0,9,1):
                if board[i][j] == '.':
                    board[i][j] = '0'
                    missing.append([i,j])
                board[i][j] = int(board[i][j])

        i = 0

        while i != len(missing):
            x,y = missing[i][0], missing[i][1]
            board[x][y] += 1
            while board[x][y] <= 9:
                valid = True
                for j in range(0,9,1):
                    if (j != y) & (board[x][j] == board[x][y]):
                        valid = False
                        break
                    if (j != x) & (board[j][y] == board[x][y]):
                        valid = False
                        break
                if valid:
                    for j in range((x//3)*3,(x//3)*3+3,1):
                        for t in range((y//3)*3,(y//3)*3+3,1):
                            if ((j,t) != (x,y)) & (board[j][t] == board[x][y]):
                                valid = False
                                break
                                break
                if valid:
                    i += 1
                    break
                else:
                    board[x][y] += 1
            if board[x][y] == 10:
                board[x][y] = 0
                i -= 1

        for i in range(0,9,1):
            for j in range(0,9,1):
                board[i][j] = str(board[i][j])