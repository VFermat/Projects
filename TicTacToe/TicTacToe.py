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
        
    def _get_win(self, board=self.board):
        winning = ['XX-', 'X-X', '-XX']
        columns = self.__get_columns(board)
        rows = self.__get_rows(board)
        diagonals = self.__get_diagonals(board)
        win_moves []
        for win in winning:
            if win in columns:
                c = columns.index(win)
                rows = [char for char in columns[c]]
                r = rows.index('-')
                win_moves.append([True, r, c])
            elif win in rows:
                r = rows.index(win)
                columns = [char for char in rows[r]]
                c = columns.index('-')
                win_moves.append([True, r, c])
            elif win in diagonals[0]:
                diagonal = [char for char in diagonals[0]]
                r = diagonal.index('-')
                win_moves.append([True, r, r])
            elif win in diagonals[1]:
                diagonal = [char for char in diagonals[1]]
                r = diagonal.index('-')
                c = 2 - r
                win_moves.append([True, r, c])
        if len(win_moves) != 0:
            return win_moves
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
    
    def _get_fork(self):
        wins = self._get_win()
        
        
    def __get_columns(self, board):
        column0 = board[0][0] + board[1][0] + board[2][0]
        column1 = board[0][1] + board[1][1] + board[2][1]
        column2 = board[0][2] + board[1][2] + board[2][2]
        columns = [column0, column1, column2]
        return columns
    
    def __get_rows(self, board):
        row0 = ''.join(board[0])
        row1 = ''.join(board[1])
        row2 = ''.join(board[2])
        rows = [row0, row1, row2]
        return rows
    
    def __get_diagonals(self, board):
        diagonal0 = board[0][0] + board[1][1] + board[2][2]
        diagonal1 = board[0][2] + board[1][1] + board[2][0]
        diagonals = [diagonal0, diagonal1]
        return diagonals
    
        