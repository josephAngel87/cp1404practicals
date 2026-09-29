"""
Rectangle Area
"""
import random

length = int(input("Length: "))
width = random.randint(1,length)

area = length*width
print(length," * ",width,"is equal to ",area)
