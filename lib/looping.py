#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count_down = 10
    while count_down > 0:
        print(count_down)
        count_down -= 1
    print("Happy New Year!")
# happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared_list = []
   
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list
# print(square_integers([2,6,7,9]))
    

def fizzbuzz():
    # code goes here!
    for numbers in range(1,101):
        if numbers % 3 ==0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0 and numbers % 5 != 0 :
            print("Fizz")
        elif numbers % 3 != 0 and numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)

# fizzbuzz()