def converter(valor):
    if (',' in valor):
        valor = valor.replace(",", ".")

    valor = float(valor)

    return valor
