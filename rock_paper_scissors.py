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
game_image = [rock,paper,scissors]
user_input = int(input("What do you choose ? Type 0 for rock, 1 for paper,2 for scissors\n"))
print(game_image[user_input])
computer_choice = random.randint(0, 2)
print("Computer_choice")
print(game_image[computer_choice])
if user_input >= 3 :
    print("invalid input")
elif user_input == 0 and computer_choice == 2 :
    print("you win!")
elif user_input == 2 and computer_choice == 0 :
    print("you loss!")
elif user_input > computer_choice :
    print("you loss!")
elif user_input < computer_choice :
    print("you win!")
elif user_input == computer_choice :
    print("It's draw!")