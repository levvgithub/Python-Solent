def get_ascii():
  print("Program started")
  print("Please enter a standard character:")
  ascii_char = input()
  value = ord(ascii_char)
  letter = len(ascii_char)
  if letter == 1:
    print(f"The ASCII code for {ascii_char} is {value}")
  else:
    print("Error")
  print("Program ended!")

get_ascii()

def guess_the_number():
  import random as rnd
  print("Please enter the minimum value:")
  min = int(input())
  print("Please enter the maximum value:")
  max = int(input())
  number = rnd.randrange(min,max)
  print(f"I am thinking of a number between {min} and {max}. Can you guess what it is?")
  guess = int(input())
  i = 1
  while (i < number):
    if guess > number:
      print("Your guess is too high. Try again!")
      guess = int(input())
    elif guess < number:
      print("Your guess is too low. Try again!")
      guess = int(input())
    else:
      print("Congratulations! You guessed my number!")
      break
  
guess_the_number()

def listen():
  print("What sound did I hear?")
  sound = str(input())
  print(f"That was a loud {sound}!")

listen()