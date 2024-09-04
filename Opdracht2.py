import math
#Berekening1
x = 9.1

y = math.sqrt(3 * x - 1) + pow((1 + x),2)

print(y)
#Berekening2
a = 0.87
b = 22.7
c = 5.03

y = (-b + math.sqrt(pow(b,2)-4*a*c))/(2*a)
print(f"De waarde van y = {y} als a = {a}, b = {b} en c = {c}")

