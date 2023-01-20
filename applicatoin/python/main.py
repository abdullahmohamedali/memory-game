
import random
from rich import print
from pprint import pprint

dividend = ['1', '2', '3','4','5','6','7','8','9','10']
divisour = ['1', '2', '3','4','5','6','7','8','9','10']
qoint = ['1', '2', '3','4','5','6','7','8','9','10']
e1 = 0
e2 = 0
e3 = 0

p = int( random.choice(dividend) )
v =  int( random.choice(divisour) )

x = int( random.choice(divisour) )
y = int( random.choice(dividend) )

e = int( random.choice(divisour) )
t = int( random.choice(dividend) )




b = int( input(f" {p} x {v} = ") )
c = int( input(f" {x} x {y} = ") )
d = int( input(f" {e} x {t} = ") )


if p * v == b:
    e1 = "[green]correct"
else:
    e1 = "[red]false"


if x * y == c:
    e2 = "[green]correct"
else:
    e2 = "[red]false"

if e * t == d:
    e3 = "[green]correct"
else:
    e3 = "[red]false"

print(f"q1 {e1} ")
print(f"q2 {e2}")
print(f"q3 {e3}")

