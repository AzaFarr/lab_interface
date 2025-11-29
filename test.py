import math as m

Re = 300000
f = 0.003

sol = 1 / m.sqrt(f) - 4 * m.log10(Re * m.sqrt(f)) + 0.4

print(sol)

