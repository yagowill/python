preço = int(input('Digite o preço do produto: R$'))
desconto = preço * 5 / 100
res = preço - desconto
print('o valor com 5% de desconto é R${}'.format(res))