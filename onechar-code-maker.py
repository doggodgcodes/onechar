import random

arrayChars = ["-", "+", ";", "*", ".", "^", "-", "+", ";", "*", ".", "^", "/"]

def c():
  e = arrayChars[random.randint(0, len(arrayChars)-1)]
  return e

randomness = c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c() + c()

print("+;**;" + randomness)
