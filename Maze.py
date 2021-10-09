from colorama import init
from random import randint
from playsound import playsound
from colorama import Fore, Style
import os
import msvcrt
import winsound

init()
__author__ = 'Maor Lahat'


# Functions for the progaram:
def check_momvemt(row, colomn, maze, movement):
    """
        This function updates where the player needs to go according to his choice of movement
        :param row: the current row
        :param colomn: the current colomn
        :param maze: the maze of the game with the current situation
        :param movement: the direction that the user wants to go
        False otherwise
        :type row: int
        :type colomn: int
        :type maze: list (of lists)
        :type movement: char
        :return: new place
        :rtype: list
    """
    new_place = [row, colomn, False]
    if movement == b'w':
        row = row - 1
    if movement == b's':
        row = row + 1
    if movement == b'd':
        colomn = colomn + 1
    if movement == b'a':
        colomn = colomn - 1
    if (maze[row][colomn] != '_' and maze[row][colomn] != '-' and maze[row][colomn] != '|'
            and maze[row][colomn] != '/' and maze[row][colomn] != '\\'):
        new_place[0] = row
        new_place[1] = colomn
    if maze[row][colomn] == '$':
        new_place[2] = True
    return new_place
    # ----------


def add_dollars(maze):
    """
        This function scatter four dollars ($) randomly in the maze
        :param maze: the maze of level 3
        :type maze: list (of lists)
        :return: maze_with_dollars
        :rtype: list (of lists)
    """
    maze_with_dollars = maze
    five_dollars = 1
    while five_dollars < 5:
        row = randint(1, 23)
        colomn = randint(1, 19)
        if (maze_with_dollars[row][colomn] != '_' and maze_with_dollars[row][colomn] != '-'
                and maze_with_dollars[row][colomn] != '|' and maze_with_dollars[row][colomn] != '$'
                and maze[row][colomn] != '/' and maze[row][colomn] != '\\' and maze[row][colomn] != '*'):
            five_dollars = five_dollars + 1
            maze[row][colomn] = '$'
    return maze
    # ----------


def dictionary_of_levels(level):
    """
        This function contains in a dictionary all the mazes that in the game, divided by keys
        :return: levels
        :rtype: dict
    """
    levels = {}
    levels[1] = [
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ['|', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', '-', '-', '-', '-', '-', '-', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '|', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|'],
        ['|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', '|', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', '|'],
        ['|', ' ', '|', '-', '-', '-', '-', ' ', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '-', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '-', '-', ' ', '-', '-', '-', ' ', '-', '-', '|'],
        ['|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'],
        ['|', '-', '-', '-', '-', '-', '-', ' ', '-', '-', '-', ' ', '-', '-', ' ', ' ', '|', '-', '-', '-', '|'],
        ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '-', '-', ' ', '|', ' ', '-', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '-', '-', ' ', '-', '|'],
        ['|', ' ', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|'],
        ['|', '-', ' ', '|', ' ', '|', '-', '-', '|', '-', '-', '-', '-', ' ', '-', ' ', '|', '-', '-', ' ', '|'],
        ['|', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '-', '-', '-', '-', '-', '-', '-', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', '|'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '|', ' ', '|', '-', ' ', '-', '-', '-', ' ', '-', '-', '-', ' ', '-', '-', '-', '-', '-', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', '-', '-', ' ', '-', ' ', ' ', '-', ' ', '-', ' ', '|', ' ', '-', '-', '-', '-', '-', '-', ' ', '|'],
        ['|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '|'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$', '|'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ]
    levels[2] = [
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-'],
        ['|', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', '|'],
        ['|', '-', '|', '-', '-', '-', '-', '-', '-', '-', '-', '|', ' ', '|', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '|', '_', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', '-', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', '-', ' ', '-', '-', '-', ' ',
         '-', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '|', '-', ' ', '-', '-', '|', ' ', '-', '-', '|', ' ', '|', ' ', '|', '-', '-', '-', ' ', '-', '-',
         '-', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '_', '-', ' ', '-', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', '-', ' ', '-', ' ', '|', ' ',
         ' ', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '-', '-', ' ', '-', '-', '-', '-', '-', '-', '-', '|', '-', '|', '-', '-', '-', '-', '-', '-',
         '-', '-', '|', '-', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|',
         ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', '-', '-', '-', ' ', '|', '-', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         '-', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', ' ', '-', '-', '-', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', '-', '-', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', '|', '-', '-', '-', '-', '-', '-', '-', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|',
         '-', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', '|', '$', '|'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-'],
    ]
    levels[3] = [
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-'],
        ['|', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', '|'],
        ['|', '-', '|', '-', '-', '-', '-', '-', '-', '-', '-', '|', ' ', '|', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '|', '_', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', '-', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', '-', ' ', '-', '-', '-', ' ',
         '-', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '|', '-', ' ', '-', '-', '|', ' ', '-', '-', '|', ' ', '|', ' ', '|', '-', '-', '-', ' ', '-', '-',
         '-', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '_', '-', ' ', '-', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', '-', ' ', '-', ' ', '|', ' ',
         ' ', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '-', '-', ' ', '-', '-', '-', '-', '-', '-', '-', '|', '-', '|', '-', '-', '-', '-', '-', '-',
         '-', '-', '|', '-', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|',
         ' ', ' ', ' ', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', '-', '-', '-', ' ', '|', '-', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         '-', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', ' ', '-', '-', '-', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|',
         ' ', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', '-', '-', ' ', '|', ' ', '|',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', '|', '-', '-', '-', '-', '-', '-', '-', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|',
         '-', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', '$', '|'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-'],
    ]
    levels[4] = [
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-'],
        ['|', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', '|'],
        ['|', '\\', ' ', ' ', '\\', ' ', ' ', '-', '-', ' ', '-', '-', ' ', '|', ' ', '|', '-', '-', '-', '-', ' ', ' ',
         '/', '-', '|', ' ', '|'],
        ['|', ' ', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', '/',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', '\\', ' ', ' ', '\\', '-', ' ', '-', '-', '-', '-', '-', ' ', '|', ' ', '|', ' ', '|', '/', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '/', ' ', ' ',
         ' ', '/', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '\\', ' ', ' ', '\\', ' ', '|', ' ', '|', '-', '|', '-', ' ', '|', '/', ' ', ' ', ' ',
         '/', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', '\\', ' ', ' ', '\\', '|', ' ', '|', ' ', '|', ' ', ' ', '/', ' ', ' ', ' ', '/',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', '\\', ' ', ' ', '\\', ' ', '|', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', '-', '\\', ' ', ' ', '\\', '|', ' ', '|', '/', ' ', ' ', ' ', '/', ' ', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '-', '-', '-', '|', ' ', ' ', ' ', '\\', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', ' ', '|', '-', '-', ' ', '-', '\\', ' ', ' ', ' ', ' ', ' ', ' ', '/', '|', '-', '-', ' ',
         '|', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '/', ' ', '|', ' ', '|', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '-', ' ', '|', ' ', '-', '-', '-', '-', '-', '\\', ' ', '-', '/', ' ', ' ', ' ', ' ', ' ', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', '-', ' ', '|', ' ', ' ', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '-', '|', '-', '-', '-', '-', '-', ' ', '|', '-', ' ', '|', ' ', ' ', '|', ' ', '-', '-',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', '-', '-', '-', ' ', '|', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '|', '-', ' ', '-', ' ', '-', '-', '-', '-', '-', '-', ' ', '-', '|', ' ', ' ', ' ', ' ', '|', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '-', ' ', '-', '-', '-', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ',
         '|', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', '|', ' ', '|', ' ', ' ', '-', '-', '-', ' ', '-', '-', '-',
         '|', ' ', ' ', ' ', '|'],
        ['|', ' ', '|', '-', '-', '-', ' ', '-', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ',
         '-', '-', '|', ' ', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '-', '|', ' ', '|', ' ', '|', ' ', ' ',
         ' ', ' ', '|', ' ', '|'],
        ['|', ' ', ' ', ' ', '|', '-', '-', '-', '-', '-', '-', '-', '|', ' ', ' ', '|', ' ', '|', ' ', '|', '-', '|',
         '-', ' ', '|', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '-', '-', '-', '-', '-', ' ', ' ', ' ', '|',
         ' ', ' ', '|', '-', '|'],
        ['|', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|',
         ' ', ' ', ' ', '$', '|'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-'],
    ]
    return levels[level]
    # ----------


def excute_the_movment(new_row, new_colomn, maze):
    """
        This function moves the '*' from is current place in the list of lists to is new place after the player choose
        is direction that he wants the '*' to move to
        :param new_row: the new row after the movment
        :param new_colomn: the new colomn after the movment
        :param maze: the former maze (before the movment), and returns it's after the place'*' updates in the maze
        :type new_row:  int
        :type new_colomn : int
        :type maze: list (of lists)
        :return: maze
        :rtype: list (of lists)
    """
    maze[new_row][new_colomn] = '*'
    return maze
    # ----------


def erase_the_previous(former_row, former_colomn, new_row, new_colomn, maze):
    """
        This function erase the '*' from is current place in the list of lists and put space instead
        :param former_row: the former row before the movment
        :param former_colomn: the former colomn before the movment
        :param new_row: the new row after the movment
        :param new_colomn: the new colomn after the movment
        :param maze: the former maze (before the movment), and returns it's after the '*' erase from is former place
        :type former_row: int
        :type former_colomn: int
        :type new_row:  int
        :type new_colomn : int
        :type maze: list (of lists)
        :return: maze
        :rtype: list (of lists)
    """
    if former_row != new_row or former_colomn != new_colomn:
        maze[former_row][former_colomn] = ' '
    return maze
    # ----------


def print_maze(current_maze, level):
    """
        :param current_maze: the maze that needs to be printed
        :param level: the level of the maze
        :type current_maze: list (of lists)
        :type level: int
        this function print the inserted maze and is level
        :return: None
    """
    if level == 5:
        level = level - 1
    print(Style.BRIGHT)
    print(Fore.CYAN + "LEVEL: " + str(level))
    print(Style.RESET_ALL, end="")
    print(Style.BRIGHT)
    for rows in current_maze:
        for in_rows in rows:
            if in_rows == '*':
                print(Fore.GREEN + in_rows + " ", end="")
            elif in_rows == '$':
                print(Fore.GREEN + in_rows + " ", end="")
            else:
                print(Fore.CYAN + in_rows, end=" ")
        print("")
    # -----------


def update_the_maze(former_row, former_colomn, new_row, new_colomn, maze):
    """
        This function erase the '*' from is current place and moves the '*' to is new place after the player choose is
        direction that he wants the '*' to move to
        :param former_row: the former row before the movment
        :param former_colomn: the former colomn before the movment
        :param new_row: the new row after the movment
        :param new_colomn: the new colomn after the movment
        :param maze: the former maze (before the movment)
        :type former_row: int
        :type former_colomn: int
        :type new_row:  int
        :type new_colomn : int
        :type maze: list (of lists)
        :return: new_maze
        :rtype: list (of lists)
    """
    new_maze = excute_the_movment(new_row, new_colomn, maze)
    new_maze = erase_the_previous(former_row, former_colomn, new_row, new_colomn, maze)
    return new_maze
    # ----------


def print_maze_structure():
    """
        this function prints the words "The Maze" with color (Red)
        :return: None
    """
    print(Style.BRIGHT)
    print(Fore.CYAN +
          """

                              _____ _           ___  ___              
                             |_   _| |          |  \\/  |              
                               | | | |__   ___  | .  . | __ _ _______ 
                               | | | '_ \\ / _ \\ | |\\/| |/ _` |_  / _ \\
                               | | | | | |  __/ | |  | | (_| |/ /  __/
                               \\_/ |_| |_|\\___| \\_|  |_/\\__,_/___\\___|
    """)
    print(Style.RESET_ALL, end="")

    # ----------


def print_you_won():
    """
        this function prints the words "You Win" with color (Yellow)
        :return: None
    """
    print(Style.BRIGHT)
    print(Fore.CYAN +
          """


                               __   __            _    _             
                               \\ \\ / /           | |  | |            
                                \\ V /___  _   _  | |  | | ___  _ __  
                                 \\ // _ \\| | | | | |/\\| |/ _ \\| '_ \\ 
                                 | | (_) | |_| | \\  /\\  / (_) | | | |
                                 \\_/\\___/ \\__,_|  \\/  \\/ \\___/|_| |_|
    """)
    print(Style.RESET_ALL, end="")


# ------------------------------------------

def main():
    winsound.PlaySound(r'C:\Users\Public\Spooky Scary Skeletons.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
    os.system('cls')
    MAX_LEVEL = 4
    level = 1
    maze = dictionary_of_levels(level)
    count_dollars = 1
    left = 6
    win = False
    row = 1
    colomn = 1
    print_maze_structure()
    print(Style.BRIGHT)
    print(Fore.CYAN + """
    The keys:
    w = up
    s = down
    d = right
    a = left
    PAY ATTENTION! At advanced levels you have to collect a few dollars scattered randomly in the maze
    """)
    print(Fore.GREEN + "Press enter to start")
    print(Style.RESET_ALL, end="")
    while level <= MAX_LEVEL:
        while not win:
            movment = msvcrt.getch()
            os.system('cls')
            update_movment = check_momvemt(row, colomn, maze, movment)
            maze = update_the_maze(row, colomn, update_movment[0], update_movment[1], maze)
            row = update_movment[0]
            colomn = update_movment[1]
            print_maze(maze, level)
            win = update_movment[2]
            if level >= 3 and count_dollars <= 5:
                if win:
                    count_dollars = count_dollars + 1
                if count_dollars <= 5:
                    win = False
                if count_dollars != 6:
                    left = 6 - count_dollars
                print(Style.BRIGHT)
                print(Fore.CYAN + str(left) + " more ", end="")
                print(Fore.GREEN + "$ ", end="")
                print(Fore.CYAN + "left to be found")
                print(Style.RESET_ALL, end="")
        winsound.PlaySound(None, winsound.SND_ASYNC)
        if level == 2:
            winsound.PlaySound(r'c:\Users\Public\The Ghost.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        elif level == 3:
            winsound.PlaySound(r'C:\Users\Public\Scary Hour.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        else:
            winsound.PlaySound(r'C:\Users\Public\HALLOWEEN THEME.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        count_dollars = 1
        left = 6
        level = level + 1
        row = 1
        colomn = 1
        if level <= MAX_LEVEL:
            maze = dictionary_of_levels(level)
        if MAX_LEVEL >= level >= 3:
            maze = add_dollars(maze)
            os.system('cls')
            print_maze(maze, level)
        if level < 3:
            os.system('cls')
            print_maze(maze, level)
        elif left != 6:
            os.system('cls')
            print_maze(maze, level)
            print(Style.BRIGHT)
            print(Fore.CYAN + str(left) + " more ", end="")
            print(Fore.GREEN + "$ ", end="")
            print(Fore.CYAN + "left to be found")
            print(Style.RESET_ALL, end="")
        win = False
    os.system('cls')
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound(r'C:\Users\Public\Congratulations (mp3cut.net).wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
    print_you_won()
    finish = "No"
    while finish != "":
        finish = input("")


if __name__ == "__main__":
    main()
