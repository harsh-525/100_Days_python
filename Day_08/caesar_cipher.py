alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(text,shift,direciton):
  key = []
  pos = 0
  result = ''

  if (shift % 26 == 0 ):
      key = alphabet
  else:
    shift %= 26
    key = alphabet[shift:]+alphabet[:shift]
  print(alphabet,"\n",key)

  if direction == 'encode':
    for letter in text:
      if letter not in alphabet:
        result += letter
      else:
        pos = alphabet.index(letter)
        result += key[pos]
  else:
    for letter in text:
      if letter not in alphabet:
        result += letter
      else:
        pos = key.index(letter)
        result += alphabet[pos]
  print(f"The {direction}ed text is: {result}")

stop = 'n'
while not stop == 'y':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  
  caesar(text, shift, direction)
  stop = input("\nstop? type 'y' for yes or 'n' for no ").lower()
