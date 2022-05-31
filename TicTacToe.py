# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:49:29 2021

@author: assar
"""
import numpy as np
import random
import matplotlib.pyplot as plt

def new_board(size):
    """ Creates an empty board """
    board = [[0 for x in range(size)] for y in range(size)]
    return board

def search_empty_positions(board):
    list_of_empty_positions = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                list_of_empty_positions.append((row, col))
    return list_of_empty_positions

def place_random_marker(board, player):
    empty_positions = search_empty_positions(board)
    chosen_position = random.choice(empty_positions)
    board[chosen_position[0]][chosen_position[1]] = player
    return board, chosen_position

def analyze_board_win(board, chosen_position, player):
    winner, row, col, board_size  = 0, chosen_position[0], chosen_position[1], len(board) 
    
    if row - 2 >= 0: # N-N
        N_N = (board[row-1][col], board[row-2][col])
        if N_N == (player, player):
            winner = player
            return winner
    if row - 2 >= 0 and col + 2 < board_size: # NE-NE
        NE_NE = (board[row-1][col+1], board[row-2][col+2])
        if NE_NE == (player, player):
            winner = player
            return winner
    if col + 2 < board_size: # E-E
        E_E = (board[row][col+1], board[row][col+2])
        if E_E == (player, player):
            winner = player
            return winner
    if row + 2 < board_size and col + 2 < board_size: # SE-SE
        SE_SE = (board[row+1][col+1], board[row+2][col+2])
        if SE_SE == (player, player):
            winner = player
            return winner
    if row + 2 < board_size: # S-S
        S_S = (board[row+1][col], board[row+2][col])
        if S_S == (player, player):
            winner = player
            return winner
    if row + 2 < board_size and col - 2 >= 0: #SW-SW
        SW_SW = (board[row+1][col-1], board[row+2][col-2])
        if SW_SW == (player, player):
            winner = player
            return winner
    if col - 2 >= 0: #W-W
        W_W = (board[row][col-1], board[row][col-2])
        if W_W == (player, player):
            winner = player
            return winner
    if row - 2 >= 0 and col - 2 >= 0: #NW-NW
        NW_NW = (board[row-1][col-1], board[row-2][col-2])
        if NW_NW == (player, player):
            winner = player
            return winner
    if row - 1 >= 0 and row + 1 < board_size: #N-S
        N_S = (board[row-1][col], board[row+1][col])
        if N_S == (player, player):
            winner = player
            return winner
    if row - 1 >= 0 and col + 1 < board_size and row + 1 < board_size and col - 1 >= 0: #NE-SW
        NE_SW = (board[row-1][col+1], board[row+1][col-1])
        if NE_SW == (player, player):
            winner = player
            return winner
    if col + 1 < board_size and col - 1 >= 0: # E-W
        E_W = (board[row][col+1], board[row][col-1])
        if E_W == (player, player):
            winner = player
            return winner
    if row - 1 >= 0 and row + 1 < board_size and col - 1 >= 0 and col + 1 < board_size: #SE-NW
        SE_NW = (board[row+1][col+1], board[row-1][col-1])
        if SE_NW == (player, player):
            winner = player
            return winner

    if search_empty_positions(list(board)) == [] and winner == 0: # Draw
        winner = 3
    return winner

def show_result(size, number_of_games, player_1_wins, player_2_wins, draws):

    x = ["Spelare 1", "Spelare 2", "Oavgjort"]
    y = [player_1_wins, player_2_wins, draws]

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, y)
    plt.ylabel("Antalet vinster")
    plt.title("Utfall tre-i-rad " + str(size) + "x" + str(size) + " bräde, " + str(number_of_games) + "st rundor.")

    plt.xticks(x_pos, x)
    plt.savefig("utfall.pdf")

    print("Spelare 1 vinster: ", player_1_wins, "\nSpelare 2 vinster: ",
          player_2_wins, "\nOavgjort: ", draws)

def main():
    print("Programmet startar...")
    print("Detta program simulerar uprepade partier av tre-i-rad")
    
    size = int(input("Hur stort bräde(3/5/7)?" + "\n" + ": "))
    
    number_of_games = int(
        input("Hur många partier vill du simulera?" + "\n" + ": "))

    print("Scenario 1: Alla drag slumpas ut." + "\n"
          + "Scenario 2: Spelare 1 sätter första markören i mitten. " + "\n" + "Alla andra drag slumpas ut.")

    scenario = int(input("Vilket scenario vill du spela?" + "\n" + ": "))

    count, player_1_wins, player_2_wins, draws = 0, 0, 0, 0

    while count < number_of_games:
        board, winner, first_move = new_board(size), 0, 0
        while winner == 0:
            for player in [1, 2]:
                if scenario == 2 and first_move == 0:
                    board[int(len(board)/2)][int(len(board)/2)] = 1
                    first_move = 1
                    continue

                (board, chosen_position) = place_random_marker(board, player)
                winner = analyze_board_win(board, chosen_position, player)

                if winner == 1:
                    count += 1
                    player_1_wins += 1

                if winner == 2:
                    count += 1
                    player_2_wins += 1

                if winner == 3:
                    count += 1
                    draws += 1
                    
                if winner != 0:
                    break

    return show_result(size, number_of_games, player_1_wins, player_2_wins, draws)

if __name__ == '__main__':
    main()
