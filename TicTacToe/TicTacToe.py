# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:03:46 2018

@author: Vitor Eller1
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
    
    def play(self):
        play_type = int(input('Wanna Start Playing?\n0 - Yes\n1 - No\n'))
        while play_type not in range(2):
            print('Please type a valid option!')
        if play_type == 1:
            self._c_play()
        else:
            self._p_play()
            
    def _p_play(self):
        winner = self._check_winner()
        com_move = 0
        p_move = 0
        print(self.print_board())
        while not winner[0]:
            r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
            while r_move not in range(3):
                print('Escolha Invalida!')
                r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
            c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
            while c_move not in range(3):
                print('Escolha Invalida!')
                c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
            while self.board[r_move][c_move] != '-':
                print('Favor Escolher uma Jogada Valida!')
                r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
                while r_move not in range(3):
                    print('Escolha Invalida!')
                    r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
                c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
                while c_move not in range(3):
                    print('Escolha Invalida!')
                    c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
            self.board[r_move][c_move] = 'O'
            p_move += 1
            print('Player Move: {}'.format(p_move))
            print('\n{}'.format(self.print_board()))
            winner = self._check_winner()
            if winner[0]:
                print(winner[1])
                print('WHAT THE HECK HAS JUST HAPPENED?')
            else:
                r_move, c_move = self._get_move()
                self.board[r_move][c_move] = 'X'
                com_move += 1
                print('Computer Move: {}'.format(com_move))
                print('Row: {}\nColumn: {}'.format(r_move + 1, c_move + 1))
                print('\n{}'.format(self.print_board()))
                winner = self._check_winner()
                if winner[0]:
                    print(winner[1])
                    print('Congrats, you lost to the computer!')
        self._reset_board()
            
    def _c_play(self):
        winner = self._check_winner()
        com_move = 0
        p_move = 0
        while not winner[0]:
            r_move, c_move = self._get_move()
            self.board[r_move][c_move] = 'X'
            com_move += 1
            print('Computer Move: {}'.format(com_move))
            print('Row: {}\nColumn: {}'.format(r_move + 1, c_move + 1))
            print('\n{}'.format(self.print_board()))
            winner = self._check_winner()
            if winner[0]:
                print(winner[1])
                print('Congrats, you lost to the computer!')
            else:
                r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
                while r_move not in range(3):
                    print('Escolha Invalida!')
                    r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
                c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
                while c_move not in range(3):
                    print('Escolha Invalida!')
                    c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
                while self.board[r_move][c_move] != '-':
                    print('Favor Escolher uma Jogada Valida!')
                    r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
                    while r_move not in range(3):
                        print('Escolha Invalida!')
                        r_move = int(input('Qual Linha quer Jogar? 1, 2 ou 3?')) - 1
                    c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
                    while c_move not in range(3):
                        print('Escolha Invalida!')
                        c_move = int(input('Qual Coluna Deseja Jogar? 1, 2 ou 3?')) - 1
                self.board[r_move][c_move] = 'O'
                p_move += 1
                print('Player Move: {}'.format(p_move))
                print('\n{}'.format(self.print_board()))
                winner = self._check_winner()
                if winner[0]:
                    print(winner[1])
                    print('WHAT THE HECK HAS JUST HAPPENED?')
        self._reset_board()
            
    def _get_move(self):
        get_win = self._get_win(self.board)
        if get_win[0] != False:
            return get_win[0][1:]
        get_block = self._get_block(self.board)
        if get_block[0] != False:
            return get_block[0][1:]
        get_fork = self._get_fork()
        if get_fork[0]:
            return get_fork[1:]
        get_block_fork = self._get_block_fork()
        if get_block_fork[0]:
            return get_block_fork[1:]
        get_center = self._get_center()
        if get_center[0]:
            return get_center[1:]
        get_opposite = self._get_opposite()
        if get_opposite[0]:
            return get_opposite[1:]
        get_empty_side = self._get_empty_side()
        if get_empty_side[0]:
            return get_empty_side[1:]
        get_empty_corner = self._get_empty_corner()
        if get_empty_corner[0]:
            return get_empty_corner[1:]
        
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
                win_moves.append([True, r, r])
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
        for r in range(len(self.board)):
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
            if self.board[corners_point[move_ind][0]][corners_point[move_ind][1]] == '-':
                return [True, corners_point[move_ind][0], corners_point[move_ind][1]]
        return [False]
        
    def _get_empty_side(self):
        side_point = [[0, 1], [1, 0], [1, 2], [2, 1]]
        sides = self._check_sides()
        ind = sides.index('-')
        return [True, side_point[ind][0], side_point[ind][1]] 
    
    def _get_empty_corner(self):
        corners_point = [[0, 0], [0, 2], [2, 0], [2, 2]]
        corners = self._check_corners()
        if '-' not in corners:
            return [False]
        ind = corners.index('-')
        return [True, corners_point[ind][0], corners_point[ind][1]]

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
        side3 = self.board[2][1]
        return [side0, side1, side2, side3]
    
    def _check_winner(self):
        win = 'XXX'
        loose = 'OOO'
        columns = self._get_columns(self.board)
        rows = self._get_rows(self.board)
        diagonals = self._get_diagonals(self.board)
        if win in columns or win in rows or win in diagonals:
            return [True, 'Computer Wins']
        elif loose in columns or loose in rows or loose in diagonals:
            return [True, 'Player Wins']
        elif self._get_tie():
            return [True, 'It\'s a Tie']
        return [False]
    
    def _get_tie(self):
        moves = []
        for r in self.board:
            for c in r:
                moves.append(c)
        if '-' in moves:
            return False
        return True
    
    def _reset_board(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    @staticmethod
    def _get_columns(board):
        column0 = board[0][0] + board[1][0] + board[2][0]
        column1 = board[0][1] + board[1][1] + board[2][1]
        column2 = board[0][2] + board[1][2] + board[2][2]
        columns = [column0, column1, column2]
        return columns

    @staticmethod
    def _get_rows(board):
        row0 = ''.join(board[0])
        row1 = ''.join(board[1])
        row2 = ''.join(board[2])
        rows = [row0, row1, row2]
        return rows

    @staticmethod
    def _get_diagonals(board):
        diagonal0 = board[0][0] + board[1][1] + board[2][2]
        diagonal1 = board[0][2] + board[1][1] + board[2][0]
        diagonals = [diagonal0, diagonal1]
        return diagonals


game = TicTacToe()


game.play()
