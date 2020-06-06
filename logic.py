from random import randint

# define selections in a tuple
options = ('rock', 'paper', 'scissors', 'double scissors')


def computerChoice():
    ''' generate the computer's choice '''
    computer = options[randint(0, 3)]

    return computer


def play(computer, player):
    ''' if statement to determine the outcome '''

    if player == computer:
        result = 'Draw!'
    elif player == 'rock' and computer == 'paper':
        result = 'Computer wins!'
    elif player == 'rock' and computer == 'scissors':
        result = 'You win!'
    elif player == 'rock' and computer == 'double scissors':
        result = 'You win!'
    elif player == 'paper' and computer == 'rock':
        result = 'You win!'
    elif player == 'paper' and computer == 'scissors':
        result = 'Computer wins!'
    elif player == 'paper' and computer == 'double scissors':
        result = 'Computer wins!'
    elif player == 'scissors' and computer == 'rock':
        result = 'Computer wins!'
    elif player == 'scissors' and computer == 'paper':
        result = 'You win!'
    elif player == 'scissors' and computer == 'double scissors':
        result = 'Computer wins!'
    elif player == 'double scissors' and computer == 'rock':
        result = 'Computer wins!'
    elif player == 'double scissors' and computer == 'paper':
        result = 'You win!'
    elif player == 'double scissors' and computer == 'scissors':
        result = 'Computer wins!'

    return result
