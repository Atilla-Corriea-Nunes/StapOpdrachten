import math
#Berekening1
x = 9.1

y = math.sqrt(3 * x - 1) + pow((1 + x),2)

print(y)
#Berekening2
a = 0.87
b = 22.7
c = 5.03

y = (-b+math.sqrt(pow(b,2)-4*a*c))/(2*a)
print(f"De waarde van y = {y} als a = {a}, b = {b} en c = {c}")
#Berekening3
t = 4
v = 179875474.8
c = 299792458

delta = t*1/(1/(v*(1-(pow(v,2))/(pow(c,2)))))

print(f"Vanaf een komeet gezien zit u {delta} uur op de tuinstoel")
