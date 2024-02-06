# Funkcja jako argument funkcji

def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(func, values):
    returned_values=[]
    for value in values:
        returned_values.append(func(value))

    return returned_values



x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))