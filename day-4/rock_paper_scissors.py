rock_art = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

images = [rock_art, paper_art, scissors_art]
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f'Computer chose {images[computer_choice]}')
print(f"You chose {images[user_choice]}")
if computer_choice == user_choice:
    print("It's a Tie!")

elif computer_choice == 0:
    if user_choice == 1:
        print("You Win, paper beats rock")
    elif user_choice == 2:
        print("You lose, rock beats scissors")

elif computer_choice == 1:
    if user_choice == 0:
        print('You lose, paper beats rock')
    elif user_choice == 2:
        print('You Win!, scissors beats paper')

elif computer_choice == 2:
    if user_choice == 0:
        print('You Win, rock beats scissors')
    elif user_choice == 1:
        print('You lose, scissors beats paper')

    