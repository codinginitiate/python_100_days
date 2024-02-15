import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
set = [rock, paper, scissors]
input = input("What is your choice rock, paper, or scissors)? ")
print(set[])
set = [rock, paper, scissors]
computer = random.choice(set)
print(type(computer))

