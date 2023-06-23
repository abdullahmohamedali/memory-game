
import random
from rich import print
dividend = ['1', '2', '3','4','5','6','7','8','9','10', '11', '12', '13', '14', '15']
divisour = ['1', '2', '3','4','5','6','7','8','9','10']
qoint = ['1', '2', '3','4','5','6','7','8','9','10']
e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0

score = 0

p = int( random.choice(dividend) )
v =  int( random.choice(divisour) )

x = int( random.choice(divisour) )
y = int( random.choice(dividend) )

e = int( random.choice(divisour) )
t = int( random.choice(dividend) )

i = int( random.choice(dividend))
h = int( random.choice(divisour)) 


j = int( random.choice(dividend) )
g = int( random.choice(divisour))


b = int( input(f" {p} x {v} = ") )
c = int( input(f" {x} x {y} = ") )
d = int( input(f" {e} x {t} = ") )
s = int( input(f" {i} x {h} = "))
n = int( input(f" {g} x {j} = "))
if p * v == b:
    e1 = "[green]correct"
    score +=10
else:
    e1 = "[red]false"
    score -=5

if x * y == c:
    e2 = "[green]correct"
    score +=10
else:
    e2 = "[red]false"
    score -=5
if e * t == d:
    e3 = "[green]correct"
    score +=10
else:
    e3 = "[red]false"
    score -=5

if i * h == s:
    e4 = "[green]correct"
    score +=10
else:
    e4 = "[red]false"
    score -=5
if g * j == n:
    e5 = "[green]correct"
    score +=10
else:
    e5 = "[red]false"
    score -=5
print(f"q1 {e1} ")
print(f"q2 {e2}")
print(f"q3 {e3}")
print(f"q4 {e4}")
print(f"q5 {e5}")

print(f"your score is {score}")
