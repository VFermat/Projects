# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:03:46 2018

@author: Vitor Eller
"""

class TicTacToe:
    
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        
    def print_board(self):
        printable_board = []
        for r in self.board:
            printable_board.append('\t'.join(r))
        printable_board = '\n'.join(printable_board)
        return printable_board
        
    def _get_win(self):
        winning = ['XX-', 'X-X', '-XX']
        columns = self.__get_columns()
        rows = self.__get_rows()
        diagonals = self.__get_diagonals()
        for win in winning:
            if win in columns:
                c = columns.index(win)
                rows = [char for char in columns[c]]
                r = rows.index('-')
                return [True, r, c]
            elif win in rows:
                r = rows.index(win)
                columns = [char for char in rows[r]]
                c = columns.index('-')
                return [True, r, c]
            elif win in diagonals[0]:
                diagonal = [char for char in diagonals[0]]
                r = diagonal.index('-')
                return [True, r, r]
            elif win in diagonals[1]:
                diagonal = [char for char in diagonals[1]]
                r = diagonal.index('-')
                c = 2 - r
                return [True, r, c]
        return [False]
    
    def _get_block(self):
        loosing = ['OO-', 'O-O', '-OO']
        columns = self.__get_columns()
        rows = self.__get_rows()
        diagonals = self.__get_diagonals()
        for loose in loosing:
            if loose in columns:
                c = columns.index(loose)
                rows = [char for char in columns[c]]
                r = rows.index('-')
                return [True, r, c]
            elif loose in rows:
                r = rows.index(loose)
                columns = [char for char in rows[r]]
                c = columns.index('-')
                return [True, r, c]
            elif loose in diagonals[0]:
                diagonal = [char for char in diagonals[0]]
                r = diagonal.index('-')
                return [True, r, r]
            elif loose in diagonals[1]:
                diagonal = [char for char in diagonals[1]]
                r = diagonal.index('-')
                c = 2 - r
                return [True, r, c]
        return [False]
        
    def __get_columns(self):
        column0 = self.board[0][0] + self.board[1][0] + self.board[2][0]
        column1 = self.board[0][1] + self.board[1][1] + self.board[2][1]
        column2 = self.board[0][2] + self.board[1][2] + self.board[2][2]
        columns = [column0, column1, column2]
        return columns
    
    def __get_rows(self):
        row0 = ''.join(self.board[0])
        row1 = ''.join(self.board[1])
        row2 = ''.join(self.board[2])
        rows = [row0, row1, row2]
        return rows
    
    def __get_diagonals(self):
        diagonal0 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        diagonal1 = self.board[0][2] + self.board[1][1] + self.board[2][0]
        diagonals = [diagonal0, diagonal1]
        return diagonals
    
        