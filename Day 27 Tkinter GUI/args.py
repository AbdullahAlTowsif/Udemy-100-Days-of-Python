# It's type is Tuple

def add(*args): # I can use *num, *numbers, *anything
    sum = 0
    for n in args:
        sum = sum + n
    print(sum)

add(5, 6, 8, 10, 2, 18, 54)

