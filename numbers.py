import random;

class Numbers:
    def guess_numbers(self,no_of_allowed_guess,range_to_guess):
        number_to_guess = random.randint(0,range_to_guess)
        guess_times = 1
        name = input('Please enter your name: ')
        print(f'Please guess a number between 0 and {range_to_guess}')
        while guess_times <= no_of_allowed_guess:
            guess = input('> ')
            if guess.isdigit:
                guess = int(guess)
                if(guess == number_to_guess):
                    print(f'Congratulations {name}, {guess} is the correct answer')
                    break
                elif(guess < number_to_guess):
                    if guess_times != no_of_allowed_guess:
                        print('Too low, please try again')
                elif(guess > number_to_guess):
                    if guess_times != no_of_allowed_guess:
                        print('Too high, pleas try again')
                guess_times+=1
            else:
                print('Please enter a digit')
        else:
            print(f'Too bad {name}, you were unable to guess the right answer after {no_of_allowed_guess} guesses')

    def summing_numbers(self,*numbers):
        sum = 0
        try:
            for x in numbers:
                sum+=x
        except TypeError as identifier:
            print('All parameters must be a type number')
        print(sum)

test = Numbers();
#test.guess_numbers(3,10)
test.summing_numbers(1,2,3,4,5,6)
            