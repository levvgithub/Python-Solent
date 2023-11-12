print("What is your name?")
name = input()

print("How old are you?")
age = int(input())

print("How tall are you?")
height = float(input())

print("Your weight?")
weight = float(input())

bmi = weight / (height ** 2)
print(f"{name}, you are {age} years old, and your BMI is {bmi:.2f}")