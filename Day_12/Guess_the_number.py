import random
from art import logo

def game(num,chances):
	guess = 0
	for i in range(chances):
		guess = int(input("Guess a number: "))
		if guess == num:
			print(f"you WIN!🤩; you guessed the correct number")
			return 0
		elif guess < num:
			print(f"You guess low, chances remaining {chances-(i+1)}")
		else:
			print(f"You guess high, chances remaining {chances-(i+1)}")
	print(f"you LOST!😢. The number is {num}")


play = 'y'
while play != 'n':
	print(logo)
	mode = input("Choose a mode to play; 'easy' or 'hard': ")
	num = random.randint(1,100)
	chances = 0
	if mode == 'easy':
		chances = 10
		print(f"Number Generated between 1 to 100. You have {chances} chances to guess it")
		game(num,chances)
	else:
		chances = 5
		print(f"Number Generated between 1 to 100. You have {chances} chances to guess it")
		game(num,chances)
	play = input("Type 'y' to play again; 'n' to quit: ")
