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
my_choice = input("What is your choice (1)rock , (2)paper, or (3)scissors? Enter a number: ")
# print my choice as graphic
print("\nYou chose:")
print(set[int(my_choice)-1])
# print computer random choice as graphic
print("Computer chose:")
computer = random.choice(set)
print(computer)
# print outcome win, lose, tie
if set[int(my_choice)-1] == rock and computer == scissors:
    print("YOU WIN!")
elif set[int(my_choice)-1] == scissors and computer == paper:
    print("YOU WIN!")
elif set[int(my_choice)-1] == paper and computer == rock:
    print("YOU WIN!")
elif set[int(my_choice)-1] == computer:
    print("It's a tie.")
else:
    print("Sorry, You lose.")
