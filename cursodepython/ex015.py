dias = int(input('Quantos dias o carro foi alugado? ')) * 60
km = float(input('Quantos km rodados? ')) * 0.15
print('O total à pagar é de R${}'.format(dias + km))
