from funcionalidades import converter

def moeda(valor):
    valor = converter(valor)
    return valor

def dobro(valor):
    valor = converter(valor)
    return valor*2


def metade(valor):
    valor = converter(valor)
    valor = valor/2
    return valor


def aumentar(valor):
    valor = converter(valor)
    aumento = valor/10
    valor = valor + aumento
    return valor