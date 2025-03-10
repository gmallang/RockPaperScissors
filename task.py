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

print("Welcome to rock, paper, scissors! You will play against the computer.")
user = int(input("Choose 0 for rock, 1 for scissor, and 2 for paper. \n"))
comp = random.randint(0,2)


if user == 0 and comp == 0:
    print("User chose\n" + rock)
    print("Computer choose\n" + rock)
    print("It was a draw")
elif user == 1 and comp == 1:
    print("User chose\n" + paper)
    print("Computer choose\n" + paper)
    print("It was a draw")
elif user == 2 and comp == 2:
    print("User chose\n" + scissors)
    print("Computer choose\n" + scissors)
    print("It was a draw")
elif user == 0 and comp == 2:
    print("User chose\n" + rock)
    print("Computer choose\n" + scissors)
    print("You win")
elif user == 1 and comp == 0:
    print("User chose\n" + paper)
    print("Computer choose\n" + rock)
    print("You win")
elif user == 2 and comp == 1:
    print("user chose \n" + scissors)
    print("Computer choose\n" + paper)
    print("You win")
elif user == 1 and comp == 2:
    print("User chose\n" + paper)
    print("Computer chose\n" + scissors)
    print("You lose")
elif user == 0 and comp == 1:
    print("User chose\n" + rock)
    print("Computer chose\n" + paper)
    print("You lose")
elif user == 2 and comp == 0:
    print("User chose\n" + scissors)
    print("Computer chose\n" + rock)
    print("You lose")
else:
    print("Invalid")
