# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:12:11 2019

@author: binxi
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        board = [['.' for i in range(n)] for j in range(n)]

        banned = [[None for i in range(n)] for j in range(n)]

        for i in range(0,n,1):
            for j in range(0,n,1):
                banned[i][j] = []
                for t in range(0,n,1):
                    banned[i][j].append([t,j])
                    banned[i][j].append([i,t])
                    if (i+j-t) in range(0,n,1):
                        banned[i][j].append([t,i+j-t])
                    if (t+j-i) in range(0,n,1):
                        banned[i][j].append([t,t+j-i])
                copy = []
                for t in banned[i][j]:
                    if t not in copy:
                        copy.append(t)
                banned[i][j] = copy

        lst = []

        x,y = 0,0

        while True:
            if board[x][y] == 'Q':
                board[x][y] = '.'
                y += 1
            else:
                valid = True
                for t in banned[x][y]:
                    if board[t[0]][t[1]] == 'Q':
                        valid = False
                        break
                if valid:
                    board[x][y] = 'Q'
                    x += 1
                    y = 0
                else:
                    board[x][y] = '.'
                    y += 1

            if x == n:
                lst.append([p[:] for p in board])
                y = n

            if y == n:
                x -= 1
                if x == -1:
                    break
                y = board[x].index('Q')        
            
        return len(lst)