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

my_choice = input("What is your choice (r)ock, (p)aper, or (s)cissors)? ")
computer = random.choice('rock', 'paper', 'scissors')
print(computer)
