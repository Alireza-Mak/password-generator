import random
print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))
letters =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers =["1","2","3","4","5","6","7","8","9","0"]          
symbols =["(",")","*","&","^","%","$","#","@","!"]
data=[letters,numbers,symbols]
totalCharLen = letter + symbol + number
password =""
for _ in range(0,totalCharLen):
  randomNum = random.choice(data)
  randomNum2 = random.choice(randomNum)
  password += randomNum2

print(f"Your password is:\n{password}")
  
