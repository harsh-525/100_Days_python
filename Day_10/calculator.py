from art import logo
print(logo)

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

def mod(a,b):
  return a%b

result = 0
run = 'y'
func = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
  "%":mod
}
while run != 'n':  
  if run == 'clear' or result == 0:
    result = 0
    a = float(input("Enter your first number " ))
    b = float(input("Enter your second number "))
  else:
    a = result
    b = float(input("Enter your number "))
  op = input("enter the operation to perform + , - , * , / , %\nType your operation: ")
  result = func[op](a,b)
  print(f"{a}{op}{b} = {result}")

  run = input("enter 'n' to stop calculator \n'clear' to clear the history and continue \nelse 'y' to continue\n")
    
    
