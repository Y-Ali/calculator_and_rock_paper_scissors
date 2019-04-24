import random

class Rpc_game():
    def __init__(self):
        self.player_input = "nothing"
        self.computer_input = "nothing"

    #get user input
    def get_user_input(self):
        user_input = input("Enter rock, paper or scissors: ")

        self.player_input = user_input.strip().lower()

    #get computer input
    def generate_random_computer_input(self):
        options = ["rock", "paper", "scissors"]
        random_integer = random.randint(0,2)
        #print(random_integer)

        self.computer_input = options[random_integer]

        #print(self.computer_input)

    def game_result_comparison(self):
        if self.player_input == self.computer_input:
            return "Draw"
        elif self.player_input == "rock" and self.computer_input == "paper":
            return "You Lose"
        elif self.player_input == "rock" and self.computer_input == "scissors":
            return "You Win"
        elif self.player_input == "paper" and self.computer_input == "rock":
            return "You Win"
        elif self.player_input == "paper" and self.computer_input == "scissors":
            return "You Lose"
        elif self.player_input == "scissors" and self.computer_input == "rock":
            return "You Lose"
        elif self.player_input == "scissors" and self.computer_input == "paper":
            return "You Win"

    def run_game(self):
        while True:
            self.get_user_input()
            self.generate_random_computer_input()
            print("you chose", self.player_input)
            print("computer chose", self.computer_input)
            print(self.game_result_comparison())

            player_option = input("play game?: y/n")
            if player_option == "n":
                print("Goodbye...!")
                break


game = Rpc_game()
game.run_game()
#
# print("you chose", game.player_input)
# print("computer chose",game.computer_input)
# game.game_result_comparison()
