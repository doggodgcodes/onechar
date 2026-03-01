import sys
import math
chars = sys.stdin.readline()
asc = 0
final = ""
print("")
for character in chars:
    if character == "-":
        asc = asc - 1
    if character == "+":
        asc = asc + 1
    if character == ".":
        if asc > 255:
            asc = asc - 255
        final = final + chr(math.floor(asc))
    if character == "*":
        asc = asc * asc
    if character == "/":
        asc = asc / asc
    if character == "^":
        asc = asc * asc - asc
    if character == "!":
        print(asc)
    if character == ";":
        asc = asc * 2
print(final)
