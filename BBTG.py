#variable to identify winner
import random
winner = ''

#rand function to choose one of three numbers and idnetify the assigned value
random_choice = random.randint(0,2)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# User Choice- check validity
user_choice = ''

while (user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors'):
    user_choice = input('rock, paper, or scissors? ')

#Choose the winner
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

if winner == 'Tie':
    print('We both choose', computer_choice, ', play again.')
else:
    print(winner, 'won. The computer chose', computer_choice, '.')
