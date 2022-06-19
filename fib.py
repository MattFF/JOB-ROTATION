numero = 13

fib_ant = 0
fib_prox = 1

if (numero == 0 or numero == 1):
    print(f'O número {numero} pertence a sequência de fibonacci')
else:
    while True:
        result = fib_ant + fib_prox
        if result == numero:
            print(f'O número {numero} pertence a sequência de fibonacci')
            break
        elif result > numero:
            print(f'O número {numero} não pertence a sequência de fibonacci')
            break

        fib_ant = fib_prox
        fib_prox = result
