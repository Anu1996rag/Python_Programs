# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:30:53 2020

@author: Gurudas

Tic-Tac-Toe 
"""
#the board structure dictionary

theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}

#printing the board

def printBoard(Board):
    print(Board['top-L'] + '|' + Board['top-M'] + '|' + Board['top-R'])
    print("-+-+-")
    print(Board['mid-L'] + '|' + Board['mid-M'] + '|' + Board['mid-R'])
    print("-+-+-")
    print(Board['low-L'] + '|' + Board['low-M'] + '|' + Board['low-R'])


#assigning the first value to the board
turn = 'X'

#repeat 9 times 
for i in range(9):
    printBoard(theBoard)
    print('Turn for '+ turn + '. Move on which space ?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

#printing thr board    
printBoard(theBoard)