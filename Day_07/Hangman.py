import random
from hangman_art import stages,logo
from  hangman_words import word_list
#from replit import clear
import string

print(logo)
word = random.choice(word_list)
key = ['_']*len(word)

alphabet_string = string.ascii_lowercase
alphabets = list(alphabet_string)

game_over = False
lives = 7
hearts = "\u2764\uFE0F "*7
hearts_count=0

while not game_over:

  print(f"\n.....................................................\n")
  print(f"{' '.join(key)}, total lifes: {hearts[hearts_count:]}")
  print("letters available\t","".join(alphabets))
  user_input = input("Enter your guess letter:\t").lower()
  pos = 0

  if user_input in key:
    print("Letter Already found. Please try new letters")
  elif user_input not in alphabets:
    print("Letter Already tried and you lost life. Please try new letters")

    #reducing lives for the user input not found in the word
  elif user_input not in word:
    alphabets[alphabets.index(user_input)] = '_'
    print(f"'{user_input}' NOT FOUND")
    print(f"Life lost - 💔")
    lives -= 1
    hearts_count += 3
    print(stages[lives])
  else:
    #finding the user input in the word
    for i in word:
      if user_input == i:
        alphabets[alphabets.index(i)] = '_'
        key[pos]=i
        print(f"'{user_input}' FOUND:\t{' '.join(key)}")
             
      pos+=1  

  #game over check conditions (loop out conditions)
  if '_' not in key:
    game_over = True
    print("you WON")
  if lives == 0:
    game_over = True
    print("you LOST; Person Hanged")

print(f"\nthe answer is: {word}")
