print(""""\nCódigo para calcular a determinante de uma matriz 2x2 ou 3x3.\n
Para calcular a determinante colocar os números da equação na seguinte sequência:\n
aX + bY – cZ = N
aX [0,0]
bY [0,1]
cZ [0,2]
 N [0,3]

Assim para todas as equações que você tiver.

Atenção para não esquecer do sinal dos valores!""")
num = int(input("Escolha sua matriz:\n"
                "[ 1 ] - 2 x 2\n"
                "[ 2 ] - 3 x 3\n"
                "Opção: "))
if num == 1:
    matriz = [[0, 0, 0], [0, 0, 0]]
    for l in range(0, 2):
        for c in range(0, 3):
            matriz[l][c] = int(input(f'Digite os valores da matriz para [{l}, {c}]: '))
    print('-=' * 30)
    for l in range(0, 2):
        for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
    print('-=' * 30)
    det_m = ((matriz[0][0]) * (matriz[1][1]) +
             ((matriz[1][0]) * (matriz[0][1]) * -1))
    print(f'{det_m}')
    det_a = ((matriz[0][2]) * (matriz[1][2]) +
             ((matriz[1][0]) * (matriz[0][1]) * -1))
    print(f'{det_a}')
    det_b = ((matriz[0][0]) * (matriz[1][1]) +
             ((matriz[0][2]) * (matriz[1][2]) * -1))
    print(f'{det_b}')
    a = det_a / det_m
    b = det_b / det_m
    print(f'Resultado é de a = {a}')
    print(f'Resultado é de b = {b}')

elif num == 2:
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for l in range(0, 3):
        for c in range(0, 4):
            matriz[l][c] = int(input(f'Digite os valores da matriz para [{l}, {c}]: '))
    print('-=' * 30)
    for l in range(0, 3):
        for c in range(0, 4):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
    print('-=' * 30)
    det_m = (((matriz[0][0] * matriz[1][1] * matriz[2][2]) +
              (matriz[0][1] * matriz[1][2] * matriz[2][0]) +
              (matriz[0][2] * matriz[1][0] * matriz[2][1])) +
             ((matriz[0][2] * matriz[1][1] * matriz[2][0]) * -1) +
             ((matriz[0][0] * matriz[1][2] * matriz[2][1]) * -1) +
             ((matriz[0][1] * matriz[1][0] * matriz[2][2]) * -1))
    print(f'{det_m} ')
    det_a = (((matriz[0][3] * matriz[1][1] * matriz[2][2]) +
              (matriz[0][1] * matriz[1][2] * matriz[2][3]) +
              (matriz[0][2] * matriz[1][3] * matriz[2][1])) +
             ((matriz[0][2] * matriz[1][1] * matriz[2][3]) * -1) +
             ((matriz[0][3] * matriz[1][2] * matriz[2][1]) * -1) +
             ((matriz[0][1] * matriz[1][3] * matriz[2][2]) * -1))
    print(f'{det_a}')

    det_b = (((matriz[0][0] * matriz[1][3] * matriz[2][2]) +
              (matriz[0][3] * matriz[1][2] * matriz[2][0]) +
              (matriz[0][2] * matriz[1][0] * matriz[2][3])) +
             ((matriz[0][2] * matriz[1][3] * matriz[2][0]) * -1) +
             ((matriz[0][0] * matriz[1][2] * matriz[2][3]) * -1) +
             ((matriz[0][3] * matriz[1][0] * matriz[2][2]) * -1))
    print(f'{det_b}')