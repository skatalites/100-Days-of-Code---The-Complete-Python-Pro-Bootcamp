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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

match user_choice:
    case 0 | 1 | 2:
        print(game_images[user_choice])
        print("Computer chose:")
        print(game_images[computer_choice])

        match (user_choice, computer_choice):
            case (u, c) if u == c:
                print("It's a draw!")
            case (0, 2) | (1, 0) | (2, 1):
                print("You win!")
            case _:
                print("You lose!")
    case _:
        print("You typed an invalid number. You lose!")