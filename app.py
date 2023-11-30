from enum import Enum
import random

class Choice(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

DEFEATS = {
    Choice.ROCK: Choice.SCISSORS,
    Choice.PAPER: Choice.ROCK,
    Choice.SCISSORS: Choice.PAPER
}

class RockPaperScissors:
    def __init__(self):
        """
        Initializes the class instance.
        """
        self.user = None
        self.bot = None
        self.wins = 0
        self.rounds = 0


    def get_user_choice(self):
            """
            Prompts the user to enter their choice of rock, paper, or scissors.
            Returns the user's choice as a Choice object.
            """
            while True:
                user_input = input('Please enter your choice between rock, paper, or scissors: ').lower().strip()
                try:
                    user_choice = Choice(user_input)
                    print('You chose', user_choice.value)
                    return user_choice
                except ValueError:
                    print('Invalid choice! Please try again.')


    def get_bot_choice(self):
            """
            Returns the bot's choice for the game.
            
            Returns:
                Choice: The bot's choice for the game.
            """
            bot_choice = random.choice(list(Choice))
            print('Bot chose', bot_choice.value)
            return bot_choice


    def play_again(self):
        while True:
            play_again = input('Do you want to play again? (yes/no) ').lower().strip()
            if play_again == 'yes':
                return True
            elif play_again == 'no':
                return False
            else:
                print('Invalid input! Please enter yes or no.')


    def play(self):
            """
            Plays a round of the game and determines the winner.

            Returns:
                str: The result of the game (tie, win, or lose).
            """
            print('Welcome to Rock, Paper, Scissors!')
            while True:  # game loop
                self.user = self.get_user_choice()
                self.bot = self.get_bot_choice()
                self.rounds += 1
                if self.user == self.bot:
                    print('It\'s a tie!')
                elif DEFEATS[self.user] == self.bot:
                    print('You win!')
                    self.wins += 1
                else:
                    print('You lose!')
                print('You have won', self.wins, 'out of', self.rounds, 'rounds.')
                if not self.play_again():
                    print('Thanks for playing!')
                    break


game = RockPaperScissors()
result = game.play()
print(result)