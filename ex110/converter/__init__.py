def converter(valor):
    if ',' in valor:
        valor = valor.replace(',', '.')
    valor = float(valor)
    return valor


def reconverter(valor):
    valor = str(valor)
    if '.' in valor:
        valor = valor.replace('.', ',')
        valor = valor + '0'
    return valor

