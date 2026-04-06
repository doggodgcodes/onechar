import sys
print("Text To Anychar Converter Extended (line break support)")
text = sys.stdin.read()
output_program = "+"

for character in text:
    if character == " ":
        output_program = output_program + "/;;*;."
    if character == "!":
        output_program = output_program + "/;;*;+."
    if character == '"':
        output_program = output_program + "/;;*;++."
    if character == "#":
        output_program = output_program + "/;;*;+++."
    if character == "$":
        output_program = output_program + "/;;*;++++."
    if character == "%":
        output_program = output_program + "/;;*;+++++."
    if character == "&":
        output_program = output_program + "/;;*;++++++."
    if character == "'":
        output_program = output_program + "/;;*;+++++++."
    if character == "(":
        output_program = output_program + "/;;*;++++++++."
    if character == ")":
        output_program = output_program + "/;;*;+++++++++."
    if character == "*":
        output_program = output_program + "/;;*;++++++++++."
    if character == "+":
        output_program = output_program + "/;;*;+++++++++++."
    if character == ",":
        output_program = output_program + "/;;*;++++++++++++."
    if character == "-":
        output_program = output_program + "/;;*;+++++++++++++."
    if character == ".":
        output_program = output_program + "/;;*;++++++++++++++."
    if character == "/":
        output_program = output_program + "/;;*;+++++++++++++++."
    if character == "0":
        output_program = output_program + "/;;*;++++++++++++++++."
    if character == "1":
        output_program = output_program + "/;;*;+++++++++++++++++."
    if character == "2":
        output_program = output_program + "/;;*;++++++++++++++++++."
    if character == "3":
        output_program = output_program + "/;;*;+++++++++++++++++++."
    if character == "4":
        output_program = output_program + "/;;*;++++++++++++++++++++."
    if character == "5":
        output_program = output_program + "/;;*;+++++++++++++++++++++."
    if character == "6":
        output_program = output_program + "/;;*;++++++++++++++++++++++."
    if character == "7":
        output_program = output_program + "/;;*;+++++++++++++++++++++++."
    if character == "8":
        output_program = output_program + "/;;*;++++++++++++++++++++++++."
    if character == "9":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++."
    if character == ":":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++."
    if character == ";":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++."
    if character == "<":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++."
    if character == "=":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++."
    if character == ">":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++."
    if character == "?":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++."
    if character == "@":
        output_program = output_program + "/;;*;;."
    if character == "A":
        output_program = output_program + "/;;*;;+."
    if character == "B":
        output_program = output_program + "/;;*;;++."
    if character == "C":
        output_program = output_program + "/;;*;;+++."
    if character == "D":
        output_program = output_program + "/;;*;;++++."
    if character == "E":
        output_program = output_program + "/;;*;;+++++."
    if character == "F":
        output_program = output_program + "/;;*;;++++++."
    if character == "G":
        output_program = output_program + "/;;*;;+++++++."
    if character == "H":
        output_program = output_program + "/;;*;;++++++++."
    if character == "I":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++."
    if character == "J":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++."
    if character == "K":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++."
    if character == "L":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++."
    if character == "M":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++."
    if character == "N":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "O":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "P":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "Q":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "R":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "S":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "T":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "U":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "V":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "W":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "X":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "Y":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "Z":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "[":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "\\":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "]":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "^":
        output_program = output_program + "/;;*;++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "_":
        output_program = output_program + "/;;*;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "`":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++."
    if character == "a":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++."
    if character == "b":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++."
    if character == "c":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++."
    if character == "d":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++."
    if character == "e":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++."
    if character == "f":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++."
    if character == "g":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++."
    if character == "h":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++."
    if character == "i":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++."
    if character == "j":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++."
    if character == "k":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++."
    if character == "l":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++."
    if character == "m":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++."
    if character == "n":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "o":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "p":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "q":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "r":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "s":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "t":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "u":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "v":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "w":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "x":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "y":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "z":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "{":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "|":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "}":
        output_program = output_program + "/;;*;;+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "~":
        output_program = output_program + "/;;*;;++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."
    if character == "\n":
        output_program = output_program + "+/;;*------."

    
print(output_program)
