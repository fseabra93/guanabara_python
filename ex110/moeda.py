import calculos as cal
import converter as cv

def resumo(valor, aumento, reducao):
    maior = cal.aumento(valor, aumento)
    menor = cal.reducao(valor, reducao)
    dobro = cal.dobro(valor)
    metade = cal.metade(valor)
    original = dobro/2
    imprimir(aumento, reducao, original, maior, menor, dobro, metade)


def imprimir(aumento, reducao, original, maior, menor, dobro, metade):
    original = cv.reconverter(original)
    maior = cv.reconverter(maior)
    menor = cv.reconverter(menor)
    dobro = cv.reconverter(dobro)
    metade = cv.reconverter(metade)

    print('Resumo do Valor')
    print(f'Preço analisado: R${original}')
    print(f'Dobro: R${dobro}')
    print(f'Metade: {metade}')
    print(f'{aumento}% de aumento: R${maior}')
    print(f'{reducao}% de redução: R${menor}')