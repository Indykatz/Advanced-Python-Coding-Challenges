# FizzBuzz
#  number / by 3 fizz
#  number / by 5 buzz
#  number / by 3 and 5 fizzbuzz

def fizzbuzz():
    for number in range(1, 101, 1):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizzbuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizzbuzz()