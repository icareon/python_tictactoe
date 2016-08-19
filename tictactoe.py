# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 09:08:44 2016

@author: shahidi
"""

from __future__ import print_function
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
    
def player_input():
    marker=''
    while not (marker =='X' or marker=='O'):
        marker=raw_input('Player 1: Do you want to be X or O?').upper()
         
    if marker=='X':
        return ('X','O')
    elif marker=='O':
        return ('O','X')
         
def place_marker(board,marker,position):
    board[position-1]=marker[0]
    
def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or 
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark))
   
theBoard = [' '] * 10
display_board(theBoard)