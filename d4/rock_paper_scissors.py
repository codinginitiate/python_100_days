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
if my_choice == 'r':
    print(rock)
elif my_choice == 'p':
    print(paper)
elif my_choice == 's':
    print(scissors)
set = ['r', 'p', 's']
computer = random.choice(set)
if computer == 'r':
    print(rock)
elif computer == 'p':
    print(paper)
elif computer == 's':
    print(scissors)

