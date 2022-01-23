###Interactove Coding Exercise #1

# number = input("Type a two digit number: ")

# numberFirst = int(number[0])
# numberSecond = int(number[1])

# print(numberFirst + numberSecond)


###Interactove Coding Exercise #2

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# BMI = int(weight/(height ** 2))

# print(BMI)


###Interactove Coding Exercise #3

# age = input("What is your current age? ")

# yearsLeft = 90 - int(age)
# monthsLeft = yearsLeft*12
# weeksLeft = yearsLeft*52
# daysLeft = yearsLeft*365

# print(f"You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left.")


###Day 2 Project Tip Calculator

# total = float(input("What was the total bill? $"))
# tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
# count_people = int(input("How many people to split the bill? "))

# one_person = round((total * (1 + tip_percent/100))/count_people, 2)

# print(f"Each person should pay: ${one_person}")