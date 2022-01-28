###Interactove Coding Exercise #1

# number = int(input("Which number do you want to check\n"))

# if (number % 2) == 0:
#     print("This is an even number")
# else: 
#     print("This is an odd number")


###Interactove Coding Exercise #2


# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# BMI = int(weight/(height ** 2))

# if BMI <= 18.5:
#     print(f"Your bim is {BMI}, you are unverweight")
# elif BMI <= 25:
#     print(f"Your bim is {BMI}, you have a normal weight")
# elif BMI <= 30:
#     print(f"Your bim is {BMI}, you are overweight")
# elif BMI <= 35:
#     print(f"Your bim is {BMI}, you are obese")
# else:
#     print(f"Your bim is {BMI}, you are clinically obese")


###Interactove Coding Exercise #3


# year = int(input("Which year do you want to check?\n"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


###Interactove Coding Exercise #4


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size.lower() == "s":
#     bill += 15
#     if add_pepperoni.lower() == "y":
#         bill += 2
#     if extra_cheese.lower() == "y":
#         bill +=1
# elif size.lower() == "m":
#     bill += 20
#     if add_pepperoni.lower() == "y":
#         bill += 3
#     if extra_cheese.lower() == "y":
#         bill +=1
# elif size.lower() == "l":
#     bill += 25
#     if add_pepperoni.lower() == "y":
#         bill += 3
#     if extra_cheese.lower() == "y":
#         bill +=1

# print(f"Your final bill is: ${bill}")


###Interactove Coding Exercise #5


# print('Welcome to the Love Calculator!')
# name1 = input("What is your name?\n").lower()
# name2 = input("What is their name?\n").lower()

# countT = name1.count('t') + name2.count('t')
# countR = name1.count('r') + name2.count('r')
# countU = name1.count('u') + name2.count('u')
# countE = name1.count('e') + name2.count('e')
# first_number = countT + countR + countU + countE

# countL = name1.count('l') + name2.count('l')
# countO = name1.count('o') + name2.count('o')
# countV = name1.count('v') + name2.count('v')
# countE = name1.count('e') + name2.count('e')
# second_number = countL + countO + countV + countE

# total_persent = int(str(first_number) + str(second_number))

# if total_persent <= 10 or total_persent >= 90:
#     print(f"Your score is {total_persent}, you do together like coke and mentos.")
# elif 40 <= total_persent >= 50:
#     print(f"Your score is {total_persent}, you are alright together.")
# else:
#     print(f"Your score is {total_persent}")


###Day 3 Project Treasure Island

# print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
# move1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
# if move1.lower() == 'left':
#     move2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
#     if move2.lower() == "wait":
#         move3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, on yellowm and one blue. Which colour do you choose?\n")
#         if move3.lower() == "yellow":
#             print("You Win!")
#         else:
#             print("Game Over.")
#     else:
#         print("Game Over.")
# else:
#     print("Game Over.")