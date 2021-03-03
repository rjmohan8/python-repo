from random import *


class Num_Guess():

    def __init__(self, number):
        self.number = number

    def generate_random_number(self):
        num = randint(1, self.number)
        return num

    def accept_input(self):
        val = int(input("Enter a number to guess: "))
        return val

    def give_clue(self, val):
        if val == num:
            print(f"Its a match. You have choosen the right number {num}")

        else:
            print("Please try again")

    if __init__ == main:
        generate_random_number()
        accept_input()
        give_clue()