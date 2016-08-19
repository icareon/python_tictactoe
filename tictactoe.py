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
    board[position]=marker
    
def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or 
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark))

import random
def choose_first():
    playa=str(random.randint(1,2))
    return playa
    
def space_check(board,position):
    if board[position]==' ':
        return True
    else:
        return False

def full_board_check(board):
    for i in board:
        if board[i]==' ':
            return False
        else:
            return True
def player_choice(board):
    pos=raw_input('Which position do you want to play? (1-9)')
    if space_check(board,pos)==True:
        return pos
    elif space_check(board,pos)==False:
        return nan 
          
def replay():
    play_again=raw_input('Do you want to play again? (y/n)')
    if play_again=='y':
        return True
    elif play_again=='n':
        return False
    
print ('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_mark,player2_mark=player_input() 
    turn=choose_first()
    print ('Player '+turn+' goes first!')
    game_on=True
    
    while game_on:
        if turn=='1':
            #plauer 1 turn
            display_board(theBoard)
            pos=player_choice(theBoard)
            place_marker(thebBoard,player1_mark,pos)
            
            if win_check(theBoard,player1_mark)==True:
                print('You won!)
                game_on=False
                
            else:
                if full_board_check(theBoard)==False:
                    turn='2'
                elif full_board_check(theBoard)==True:
                    print ('The game is a draw')
                    break
        
        else:
            #player2 turn
                    
            
            
        
    place_marker(board,first,pos)


while replay==True:
    
        
