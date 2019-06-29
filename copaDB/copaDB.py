# Ewerton Vieira de Silles
# 17/06/2019
#
# Programa que exibe um menu de gerenciamento de um banco de dados da copa realizando as funcoes:
# criar selecao, acrescentar jogador, apagar jogador, atualizar o numero de gols e consultar informacoes

import os.path

# Funcao - cria o arquivo selecoes.txt casa ele nao exista

def verificar():
    if (not os.path.isfile('selecoes.txt')):
        arquivo = open('selecoes.txt', 'w')
        arquivo.close()


# Funcao - encontra uma sequencia de caracteres dentro de uma string e retorna sua primeira posicao

def find(string, char):
    encontrou = False
    posicao = ''
    for cont in range(len(string) - 1, -1, -1):
        if (string[cont:cont + len(char)] == char):
            posicao = cont
            encontrou = True
    return posicao, encontrou


# Funcao - encontra uma sequencia de caracteres dentro de uma string e retorna sua ultima posicao

def findReverse(string, char):
    encontrou = False
    posicao = ''
    for cont in range(len(string)):
        if (string[cont:cont + len(char)] == char):
            posicao = cont
            encontrou = True
    return posicao, encontrou


# Funcao - separa as palavras de uma string em uma lista

def split(string, char=' '):
    lista = []
    aux = ''
    string += char
    for caractere in string:
        if (caractere != char):
            aux += caractere
        else:
            lista += [aux]
            aux = ''
    return lista


# Funcao - junta todos os itens de uma lista em uma string separando-os por um determinado caractere

def join(lista, char=''):
    string = ''
    for item in lista:
        string += item + char
    return string


# Funcao - testa se um arquivo existe

def testeArquivo(info):
    if (not os.path.isfile(info + '.txt')):
        info = input('Essa seleção não existe, entre com um nome de seleção válido: ')
        info = testeArquivo(info)
    return info


# Funcao - testa se uma informação contem somente letras

def testeAlpha(info):
    if (not join(split(join(split(info)), '-')).isalpha()):
        info = input('Essa informação deve conter apenas letras, tente novamente: ')
        info = testeAlpha(info)
    return info


# Funcao - testa se uma informação contem somente numeros

def testeNum(info):
    if (not info.isnumeric()):
        info = input('Essa informação deve conter apenas números, tente novamente: ')
        info = testeNum(info)
    return int(info)


# Funcao - ordena as linhas de uma matriz com base em uma determinada coluna

def ordenar(matriz, coluna):
    for cont in range(len(matriz) - 1):
        for cont in range(len(matriz) - 1):
            if (matriz[cont][coluna].isnumeric()):
                if (int(matriz[cont][coluna]) > int(matriz[cont + 1][coluna])):
                    aux = matriz[cont]
                    matriz[cont] = matriz[cont + 1]
                    matriz[cont + 1] = aux
            elif (matriz[cont][coluna] > matriz[cont + 1][coluna]):
                    aux = matriz[cont]
                    matriz[cont] = matriz[cont + 1]
                    matriz[cont + 1] = aux
    return matriz


# Funcao - ordena as linhas de uma matriz pela posicao do jogador e em ordem alfabetica do nome

def ordenarposicao(lista):
    goleiro = []
    zagueiro = []
    lateral = []
    meiocampo = []
    atacante = []
    for jogador in lista:
        if (jogador[4].lower() == 'goleiro'):
            goleiro += [jogador]
        if (jogador[4].lower() == 'zagueiro'):
            zagueiro += [jogador]
        if (jogador[4].lower() == 'lateral'):
            lateral += [jogador]
        if (jogador[4].lower() == 'meio-campo'):
            meiocampo += [jogador]
        if (jogador[4].lower() == 'atacante'):
            atacante += [jogador]
    goleiro = ordenar(goleiro, 0)
    zagueiro = ordenar(zagueiro, 0)
    lateral = ordenar(lateral, 0)
    meiocampo = ordenar(meiocampo, 0)
    atacante = ordenar(atacante, 0)
    return goleiro + zagueiro + lateral + meiocampo + atacante


# Funcao - recebe uma matriz e imprime no formato de uma tabela destacando a primeira linha

def imprimirtabela(listadelinhas):
    borda = ''
    maiores = []
    for coluna in range(len(listadelinhas[0])):
        maior = 0
        for linha in range(len(listadelinhas)):
            if (len(str(listadelinhas[linha][coluna])) > maior):
                maior = len(listadelinhas[linha][coluna])
        maiores += [maior]
        borda += '+' + '-' * (maior + 2)
    borda += '+'
    linhas = []
    for linha in range(len(listadelinhas)):
        elemento = ''
        for coluna in range(len(listadelinhas[0])):
            if ((maiores[coluna] + 2 - len(str(listadelinhas[linha][coluna])))%2 == 1):
                espaco1 = ' ' * ((maiores[coluna] + 2 - len(str(listadelinhas[linha][coluna]))) // 2)
                espaco2 = espaco1 + ' '
            else:
                espaco1 = espaco2 = ' ' * ((maiores[coluna] + 2 - len(str(listadelinhas[linha][coluna])))//2)
            elemento += '|' + espaco1 + str(listadelinhas[linha][coluna]) + espaco2
        elemento += '|'
        linhas += [elemento]
    print(borda)
    print(linhas[0])
    print(borda)
    for cont in range(1, len(linhas)):
        print(linhas[cont])
    print(borda)


# Funcao - criar um arquivo verificando se ele ja nao existe

def criar(selecao):
    if (not os.path.isfile(selecao + '.txt')):
        arquivo = open(selecao + '.txt', 'w')
        arquivo.close()
        arquivo = open('selecoes.txt', 'r')
        selecoes = arquivo.read()
        arquivo.close()
        arquivo = open('selecoes.txt', 'a')
        try:
            linha = selecoes[-1]
        except IndexError:
            linha = '\n'
        if (linha == '\n'):
            arquivo.write(selecao)
        else:
            arquivo.write('\n' + selecao)
        arquivo.close()
        retorno = 'A lista de dados dos jogadores da seleção do(a) ' + selecao + ' foi criada.'
    else:
        retorno = 'A seleção já existe.'
    return retorno


# Funcao - acrescenta os dados de um jogador ao arquivo da sua selecao

def acrescentar(selecao, nome, idade, time, posicao, gols):
    arquivo = open(selecao + '.txt', 'r')
    conteudo = arquivo.read()
    arquivo.close()
    arquivo = open(selecao + '.txt', 'a')
    try:
        linha = conteudo[-1]
    except IndexError:
        linha = '\n'
    if (linha == '\n'):
        arquivo.write(nome + ';' + str(idade) + ';' + time + ';' + posicao + ';' + str(gols))
    else:
        arquivo.write('\n' + nome + ';' + str(idade) + ';' + time + ';' + posicao + ';' + str(gols))
    arquivo.close()


# Funcao - apaga os dados de um jogador do arquivo da sua selecao

def apagar(selecao, nome):
    arquivo = open(selecao + '.txt', 'r')
    conteudo = arquivo.read()
    inicio, encontrou = find(conteudo, nome)
    if (encontrou):
        fim, encontrou = find(conteudo[inicio:], '\n')
        if (not encontrou):
            fim = len(conteudo[inicio:])
        arquivo.close()
        arquivo = open(selecao + '.txt', 'w')
        arquivo.write(conteudo[:inicio] + conteudo[inicio + fim + 1:])
        retorno = 'O jogador foi apagado com sucesso.'
    else:
        retorno = 'O jogador não existe.'
    arquivo.close()
    return retorno


# Funcao - atualiza a quantidade de gols de um jogador no arquivo da sua selecao

def atualizar(selecao, nome, gols):
    arquivo = open(selecao + '.txt', 'r')
    conteudo = arquivo.read()
    inicio, encontrou = find(conteudo, nome)
    if (encontrou):
        fim, encontrou = find(conteudo[inicio:], '\n')
        if (not encontrou):
            fim = len(conteudo[inicio:])
        atualizacao = conteudo[inicio:inicio + fim + 1]
        posicao, encontrou = findReverse(atualizacao, ';')
        atualizacao = atualizacao[:posicao + 1] + str(gols)
        arquivo.close()
        arquivo = open(selecao + '.txt', 'w')
        arquivo.write(conteudo[:inicio] + atualizacao + conteudo[inicio + fim:])
        retorno = 'Número de gols atualizados com sucesso.'
    else:
        retorno = 'O jogador não existe.'
    arquivo.close()
    return retorno


# Funcao - consulta os arquivos de texto e exibe numa tabela as informacoes que foram solicitadas pelo usuario

def consultar(info):
    arquivo = open('selecoes.txt', 'r')
    selecoes = arquivo.readlines()
    arquivo.close()
    for cont in range(len(selecoes)):
        if selecoes[cont][-1] == '\n':
            selecoes[cont] = selecoes[cont][:-1]
        if (selecoes[cont][-4:] == '.txt'):
            selecoes[cont] = selecoes[cont][:-4]
    listacompleta = []
    for cont in range(len(selecoes)):
        arquivo = open(selecoes[cont] + '.txt', 'r')
        lista = arquivo.readlines()
        for item in range(len(lista)):
            if lista[item][-1] == '\n':
                lista[item] = lista[item][:-1]
            lista[item] = [selecoes[cont]] + split(lista[item], ';')
        listacompleta += lista
    if (info.isnumeric()):
        lista = []
        for dicionario in listacompleta:
            if (int(dicionario[2]) < int(info)):
                lista += [dicionario]
        for cont in range(len(lista)):
            lista[cont] = lista[cont][:3]
        print('=-=' * 10)
        if (lista != []):
            print('Segue a tabela dos jogadores com menos de', info, 'anos:')
            imprimirtabela([['País', 'Nome', 'Idade']] + ordenar(lista, 2))
        else:
            print('Não há jogadores com menos de', info, 'anos!')
        print('=-=' * 10)
    elif (info in selecoes):
        lista = []
        for jogador in listacompleta:
            if (info == jogador[0]):
                lista += [jogador]
        lista = ordenarposicao(lista)
        for cont in range(len(lista)):
            lista[cont] = [lista[cont][1]] + [lista[cont][4]]
        print('=-=' * 10)
        if (lista != []):
            print('Segue a tabela dos jogadores da seleção do(a)', info + ':')
            imprimirtabela([['Nome', 'Posição']] + lista)
        else:
            print('Não há jogadores registrados nessa seleção!')
        print('=-=' * 10)
    elif (info.lower() == 'artilheiros'):
        for cont in range(len(listacompleta)):
            listacompleta[cont] = listacompleta[cont][:2] + [listacompleta[cont][-1]]
        listacompleta = ordenar(listacompleta, 2)
        lista = listacompleta + []
        for cont in range(len(listacompleta)):
            lista[cont] = listacompleta[-cont - 1]
        print('=-=' * 10)
        if (lista != []):
            print('Segue a tabela dos 10 principais artileiros da copa:')
            imprimirtabela([['País', 'Nome', 'Número de gols']] + lista[:10])
        else:
            print('Não há jogador algum no banco de dados!')
        print('=-=' * 10)
    else:
        lista = []
        for jogador in listacompleta:
            if (info.lower() == jogador[3].lower()):
                lista += [jogador]
        if (lista != []):
            lista = ordenarposicao(lista)
            for cont in range(len(lista)):
                lista[cont] = lista[cont][:2] + [lista[cont][4]]
            print('=-=' * 10)
            print('Segue a tabela dos jogadores que jogam no', info + ':')
            imprimirtabela([['País', 'Nome', 'Posição']] + lista)
            print('=-=' * 10)
        else:
            info = input('Opção inválida. Tente novamente: ')
            consultar(info)


# Funcao - imprime o menu principal do programa com seis opcoes

def menu():
    print('=-=-= Banco de dados da copa =-=-='
          '\nSelecione uma opção do menu:'
          '\n   [1] Criar seleção'
          '\n   [2] Acescentar jogador'
          '\n   [3] Apagar jogador'
          '\n   [4] Atualizar numéro de gols de um jogador'
          '\n   [5] Consultar'
          '\n   [6] Sair do programa')


# Funcao - imprime o menu de consulta com quatro opcoes

def menuConsulta():
    print('Selecione uma opção do menu:'
          '\n   >>> Entre com o nome de uma seleção para exibir seus jogadores.'
          '\n   >>> Entre com uma idade para exibir os jogadores abaixo desta idade.'
          '\n   >>> Entre com o nome de um time para exibir seus jogadores.'
          '\n   >>> Digite "artilheiros" para exibir os 10 principais artilheiros da copa.')


######## Programa principal ########

def main():
    menu()
    opcao = input('Qual sua opção? ')
    opcao = testeNum(opcao)
    while (opcao < 1 or opcao > 6):
        print('Opção inválida!')
        opcao = input('Qual sua opção? ')
        opcao = testeNum(opcao)
    print('=-=' * 10)
    if (opcao == 1):
        selecao = input('Entre com o nome da seleção: ')
        selecao = testeAlpha(selecao)
        print('=-=' * 10)
        print(criar(selecao))
    elif (opcao == 2):
        selecao = input('Entre com o nome da seleção na qual deseja acrescentar um jogador: ')
        selecao = testeArquivo(selecao)
        nome = input('Entre com o nome do jogador: ')
        nome = testeAlpha(nome)
        arquivo = open(selecao + '.txt', 'r')
        conteudo = arquivo.read()
        arquivo.close()
        while (find(conteudo, nome)[1]):
            nome = input('Esse jogador já foi registrado, entre com outro nome: ')
            nome = testeAlpha(nome)
        idade = input('Entre com a idade do jogador: ')
        idade = testeNum(idade)
        while (idade < 18):
            idade = input('O jogador deve ser maior de idade, tente novamente: ')
            idade = testeNum(idade)
        time = input('Entre com o nome do time que ele joga: ')
        time = testeAlpha(time)
        posicao = input('Entre com a posição que ele joga: ')
        posicao = testeAlpha(posicao)
        gols = input('Entre com o número de gols: ')
        gols = testeNum(gols)
        acrescentar(selecao, nome, idade, time, posicao, gols)
        print('=-=' * 10)
        print('Dados do jogador adicionados com sucesso.')
    elif (opcao == 3):
        selecao = input('Entre com o nome da seleção na qual deseja apagar um jogador: ')
        selecao = testeArquivo(selecao)
        nome = input('Entre com o nome do jogador: ')
        nome = testeAlpha(nome)
        print('=-=' * 10)
        print(apagar(selecao, nome))
    elif (opcao == 4):
        selecao = input('Entre com o nome da seleção na qual deseja atualizar o número de gols de um jogador: ')
        selecao = testeArquivo(selecao)
        nome = input('Entre com o nome do jogador: ')
        nome = testeAlpha(nome)
        gols = input('Entre com o novo número de gols: ')
        gols = testeNum(gols)
        print('=-=' * 10)
        print(atualizar(selecao, nome, gols))
    elif (opcao == 5):
        menuConsulta()
        info = input('Digite uma das opções: ')
        consultar(info)
    if (opcao != 6):
        main()


##### verifica a exixtencia do arquivo principal antes da inicializacao do programa e o executa

verificar()
main()

##### Termino do programa

print('Fim do programa! Volte sempre!')
