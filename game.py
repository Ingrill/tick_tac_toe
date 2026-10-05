import time
import math
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #board as a list
        self.current_winner = None #Keep track of winner

    def print_board(self):
        #function to print a board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #function to print a board with square numbers
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        #check what moves are available to player
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        #check if there are empty squares on board
        return ' ' in self.board

    def num_empty_squares(self):
        #check how many empty squares there are
        return self.board.count(' ')

    def make_move(self, square, letter):
        #making a move amd checking if there is a winner
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #check if there is a winner

        #check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]

        if all([s == letter for s in row]):
            return True

        #check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]

        if all([s == letter for s in column]):
            return True
        
        #check the diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False


def choose_game_type():
    #function to choose game type
    valid_type = False
    while not valid_type:
        try:
            game_type = int(input('Chose game type:\n1.Computer vs You\n2.Computer vs Computer\n'))
            if not game_type:
                raise ValueError
            valid_type = True
        except ValueError:
            print('Choose 1 or 2')
    time.sleep(.5)
    if game_type == 1:
        print('You chose to play against computer')
    else:
        print('You chose to watch 2 idiots battle against each other')
    time.sleep(.5)
    return game_type


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    game_type = choose_game_type()

    if game_type == 1:
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player, print_game = True)
    else:
        x_player = RandomComputerPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player, print_game = True)