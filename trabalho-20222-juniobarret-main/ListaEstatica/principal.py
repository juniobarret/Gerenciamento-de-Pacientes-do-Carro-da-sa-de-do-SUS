
############# TRABALHO PARTE 1: LISTA ESTATICA #############

################ BIBLIOTECAS :
import csv
import random
from faker import Faker
from datetime import datetime
from os import system
import time as time
##############################

######## CLASSE PACIENTE :
class Paciente:
    def __init__(self, id, nome, idade, telefone, data_exame):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.data_exame = data_exame

    def __str__(self):
        return f' Nome: {self.nome}\n Idade: {self.idade}\n Telefone: {self.telefone}\n Data do exame: {self.data_exame}\n' 
######## CLASSE LISTA ESTATICA :

class ListaEstatica:
    def __init__(self):
        self.tamanho = 10
        self.lista = [None] * self.tamanho
        self.qtd = 0
    
    def __str__(self):
        return str([str(paciente) for paciente in self.lista])
    
    def expandir_lista(self):
        self.tamanho *= 2
        nova_lista = [None] * self.tamanho
        for i in range(self.qtd):
            nova_lista[i] = self.lista[i]
        self.lista = nova_lista

######### INSERÇÕES:

    def inserir_final(self, paciente):
        if self.qtd == self.tamanho:
            self.expandir_lista()
        self.lista[self.qtd] = paciente
        self.qtd += 1

    def inserir_inicio(self, paciente):
        if self.qtd == self.tamanho:
            self.expandir_lista()
        elif self.qtd == 0:
            self.lista[0] = paciente
            self.qtd += 1
        else:
            self.elementos[1:] = self.elementos[0:]
            self.elementos[0] = paciente
            self.qtd += 1

##### IMPRESSÕES:

    def imprimir_lista(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            for i in range(self.qtd):
                print(f'---------- PACIENTE ID: {self.lista[i].id} ----------')
                print(self.lista[i])
                print()

##### BUSCAS:
    def buscar_por_id(self, id):
        if self.qtd == 0:
            print()
            print('ERRO: A Lista ainda não possui pacientes!')
        else:
            for i in range(self.qtd):
                if self.lista[i].id == id:
                    print()
                    print(f'---------- PACIENTE ID: {self.lista[i].id} ----------')
                    print(">>> Paciente encontrado na posição:", i,"\n")
                    return print(self.lista[i]) 
            print()
            return print('>  Paciente não encontrado!')
        
    
    def buscar_maior_id(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            maior_id = 0
            for i in range(self.qtd):
                if self.lista[i].id > maior_id:
                    maior_id = self.lista[i].id
            print()
            print(" >>> O paciente de maior ID foi encontrado na posição:", i)
            print(f'---------- PACIENTE ENCONTRADO - ID: {self.lista[i].id} ----------')
            return print(self.lista[i])
        
    
    def buscar_menor_id(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            menor_id = float('inf')
            for i in range(self.qtd):
                if self.lista[i].id < menor_id:
                    menor_id = self.lista[i].id
                    posicao_menor_id = i
            print()
            print(" >>> O paciente de menor ID foi encontrado na posição:", posicao_menor_id)
            print()
            print(f'---------- PACIENTE ENCONTRADO - ID: {self.lista[posicao_menor_id].id} ----------')
            return print(self.lista[posicao_menor_id])
    
    
    def buscar_primeiro(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            print()
            print(f'---------- PRIMEIRO PACIENTE - ID: {self.lista[0].id} ----------')
            return print(self.lista[0])
    

    
    def buscar_ultimo(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            print()
            print(f'---------- ÚLTIMO PACIENTE > POSICAO: {self.qtd-1} - ID: {self.lista[self.qtd-1].id} ----------')
            return print(self.lista[self.qtd-1])
        
##### REMOÇÕES:
                
    def remover_primeiro(self):
        if self.qtd == 0:
           print()
           print('ERRO: A Lista ainda não possui pacientes!')
           print()
        else:
            self.lista[0] = self.lista[1]
            self.qtd -= 1
            return print(f'> O primeiro paciente da lista foi removido com sucesso! Paciente removido: {self.lista[0].nome} / ID: {self.lista[0].id}')
        
    def remover_ultimo(self):
        if self.qtd == 0:
           print()
           print('ERRO: A Lista ainda não possui pacientes!')
           print()
        else:
            x = self.lista[self.qtd-1]
            self.qtd -= 1
            return print(f'> O último paciente da lista foi removido com sucesso! Paciente removido: {x.nome} / ID: {x.id}')
        

    def remover_menor_id(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            menor_id = float('inf')
            for i in range(self.qtd):
                if self.lista[i].id < menor_id:
                    menor_id = self.lista[i].id
                    posicao_menor_id = i
            x = self.lista[posicao_menor_id]
            self.lista[posicao_menor_id] = self.lista[posicao_menor_id+1]
            self.qtd -= 1
            return print(f' >>> O paciente de menor ID foi removido da posição {posicao_menor_id} com sucesso! Paciente removido: {x.nome} / ID: {x.id}')
        
    def remover_maior_id(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            maior_id = 0
            for i in range(self.qtd):
                if self.lista[i].id > maior_id:
                    maior_id = self.lista[i].id
                    posicao_maior_id = i
            x = self.lista[posicao_maior_id]
            self.lista[posicao_maior_id] = self.lista[posicao_maior_id+1]
            self.qtd -= 1
            return print(f'> O paciente de maior ID foi removido da posição {posicao_maior_id} com sucesso! Paciente removido: {x.nome} / ID: {x.id}')
        
    def remover_por_id(self, id):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            for i in range(self.qtd):
                if self.lista[i].id == id:
                    x = self.lista[i]
                    self.lista[i] = self.lista[i+1]
                    self.qtd -= 1
                    return print(f'> O paciente de ID {id} foi removido com sucesso! Paciente removido: {x.nome} / ID: {x.id}')
            print()
            return print('>  Paciente não encontrado!')
        
        
    def remover_todos(self):
        if self.qtd == 0:
            print()
            print('>> A lista está vazia! <<')
        else:
            self.qtd = 0
            return print(f'> Todos os pacientes foram removidos com sucesso!')


class Arquivo:
    import faker as faker
    @staticmethod
    def cadastrar_pacientes(lista,n, sequencia):
        inicio = time.time()
        elementos = []
        id_set = set() 
        if sequencia.lower() == "a":
            print("... Gerando dados aleatórios...")
            for i in range(n):
                fake = Faker('pt_BR')
                while True:
                    id = random.randint(1, 100000)
                    if id not in id_set:
                        id_set.add(id)
                        break
                paciente = Paciente(
                    id=id,
                    nome=fake.name(),
                    idade=fake.random_int(min=1, max=90),
                    telefone=fake.phone_number(), #Como eu faço para gerar um número de telefone estilo (xx) xxxxx-xxxx?
                    data_exame = fake.date_this_month().strftime('%d/%m/%Y'),
                )
                elementos.append(paciente)
            fim = time.time()
            tempo_criar_elementos = fim - inicio
            print()
            print(f'> Tempo para criar {n} elementos de forma ALEATÓRIA: {tempo_criar_elementos:.2f} segundos')
            print()

        else:
            print("... Gerando dados organizados...")
            if lista.qtd > 0:
                ultimo_id = lista.lista[lista.qtd-1].id
            else:
                ultimo_id = 0
            for i in range(n):
                fake = Faker('pt_BR')
                paciente = Paciente(
                    id=ultimo_id+i+1,
                    nome=fake.name(),
                    idade=fake.random_int(min=1, max=90),
                    telefone=fake.phone_number(),
                    data_exame = fake.date_this_month().strftime('%d/%m/%Y'),
                )
                elementos.append(paciente)
            fim = time.time()
            tempo_criar_elementos = fim - inicio
            print()
            print(f'> Tempo para criar {n} elementos de forma ORDENADA/CRESCENTE: {tempo_criar_elementos}')
    
        for paciente in elementos:
            lista.inserir_final(paciente)

    @staticmethod
    def salvar_arquivo(lista,nome):
        import csv as csv
        import os.path as path
        if path.exists(nome + '.csv'):
            with open(nome + '.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo)
                for i in range(lista.qtd):
                    writer.writerow([lista.lista[i].id, lista.lista[i].nome, lista.lista[i].idade, lista.lista[i].telefone, lista.lista[i].data_exame])
                print()
                print(f'> Lista salva com sucesso em {nome}.csv!')
                print()
        else:
            with open(nome + '.csv', 'w', newline='') as arquivo:
                writer = csv.writer(arquivo)
                for i in range(lista.qtd):
                    writer.writerow([lista.lista[i].id, lista.lista[i].nome, lista.lista[i].idade, lista.lista[i].telefone, lista.lista[i].data_exame])
                print()
                print(f'> Lista salva com sucesso em {nome}.csv!')
                print()
    @staticmethod
    def listar_arquivos():
        import os as os
        print()
        print('----------------- ARQUIVOS -----------------')
        print()
        for arquivo in os.listdir():
            if arquivo.endswith('.csv'):
                print(arquivo)
        print()

    @staticmethod
    def abrir_arquivo(lista, nome):
        import csv as csv
        import os.path as path
        nome = str(nome)
        if path.exists(nome + '.csv'):
            with open(nome + '.csv', 'r', newline='') as arquivo:
                reader = csv.reader(arquivo)
                for linha in reader:
                    paciente = Paciente(
                        id=int(linha[0]),
                        nome=linha[1],
                        idade=linha[2],
                        telefone=linha[3],
                        data_exame=linha[4],
                    )
                    lista.inserir_final(paciente)
                print()
                print(f'> Lista {nome} aberta com sucesso!')
                print()
        else:
            print()
            print(f'> ERRO: Não existe um arquivo com o nome {nome}!')
            print()

class AlgoritmoDeOrdenacao:
    import time as time
    import random as random


    @staticmethod
    #BUBBLE SORT: Este algoritmo de ordenação compara dois elementos adjacentes da lista e os troca de posição se estiverem na ordem errada.
    def bubble_sort(lista):
        inicio = time.time()
        n = lista.qtd
        for i in range(n-1):
            for j in range(n-1):
                if lista.lista[j].id > lista.lista[j+1].id:
                    lista.lista[j], lista.lista[j+1] = lista.lista[j+1], lista.lista[j]
        fim = time.time()
        tempo_ordenacao = fim - inicio
        print("BUBBLE SORT finalizado com sucesso!")
        print()
        print(f'> Tempo para ordenar a lista com BUBBLE SORT: {tempo_ordenacao:.2f} segundos')
        print()

    @staticmethod
    #SELECTION SORT: Este algoritmo de ordenação percorre a lista e procura o menor elemento. Quando o menor elemento é encontrado, ele é trocado com o primeiro elemento da lista.
    def selection_sort(lista):
        inicio = time.time()
        n = lista.qtd
        for i in range(n-1):
            menor = i
            for j in range(i+1, n):
                if lista.lista[j].id < lista.lista[menor].id:
                    menor = j
            lista.lista[i], lista.lista[menor] = lista.lista[menor], lista.lista[i]
        fim = time.time()
        tempo_ordenacao = fim - inicio
        print("SELECTION SORT finalizado com sucesso!")
        print()
        print(f'> Tempo para ordenar a lista com SELECTION SORT: {tempo_ordenacao:.2f} segundos')
        print()

    @staticmethod
    #INSERTION SORT: Este algoritmo de ordenação percorre a lista e insere cada elemento na posição correta.
    def insertion_sort(lista):
        inicio = time.time()
        n = lista.qtd
        for i in range(1, n):
            j = i
            while j > 0 and lista.lista[j].id < lista.lista[j-1].id:
                lista.lista[j], lista.lista[j-1] = lista.lista[j-1], lista.lista[j]
                j -= 1
        fim = time.time()
        tempo_ordenacao = fim - inicio
        print("INSERTION SORT finalizado com sucesso!")
        print()
        print(f'> Tempo para ordenar a lista com INSERTION SORT: {tempo_ordenacao:.2f} segundos')
        print()
    

def main():
    lista = ListaEstatica()
    while True:
        print()
        print(" //----------------- MENU -----------------//")
        print(' 1 - Cadastrar pacientes')
        print(' 2 - Listar pacientes')
        print(' 3 - Buscar paciente')
	#Obs: Pergunta qual se usuário deseja : Pesquisar um ID, pesquisar o maior ID, pesquisar o menor ID, pesquisar o primeiro paciente da lista ou pequisar o último paciente da lista.
        print(' 4 - Remover paciente')
	#Obs: Pergunta qual se usuário deseja : Remover um ID, Remover o maior ID, Remover o menor ID, Remover o primeiro paciente da lista ou Remover o último paciente da lista.
        print(' 5 - Limpar lista')
	#OBs: Irá limpar a lista atual do menu
        print(' 6 - Salvar em arquivo')
	#Obs: Vai perguntar o usuário qual nome o usuário quer gravar a lista atual do menu e depois disso, vai verificar. Se existir um arquivo com o mesmo nome, o programa deve perguntar se deseja incrementar ou sobrescrever o arquivo.
        print(' 7 - Ler arquivo')
    #Obs: Vai perguntar o usuário se quer que liste os arquivos existentes na pasta do programa e depois disso, vai perguntar qual arquivo o usuário quer abrir ou deseja abrir um arquivo com um nome específico.
        print(' 8 - Ordenar lista')
	#obs: No menu principal, após o usuário escolher ser quer inserir os dados de forma ordenada ou aleatória, o programa deve perguntar se quer ou não utilizar os algoritmos de ordenação.
        print(' 9 - Sair')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
    
            n = int(input('Digite a quantidade de pacientes que deseja cadastrar: '))
            print("---------- ESCOLHA O MODO DE CADASTRO ----------")
            sequencia = input('\nA - Cadastro com sequencia aleatória \nO - Cadastro com sequencia ordenada \n> Digite a opção desejada: ')
            Arquivo.cadastrar_pacientes(lista, n, sequencia)
            print()
            print("### Pacientes cadastrados com sucesso! ###")
            print()
        elif opcao == 2:
            ListaEstatica.imprimir_lista(lista)
        elif opcao == 3:
        
            modo_busca = int(input('\n1 - Pesquisar um ID específico  \n2 - Pesquisar o maior ID \n3 - Pesquisar o menor ID \n4 - Pesquisar o primeiro paciente da lista \n5 - Pesquisar o último paciente da lista \n6 - Retornar ao menu \n> Digite o modo de busca: '))
            if modo_busca == 1:
                print()
                id = int(input('Digite o ID do paciente que deseja buscar: '))
                print()
                inicio = time.time()
                ListaEstatica.buscar_por_id(lista, id)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 2:
                print()
                inicio = time.time()
                ListaEstatica.buscar_maior_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 3:
                print()
                inicio = time.time()
                ListaEstatica.buscar_menor_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 4:
                print()
                inicio = time.time()
                ListaEstatica.buscar_primeiro(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 5:
                print()
                inicio = time.time()
                ListaEstatica.buscar_ultimo(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 6:
                continue
            else:
                print('Opção inválida!')
            
        elif opcao == 4:
            modo_exlusao = int(input('\n1 - Remover um ID específico  \n2 - Remover o maior ID \n3 - Remover o menor ID \n4 - Remover o primeiro paciente da lista \n5 - Remover o último paciente da lista \n6 - Retornar ao menu \n> Digite o modo de exclusão: '))
            if modo_exlusao == 1:
                print()
                id = int(input('Digite o ID do paciente que deseja remover: '))
                print()
                inicio = time.time()
                ListaEstatica.remover_por_id(lista, id)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 2:
                print()
                inicio = time.time()
                ListaEstatica.remover_maior_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 3:
                print()
                inicio = time.time()
                ListaEstatica.remover_menor_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 4:
                print()
                inicio = time.time()
                ListaEstatica.remover_primeiro(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 5:
                print()
                inicio = time.time()
                ListaEstatica.remover_ultimo(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 6:
                continue
            else:
                print('Opção inválida!')

        elif opcao == 5:
            print()
            inicio = time.time()
            ListaEstatica.remover_todos(lista)
            fim = time.time()
            tempo = fim - inicio
            print()
            print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
            print()
        elif opcao == 6:
            nome = input("Digite o nome do arquivo que deseja salvar: ")
            Arquivo.salvar_arquivo(lista, nome)

        elif opcao == 7:
            while True:
                modo_abertura = int(input('\n1 - Listar os arquivos existentes na pasta do programa \n2 - Abrir um arquivo com um nome específico \n3 - Retornar ao menu \nDigite o modo de abertura: '))
                if modo_abertura == 1:
                    Arquivo.listar_arquivos()
                elif modo_abertura == 2:
                    nome = input("Digite o nome do arquivo que deseja abrir: ")
                    Arquivo.abrir_arquivo(lista, nome)
                    break
                elif modo_abertura == 3:
                    break
                else:
                    print('Opção inválida!')
        elif opcao == 8:
            print()
            algoritmo = int(input('1 - Bubble Sort\n2 - Selection Sort\n3 - Insertion Sort\n4 - Retornar ao menu \nEscolha o algoritmo de ordenação: '))
            if algoritmo == 1:
                AlgoritmoDeOrdenacao.bubble_sort(lista)
            elif algoritmo == 2:
                AlgoritmoDeOrdenacao.selection_sort(lista)
            elif algoritmo == 3:
                AlgoritmoDeOrdenacao.insertion_sort(lista)
            elif algoritmo == 4:
                continue

        elif opcao == 9:
            print('Saindo...')
            break

           

if __name__ == '__main__':
    main()