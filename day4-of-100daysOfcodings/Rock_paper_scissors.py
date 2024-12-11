import random

try:
  
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and, 2 for Scissors: "))
  print("\n")
  
  computer_choice = random.randint(0, 2)
  
  def switch(s):
      if s == 0:
          return "Rock"
      elif s == 1:
          return "Paper"
      else:
          return "Scissors"
  
  computer_choice_zero_to_two = switch(computer_choice)
  print(f"Computer choose: {computer_choice_zero_to_two}")
  
  user_choice_zero_to_two = switch(user_choice)
  print(f"You choose: {user_choice_zero_to_two}")
  
  #computer choose rock > you  choose paper - you win
  if computer_choice == 0 and user_choice == 1:
      print("You win")
    
  #computer choose paper > you choose scissors - you win
  elif computer_choice == 1 and user_choice == 2:
      print("You Win!")
    
  #computer choose scissors > you choose rock - you win
  elif computer_choice == 2 and user_choice == 0:
      print("You Win!")
 
  elif computer_choice < user_choice:
      print("You lose!")
  else:
      print("It is a draw!")


except ValueError:
    print("You should use numerical (0 - 2) as input. ")
