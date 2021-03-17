import random


class Num_Guess():
    attempts = 1

    # def __init__(self):

    def accept_upper(self):
        upper = int(input('Enter the upper bound to start the game: '))
        return upper

    def randnum_gen(self, upper):
        randnum = random.randint(1, upper)
        return randnum

    def accept_guess(self, upper):
        self.guess = int(input('Enter a value from 1 to {} including'.format(upper)))
        # print("guess is {}".format(self.guess))
        return self.guess

    def guess_check(self, randnum, upper):
        print(self.guess)
        if self.guess == randnum:
            print("Perfect Guess and it took {} attempts".format(Num_Guess.attempts))

        else:
            print("Wrong Guess!")
            Num_Guess.attempts += 1
            self.accept_guess(upper)


mynumguess = Num_Guess()

upper = mynumguess.accept_upper()

randnum = mynumguess.randnum_gen(upper)

guess = mynumguess.accept_guess(upper)

mynumguess.guess_check(randnum,upper)