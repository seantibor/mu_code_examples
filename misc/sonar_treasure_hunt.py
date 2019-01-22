# Sonar Treasure Hunt by Sean Tibor

import random
import sys
import math

board_width = 10
board_height = 10
num_chests = 3


def get_new_board(board_width=60, board_height=15):
    # creates a new board with the specified width and height
    board = []
    for x in range(board_width):  # the main list is a list of board_width lists
        board.append([])
        for y in range(board_height):  # each list in the main list has board_height number of single-character strings
            # Use different characters for the ocean to make it more readable
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board


def draw_board(board):
    # Draw the board data structure
    tensDigitsLine = '    '  # initial spacing for numbers on the left side of the board
    for i in range(1, len(board)):
        if i % 10 == 0:  # append the single digit for the tens part of the line
            tensDigitsLine += str(i // 10)
        else:
            tensDigitsLine += ' '  # otherwise just add a blank space

    widthDigitsLine = '   '
    for i in range(len(board)):
        widthDigitsLine += str(i % 10)  # append the digit for the ones part of the line

    # print the top x-axis label
    print(tensDigitsLine)
    print(widthDigitsLine)

    # print each of the rows
    for row in range(len(board[0])):
        # single digit numbers need to be indented with an extra space
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        board_row = ''
        for column in range(len(board)):
            board_row += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, board_row, row))

    # print the bottom x-axis label
    print(widthDigitsLine)
    print(tensDigitsLine)


def get_random_chests(board, num_chests=3):
    chests = []
    while len(chests) < num_chests:
        new_chest = [random.randint(0, len(board) - 1), random.randint(0, len(board[0]) - 1)]
        if new_chest not in chests:  # make sure chest is not already here
            chests.append(new_chest)

    return chests


def isOnBoard(x, y, board):
    return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])


def make_move(board, chests, x, y):
    # change the board structure with each guess
    # returns False if this is an invalid move
    # otherwise returns a string with the result of the move.

    smallest_distance = math.ceil(math.sqrt(len(board) ** 2 + len(board[0]) ** 2))

    for cx, cy in chests:
        distance = math.sqrt((cx - x) ** 2 + (cy - y) ** 2)
        if distance < smallest_distance:  # We want the closest chest
            smallest_distance = round(distance)

    if smallest_distance == 0:
        # xy is directly on a treasure chest
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return 'Treasure detected at a distance of %s from the sonar device.' % (smallest_distance)
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything. All treasure chests out of range'


def enter_player_move(previous_moves, board):
    # let the player enter their move. Return a two item list of int xy coordinates
    print('Where do you want to drop the next sonar device? (0-%i 0-%i) (or type quit)' % (len(board), len(board[0])))

    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1]), board):
            if [int(move[0]), int(move[1])] in previous_moves:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]

        print('Enter a number from 0 to %i, a space, then a number from 0 to %i.' % (len(board), len(board[0])))


def show_instructions():
    print('''Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current mission is to use sonar devices to find three sunken treasure chests at the bottom of the ocean. But you only have cheap sonar that finds distance, not direction.

Enter the coordinates to drop a sonar device. The ocean map will be marked with how far away the nearest chest is, or an X if it is beyond the sonar device's range. For example, the C marks are where chests are. The sonar device shows a 3 because the closest chest is 3 spaces away.

                    1         2         3
          012345678901234567890123456789012
        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
          012345678901234567890123456789012
                    1         2         3
(In the real game, the chests are not visible in the ocean.)
Press enter to continue...''')
    input()
    print('''When you drop a sonar device directly on a chest, you retrieve it and the other sonar devices update to show how far away the next nearest chest is. The chests are beyond the range of the sonar device on the left, so it shows an X.

                    1         2         3
          012345678901234567890123456789012
        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
          012345678901234567890123456789012
                    1         2         3
The treasure chests don't move around. Sonar devices can detect treasure chests up to a distance of 9 spaces. Try to collect all 3 chests before running out of sonar devices. Good luck!

Press enter to continue...''')
    input()


# Here is the main loop of the game
print('S O N A R')
print()
print('Would you like to view the instrctions? (yes/no)')
if input().lower().startswith('y'):
    show_instructions()

while True:
    # Game setup
    sonar_devices = 20
    the_board = get_new_board(board_width, board_height)
    the_chests = get_random_chests(the_board)
    draw_board(the_board)
    previous_moves = []

    while sonar_devices > 0:
        # Show sonar device and treasure chest status
        print('You have %s sonar device(s) left. %s treasure chest(s) remaining' % (sonar_devices, len(the_chests)))
        x, y = enter_player_move(previous_moves, the_board)
        previous_moves.append([x, y])  # we must track all moves so that sonar devices can be updated

        move_result = make_move(the_board, the_chests, x, y)
        if move_result == False:
            continue
        else:
            if move_result == 'You have found a sunken treasure chest!':
                # update all the sonar devices currently on the map
                for x, y in previous_moves:
                    make_move(the_board, the_chests, x, y)
            draw_board(the_board)
            print(move_result)
            if len(the_chests) == 0:
                print('You have found all the sunken treasure chests! Congratulations and good game!')
                break
            sonar_devices -= 1
    if sonar_devices == 0:
        print('''We\'ve run out of sonar devices! Now we have to turn the ship around and head for home with treasure chests still out there! Game over.
        
            The remaining chests were here:''')
        for x, y in the_chests:
            print('    %s, %s' % (x, y))
            the_board[x][y] = '*'
        draw_board(the_board)
    print('Do you want to play again? (yes/no)')
    if not input().lower().startswith('y'):
        sys.exit()
