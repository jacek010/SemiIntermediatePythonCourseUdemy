# Funkcja eval()

import math

argument_list = []
value=0
for i in range(101):
    argument_list.append(i/10)

print(argument_list)

formula = input("Enter a formula, use 'x' as the argument: ")

for x in argument_list:
    print(f"{x} -> {round(eval(formula), 3)}")
