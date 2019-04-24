class calculator():
    def __init__(self):
        self.user_input1 = 0
        self.user_input2 = 0
        self.calc_total = 0
        self.running = True

    def ask_user_input(self):
        user_input_1 = int(input('Enter a number: '))
        self.input1 = user_input_1

        user_input_2 = int(input('Enter a number: '))
        self.input2 = user_input_2

    def multiplication(self):
        m = self.calc_total = self.input1 * self.input2
        return ("Multiplication result: ", m)

    def addition(self):
        a = self.calc_total = self.input1 + self.input2
        return ("Addition result: ", a)

    def subtraction(self):
        s = self.calc_total = self.input1 - self.input2
        return ("Subtraction result: ", s)

    def division(self):
        d = self.calc_total = self.input1 / self.input2
        return ("Division result: ", d)

    def main(self):
        while self.running == True:
            self.ask_user_input()

            print(self.multiplication())

            print(self.addition())

            print(self.subtraction())

            print(self.division())

            self.calculate_again()

    def calculate_again(self):
        again = input("y/n: ")
        if again == "y":
            self.main()
        elif again =="n":
            print("goodbye...")


play = calculator()
play.main()



#play.user_input1   #check input
#play.user_input2   #check input