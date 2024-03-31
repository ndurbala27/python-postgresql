#lists in python
#numbers = [9,8,7,6,5,4,3,2,1,0]
#print(numbers)
#print(len(numbers))
#print(numbers[9])

#list index out of range
#print(numbers[len(numbers)])

#print(numbers[len(numbers)-1])

#for number in numbers:
    #print(number)

#for number in numbers:
    #print(number**2)

#boolean expressions, true and false
#greater_than_three = 5 > 3
#print(greater_than_three)

#equal_to_five = 5 == 5
#print(equal_to_five)

#for number in numbers:
#    print(number > 5)

#if statements
#if 5 > 3:
    #print("Five is greater than three!")

#if 3 > 5:
    #print("This will not print")

#for number in numbers:
#    if number > 5:
#        print("{} is greater than 5.".format(number))

#the 'in' and 'not' keyword to check whether a list contains an element
#print(10 not in numbers)

#if not 3 > 5:
#    print("this is weird")

""" magic_numbers = [3,9]
user_number = 3

if user_number in magic_numbers:
    print("You go it right")

if user_number not in magic_numbers:
    print("You go it wrong") """

# giving the user multiple chances in this program
# magic_numbers = [3,9]
# chances = 3


# for attempt in range(chances): #range(changes is [0,1,2])
#     print("This is attempt {}.".format(attempt+1))
#     user_number = int(input("Enter a number between 0 and 9: "))
#     if user_number in magic_numbers:
#         print("You go it right")
#     if user_number not in magic_numbers:
#         print("You go it wrong")

# generating random numbers, like a slot machine in a casino
import random

magic_numbers = [random.randint(0,9) , random.randint(0,9)]

# minimum = 100

# for i in range(10):
#     random_number = random.randint(0,100)
#     print("The number generated is {}".format(random_number))
#     if random_number <= minimum:
#         minimum = random_number

# print("The minimum number was {}.".format(minimum))

# defining my own methods, asking for user input, and method returns
def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return "You go it right"
    if user_number not in magic_numbers:
        return "You go it wrong"


def run_program_x_times(chances):
    for attempt in range(chances): #range(changes is [0,1,2])
        print("This is attempt {}.".format(attempt+1))
        print(ask_user_and_check_number())

def check_user_input():
    user_attempts = int(input("How many times do you want the program to run? "))
    if int(user_attempts):
        return user_attempts
    if not int(user_attempts):
        print("Enter a number")

run_program_x_times(check_user_input)