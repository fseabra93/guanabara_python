import converter as cv

def dobro(valor):
    valor = cv.converter(valor)
    return valor*2


def metade(valor):
    valor = cv.converter(valor)
    return valor/2


def aumento(valor, percentual):
    valor = cv.converter(valor)
    aumento = valor*(percentual/100)
    valor = valor+aumento
    return valor


def reducao(valor, percentual):
    valor = cv.converter(valor)
    red = valor*(percentual/100)
    valor = valor-red
    return valor