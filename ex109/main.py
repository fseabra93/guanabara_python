import funcionalidades as fc
import moeda

p = str(input('Digite o preço: R$'))
print(f'A metade de {fc.converter(p)} é {moeda.metade(p)}')
print(f'O dobro de {fc.converter(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumentar(p)}')
print(f'Reduzindo 13% temos {moeda.moeda(p)}')
