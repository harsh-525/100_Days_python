import random
from art import logo

#print logo
print(logo)

spl_cards = ['K', 'Q', 'J']
possible_A = {
    1 : [[1],[11]],
    2 : [[1,11],[11,11],[1,1]],
    3 : [[1,1,1],[1,11,1],[11,1,11],[11,11,11]]
}
user = []
dealer = []
purse = 100
bet = 0

quit = False
choice = ''
user_total, dealer_total = 0, 0

def draw():
	deck = ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]
	return random.choice(deck)

def user_hit():
	card = draw()
	user.append(card)


def dealer_hit():
	card = draw()
	dealer.append(card)



def straight_luck():
	if 'A' in user and (10 in user or 'J' in user or 'K' in user
	                    or 'Q' in user):
		return True
	else:
		return False


def valid_bet_increase(curr_purse):
	add_bet = int(
	    input(
	        f"Current purse is ${curr_purse}\nTo increase the bet enter 5/10/20/50 or 0 to place same bet: "
	    ))
	curr_purse -= add_bet
	while curr_purse < 0:
		print(curr_purse)
		curr_purse += add_bet
		add_bet = 0
		print(curr_purse)
		add_bet += int(
		    input(
		        f"Insufficient funds. Availablep purse: ${curr_purse}.\nEnter bet amount again: "
		    ))
		curr_purse -= add_bet
		print(curr_purse)
	return add_bet



def total(person, total, cards):

	if 'A' not in cards:
		for i in cards:
			if i in spl_cards:
				total += 10
			else:
				total += i
		return total
	elif person == 'user':
		a_totals = []
		for i in cards:
			if i in spl_cards:
				total += 10
			elif i != 'A':
				total += i
		no_a = cards.count('A')
		for i in possible_A[no_a]:
			a_totals.append(total + sum(i))
		print("The possible totals of user pack is:\t",a_totals)

		#check user_totals lose condition
		count = 0
		for i in a_totals:
			if i>21:
				count+=1
		if count == len(a_totals):
			return 22
		pos = int(input("Choose which total to consider according to possition: "))
		total = a_totals[pos-1]
		return total		
	else:
		for i in cards:
			if i in spl_cards:
				total += 10
			elif i == 'A':
				total += 11
			else:
				total += i
		return total
		
def dealers_show(dealer_score, user_score,dealer):

	#print("Dealer pack: ",dealer)
	dealer_score = total('dealer',dealer_score,dealer)
	#print(dealer_score)
	
	if dealer_score == user_score:
		print("DRAW\nDealer cards: ", dealer)
		print("dealer pack total:\t", dealer_score)

	elif (dealer_score >= 17 and dealer_score > user_score) or dealer_score == 21:
		print("DEALER WIN\nDealer cards: ", dealer)
		print("dealer pack total:\t", dealer_score)

	elif dealer_score < user_score and dealer_score >= 17:
		print("========> BLACKJACK! You win. Total purse: $150")
		print("dealer pack total:\t", dealer_score)
		
	else:
		dealer_hit()
		dealers_show(0,user_score,dealer)
	


print(f"Starting game with bet ${bet} and purse amount ${purse}")
bet = int(input("Place the inital bet in the amounts of 5/10/20/50: "))
purse -= bet

user_hit()
user_hit()
dealer_hit()
dealer_hit()

while not quit:

	if len(user) == 2 and straight_luck():
		purse += 50
		print(f"User cards: {user}\nDealer cards: {dealer}")
		print(f"BLACKJACK! You win: $150")
		quit = True
	else:
		if purse >= 0:
			print(f"User cards\t: {user}\nDealer cards\t: {dealer[0]},_")
			user_total = 0
			user_total = total('user', user_total, user)
			print("user pack total:\t", user_total)
			if user_total > 21:
				print("========> YOU LOSE\nDealer cards: ", dealer)
				dealer_total = total('dealer',dealer_total,dealer)
				print("dealer pack total:\t", dealer_total)
				quit = True
			elif user_total < 21 and user_total >= 17:
				print('-----------------------------------------------------')
				choice = input("Dealer\t: Enter 'h' for hit and 's' for stand\nUser\t: ")
				if choice == 'h':
					purse -= valid_bet_increase(purse)
					user_hit()
				else:
					dealers_show(dealer_total,user_total,dealer)
					quit = True					
			elif user_total < 17:
				print('-----------------------------------------------------')
				choice = input("Dealer\t: Enter 'h' for hit\nUser\t: ")
				purse -= valid_bet_increase(purse)
				user_hit()
			else:
				print(f"========> BLACKJACK! You win. Total purse: $150")
				quit = True
		else:
			print("========> PURSE Empty; Exiting the game")
			quit = True
