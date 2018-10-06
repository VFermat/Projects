# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:03:46 2018

@author: Vitor Eller
"""

from copy import deepcopy

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
        
    def _get_win(self, board):
        winning = ['XX-', 'X-X', '-XX']
        columns = self._get_columns(board)
        rows = self._get_rows(board)
        diagonals = self._get_diagonals(board)
        win_moves = []
        for win in winning:
            if win in columns:
                c = columns.index(win)
                row = [char for char in columns[c]]
                r = row.index('-')
                win_moves.append([True, r, c])
            elif win in rows:
                r = rows.index(win)
                column = [char for char in rows[r]]
                c = column.index('-')
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
    
    def _get_block(self, board):
        loosing = ['OO-', 'O-O', '-OO']
        columns = self._get_columns(board)
        rows = self._get_rows(board)
        diagonals = self._get_diagonals(board)
        win_moves = []
        for loose in loosing:
            if loose in columns:
                c = columns.index(loose)
                row = [char for char in columns[c]]
                r = row.index('-')
                win_moves.append([True, r, c])
            elif loose in rows:
                r = rows.index(loose)
                column = [char for char in rows[r]]
                c = column.index('-')
                win_moves.append([True, r, c])
            elif loose in diagonals[0]:
                diagonal = [char for char in diagonals[0]]
                r = diagonal.index('-')
                win_moves.append([True, r, c])
            elif loose in diagonals[1]:
                diagonal = [char for char in diagonals[1]]
                r = diagonal.index('-')
                c = 2 - r
                win_moves.append([True, r, c])
        if len(win_moves) != 0:
            return win_moves
        return [False]
    
    def _get_fork(self):
        wins = self._get_win(self.board)
        for r in range(self.board):
            for c in range(3):
                if self.board[r][c] == '-':
                    new_board = deepcopy(self.board)
                    new_board[r][c] = 'X'
                    wins = self._get_win(board=new_board)
                    if len(wins) >= 2:
                        return [True, r, c]
        return [False]
    
    def _get_block_fork(self):
        wins = self._get_block(self.board)
        for r in range(len(self.board)):
            for c in range(3):
                if self.board[r][c] == '-':
                    new_board = deepcopy(self.board)
                    new_board[r][c] = 'O'
                    wins = self._get_block(board=new_board)
                    if len(wins) >= 2:
                        return [True, r, c]
        return [False]
    
    def _get_center(self):
        if self.board[1][1] == '-':
            return [True, 1, 1]
        return [False]
    
    def _get_opposite(self):
        corners_point = [[0, 0], [0, 2], [2, 0], [2, 2]]
        corners = self._check_corners()
        if 'O' not in corners:
            return [False]
        else:
            O_ind = corners.index('O')
            move_ind = 3 - O_ind
            return [True, corners_point[move_ind][0], corners_point[move_ind][1]]
        
    def _get_empty_corner(self):
        corners_point = [[0, 0], [0, 2], [2, 0], [2, 2]]
        corners = self._check_corners()
        if '-' not in corners:
            return [False]
        ind = corners.index('-')
        return [True, corners_point[ind][0], corners_point[ind][1]]
    
    def _get_empty_side(self):
        side_point = [[0, 1], [1, 0], [1, 2], [2, 1]]
        sides = self._check_sides()
        ind = sides.index('-')
        return [True, side_point[ind][0], side_point[ind][1]] 
        
    def _get_columns(self, board):
        column0 = board[0][0] + board[1][0] + board[2][0]
        column1 = board[0][1] + board[1][1] + board[2][1]
        column2 = board[0][2] + board[1][2] + board[2][2]
        columns = [column0, column1, column2]
        return columns
    
    def _get_rows(self, board):
        row0 = ''.join(board[0])
        row1 = ''.join(board[1])
        row2 = ''.join(board[2])
        rows = [row0, row1, row2]
        return rows
    
    def _get_diagonals(self, board):
        diagonal0 = board[0][0] + board[1][1] + board[2][2]
        diagonal1 = board[0][2] + board[1][1] + board[2][0]
        diagonals = [diagonal0, diagonal1]
        return diagonals
    
    def _check_corners(self):
        corner0 = self.board[0][0]
        corner1 = self.board[0][2]
        corner2 = self.board[2][0]
        corner3 = self.board[2][2]
        return [corner0, corner1, corner2, corner3]
    
    def _check_sides(self):
        side0 = self.board[0][1]
        side1 = self.board[1][0]
        side2 = self.board[1][2]
        side3 = self.board[2][0]
        return [side0, side1, side2, side3]
