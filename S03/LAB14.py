# Funkcja compile()

import math
import time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []
for i in range(1000000):
    argument_list.append(i / 10)

print("Uncompiled execution")
for formula in formulas_list:
    results_list=[]
    print(f'Formula {formula}')

    start_time = time.time()
    for x in argument_list:
        results_list.append(exec(formula))

    stop_time = time.time()

    print(f"Calculation time: {stop_time-start_time}")


print("Compiled execution")
for formula in formulas_list:
    results_list=[]
    print(f'Formula {formula}')

    start_time = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(exec(compiled_formula))
    stop_time = time.time()

    print(f"Calculation time: {stop_time-start_time}")

