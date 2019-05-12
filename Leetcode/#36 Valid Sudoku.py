# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:33:57 2019

@author: binxi
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(0,9,1):
            numlst = []
            for j in range(0,9,1):
                if (board[i][j] >= '1') & (board[i][j] <= '9'):
                    if board[i][j] in numlst:
                        return False
                        exit
                    else:
                        numlst.append(board[i][j])
        
        for j in range(0,9,1):
            numlst = []
            for i in range(0,9,1):
                if (board[i][j] >= '1') & (board[i][j] <= '9'):
                    if board[i][j] in numlst:
                        return False
                        exit
                    else:
                        numlst.append(board[i][j])

        for i in range(0,3,1):
            for j in range(0,3,1):
                numlst = []
                for row in range(i*3,i*3+3,1):
                    for col in range(j*3,j*3+3,1):
                        if (board[row][col] >= '1') & (board[row][col] <= '9'):
                            if board[row][col] in numlst:
                                return False
                                exit
                            else:
                                numlst.append(board[row][col])

        return True