from art import logo

print(logo)
participants_left = 'y'
auction = {}
highest = 0
winner = ''
while participants_left == 'y':
  name = input("Participant name: ")
  bid = int(input("Enter the bid amount: "))
  auction[name] = bid
  if highest < bid:
    highest = bid
    winner = name
  #clear()
  participants_left = input("\nAny particiapnt left? type 'y' to continue 'n' to close bidding ")

print(f"The winner of auction is {winner} and bid amount is ${auction[winner]}")
