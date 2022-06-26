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
import random
# 0 -rock
# 1 - paper
# 2 - scissors

ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
com = random.randint(0,2)
sign = [rock,paper,scissors]

print(f"you chose:\n{sign[ch]}\ncomp chose{sign[com]}\n")

if ch == com:
  print('Its a DRAW')
elif (ch==0 and com == 2) or (ch==1 and com == 0) or (ch==2 and com == 1):
  print('You WIN')
else:
  print('Comp WIN')
  
