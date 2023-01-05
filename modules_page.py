def square_foot_inputs():
    length = float(input('What is the length of the house? '))
    width = float(input('What is the width of the house? '))
    return length * width

def square_foot(length, width):
    return length * width

def circum(r):
    from math import pi
    return 2 * float(pi) * int(r)

def circum_inputs():
    from math import pi
    r = int(input('What is the radius of the circle? '))
    return 2 * float(pi) * int(r)
