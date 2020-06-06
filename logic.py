from random import randint

# define selections in a tuple
options = ('Rock', 'Paper', 'Scissors', 'Double Scissors')


def computerChoice():
    ''' generate the computer's choice '''
    computer = options[randint(0, 3)]

    return computer


def play(computer, player):
    ''' if statement to determine the outcome '''

    if player == computer:
        result = 'Draw!'
    elif player == 'Rock' and computer == 'Paper':
        result = 'Computer wins!'
    elif player == 'Rock' and computer == 'Scissors':
        result = 'You win!'
    elif player == 'Rock' and computer == 'Double Scissors':
        result = 'You win!'
    elif player == 'Paper' and computer == 'Rock':
        result = 'You win!'
    elif player == 'Paper' and computer == 'Scissors':
        result = 'Computer wins!'
    elif player == 'Paper' and computer == 'Double Scissors':
        result = 'Computer wins!'
    elif player == 'Scissors' and computer == 'Rock':
        result = 'Computer wins!'
    elif player == 'Scissors' and computer == 'Paper':
        result = 'You win!'
    elif player == 'Scissors' and computer == 'Double Scissors':
        result = 'Computer wins!'
    elif player == 'Double Scissors' and computer == 'Rock':
        result = 'Computer wins!'
    elif player == 'Double Scissors' and computer == 'Paper':
        result = 'You win!'
    elif player == 'Double Scissors' and computer == 'Scissors':
        result = 'You win!'

    return result
