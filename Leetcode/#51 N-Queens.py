# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:23:53 2019

@author: binxi
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        board = [['.' for i in range(n)] for j in range(n)]

        banned = [[None for i in range(n)] for j in range(n)]

        for i in range(0,n,1):
            for j in range(0,n,1):
                banned[i][j] = []
                for t in range(i+1,n,1):
                    banned[i][j].append((t,j))
                    if (i+j-t) in range(0,n,1):
                        banned[i][j].append((t,i+j-t))
                    if (t+j-i) in range(0,n,1):
                        banned[i][j].append((t,t+j-i))
                copy = []
                for t in banned[i][j]:
                    if t not in copy:
                        copy.append(t)
                banned[i][j] = copy

        lst = []

        x,y = 0,0

        banned_actual = []

        while True:
            if board[x][y] == 'Q':
                board[x][y] = '.'
                for i,j in banned_actual[-1]:
                    board[i][j] = '.'
                y += 1
                banned_actual = banned_actual[:-1]
            elif board[x][y] == None:
                y += 1
            else:
                board[x][y] = 'Q'
                banned_actual.append([])
                for i,j in banned[x][y]:
                    if board[i][j] != None:
                        banned_actual[-1].append((i,j))
                    board[i][j] = None
                x += 1
                y = 0

            if x == n:
                copy = [p[:] for p in board]
                for i in range(0,n,1):
                    for j in range(0,n,1):
                        if copy[i][j] == None:
                            copy[i][j] = '.'
                lst.append(copy)
                y = n

            if y == n:
                x -= 1
                if x == -1:
                    break
                y = board[x].index('Q')        

        for i in range(0,len(lst),1):
            for j in range(0,len(lst[i]),1):
                lst[i][j] = ''.join(lst[i][j])

        return lst







