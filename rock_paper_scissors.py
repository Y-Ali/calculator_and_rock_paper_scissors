import random

class Game():

    def __init__(self):
        self.player = True

    def computer_random(self):
        self.computer_choose = random.randint(1,3)
        print("computers move: ", self.computer_choose)

    def start_game(self):
        self.player_choose = int(input("please choose your move: 1,2 or 3 (rock, paper, scissors): "))
        #self.computer_random()

       # print(self.player)

        if self.player_choose == 1:
            print("You chose: Rock")
        elif self.player_choose == 2:
            print("You chose: Paper")
        else:
            print ("You chose: Scissors")


        while self.player == True:

            if self.computer_choose == self.player_choose:
                print("I'ts a Draw!")
                self.player = False

            elif self.computer_choose == 1 and self.player_choose == 2:
                print("You Win!")
                break

            elif self.computer_choose == 2 and self.player_choose == 1:
                print("You Win!")
                break

            elif self.computer_choose == 2 and self.player_choose == 3:
                print("You Win!")
                break

            elif self.computer_choose == 3 and self.player_choose == 2:
                print("You Lose!")
                break

            elif self.computer_choose == 2 and self.player_choose == 2:
                print("You Win!")
                break

    # def main(self):
    #     begin = input("Shall we begin...? y/n: ")
    #     if begin == "y":

new_game = Game()
new_game.computer_random()
new_game.start_game()
