
def busca2(vetor, num):
    print(f'len(vetor) passou = {len(vetor)}')
    #print(vetor)
    tam = len(vetor)
    recursao = 0
    while(tam>=1):
        recursao += 1
        posicao = len(vetor)//2
        #print(f'vetor[posicao] = {vetor[posicao]}')
        if (vetor[posicao] == num):
            print(f'recursao = {recursao}')
            return True
        else:
            if (num > vetor[posicao]):
                del (vetor[: posicao + 1])
                tam = len(vetor)
                #print(f'tam = {tam}')
                #print(vetor)
            else:
                del (vetor[posicao :])
                tam = len(vetor)
                #print(f'tam = {tam}')
                #print(vetor)
    print(f'recursao = {recursao}')
    return False



import random

vetor = []

tam = int(input("Qual o tamanho do vetor? "))
num = int(input("Qual o número a ser procurado? "))

for i in range (tam):
    a = random.randint(1, tam)
    if (a not in vetor):
        vetor.append(a)

vetor.sort()
print(vetor)

if busca2(vetor, num) == True:
    print(f'O valor {num} foi encontrado.')
else:
    print(f'O valor {num} não foi encontrado.')
