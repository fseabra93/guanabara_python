from lib.arquivo import *
from lib import interface as int
from time import sleep

int.cabeçalho('SISTEMA ARQUIVO v.1.0')

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = int.menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo do arquivo
        lerArquivo(arq)

    elif resposta == 2:
        int.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int.leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        int.cabeçalho('Saindo do sistema. Até logo.')

        break
    else:
        print('\33[31mERRO! Digite uma opção válida.\33[m')
    sleep(1)