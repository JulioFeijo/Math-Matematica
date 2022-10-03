""""Calculo da formula de bhaskara."""

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))
delta = ((b ** 2) + (-4 * a * c))
if  delta > 0:
    print(f'{delta} - delta')
    raiz = delta ** 0.5
    print(f'{raiz}  - raiz')
    r1 = (((-1 * b) + raiz) / (2 * a))
    r2 = (((-1 * b) - raiz) / (2 * a))
    print(f'{r1} e {r2}')
elif delta == 0:
    print(f'Raiz unica')
else:
    print(f'MathERROR')
