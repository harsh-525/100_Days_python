import random
from art import logo,vs
from game_data import data

loose = False
score = 0
print(logo)


def higher(a_pos,score,loose):
	if loose:
		print(f"Sorry! that was wrong. the final score is {score}")
		return
	else:
		b_pos = random.randint(0,len(data)-1)
		if b_pos == a_pos:
			return higher(a_pos,score,loose)

	print("-------------------------------------------------------")
	print(f"Compare A:\t{data[a_pos]['name']}, {data[a_pos]['description']}, {data[a_pos]['country']}")
	print(vs)
	print(f"Compare B:\t{data[b_pos]['name']}, {data[b_pos]['description']}, {data[b_pos]['country']}")
	user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

	if user_choice == 'a'  and data[a_pos]['follower_count'] >= data[b_pos]['follower_count']:
		score += 1
		print(f"You're right! Current Score: {score}")
		return higher(b_pos,score,False)
	elif user_choice == 'b'  and data[b_pos]['follower_count'] >= data[a_pos]['follower_count']:
		score += 1
		print(f"You're right! Current Score: {score}")
		return higher(b_pos,score,False)
	else:
		higher(b_pos,score,True)
			

higher(random.randint(0,len(data)-1),score,False)

