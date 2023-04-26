############# TRABALHO PARTE 2: LISTA ENCADEADA #############

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
    
######## CLASSE NÓ:
class No:
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None

######## CLASSE LISTA ENCADEADA:
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho
    
    def __str__(self):
        if self.inicio is None:
            return 'Lista vazia'
        no = self.inicio
        lista = ''
        while no is not None:
            lista += str(no.paciente)
            no = no.proximo
        return lista
    
######### INSERÇÕES:
    def inserir_final(self, paciente):
        no = No(paciente)
        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def inserir_inicio(self, paciente):
        no = No(paciente)
        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            no.proximo = self.inicio
            self.inicio = no
        self.tamanho += 1

##### IMPRESSÕES:
    def imprimir_lista(self):
        if self.inicio is None:
            print('>> A lista está vazia! <<')
        no = self.inicio
        while no is not None:
            print(f'---------- PACIENTE ID: {no.paciente.id} ----------')
            print(no.paciente)
            print()
            no = no.proximo

##### BUSCAS:
    def buscar_por_id(lista, id):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        no_atual = lista.inicio
        posicao = 0
        while no_atual is not None:
            if no_atual.paciente.id == id:
                return print(f'---------- PACIENTE DE ID: {id} | POSIÇÃO NA LISTA: {posicao} ----------\n{no_atual.paciente}')
            no_atual = no_atual.proximo
            posicao += 1
        return print(f'Paciente de ID {id} não encontrado na lista.')
    
    
    def buscar_maior_id(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        no_atual = lista.inicio
        maior_id = 0
        while no_atual is not None:
            if no_atual.paciente.id > maior_id:
                maior_id = no_atual.paciente.id
                paciente_maior_id = no_atual.paciente
            no_atual = no_atual.proximo
        print()
        print(" >>> O paciente de maior ID foi encontrado na posição: ", maior_id)
        print(f'---------- PACIENTE ENCONTRADO - ID: {maior_id} ----------\n{paciente_maior_id}')
        print()

        
    
    def buscar_menor_id(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        no_atual = lista.inicio
        menor_id = float('inf')
        while no_atual is not None:
            if no_atual.paciente.id < menor_id:
                menor_id = no_atual.paciente.id
                paciente_menor_id = no_atual.paciente
            no_atual = no_atual.proximo

        print()
        print(" >>> O paciente de menor ID foi encontrado na posição: ", menor_id)
        print(f'---------- PACIENTE ENCONTRADO - ID: {menor_id} ----------\n{paciente_menor_id}')
        print()

    def buscar_primeiro(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        print()
        print(f'---------- PRIMEIRO PACIENTE DA LISTA > ID: {lista.inicio.paciente.id} ----------\n{lista.inicio.paciente}')
        print()

    def buscar_ultimo(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        print()
        print(f'---------- ÚLTIMO PACIENTE DA LISTA > ID: {lista.fim.paciente.id} | POSICAO: {len(lista)-1} ----------\n{lista.fim.paciente}')
        print()

##### REMOÇÕES:
    def remover_por_id(lista, id):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        no_atual = lista.inicio
        anterior = None
        while no_atual is not None:
            if no_atual.paciente.id == id:
                if anterior is not None:
                    anterior.proximo = no_atual.proximo
                else:
                    lista.inicio = no_atual.proximo
                lista.tamanho -= 1
                return print(f'Paciente de ID {id} removido com sucesso!')
            anterior = no_atual
            no_atual = no_atual.proximo
        return print(f'Paciente de ID {id} não encontrado na lista.')
    
    def remover_maior_id(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        no_atual = lista.inicio
        maior_id = 0
        while no_atual is not None:
            if no_atual.paciente.id > maior_id:
                maior_id = no_atual.paciente.id
                paciente_maior_id = no_atual.paciente
            no_atual = no_atual.proximo
        lista.remover_por_id(maior_id)
        print()
        print(" >>> O paciente de maior ID foi removido: ", maior_id)
        print(f'---------- PACIENTE REMOVIDO - ID: {maior_id} ----------\n{paciente_maior_id}')
        print()

    def remover_menor_id(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        no_atual = lista.inicio
        menor_id = float('inf')
        while no_atual is not None:
            if no_atual.paciente.id < menor_id:
                menor_id = no_atual.paciente.id
                paciente_menor_id = no_atual.paciente
            no_atual = no_atual.proximo
        lista.remover_por_id(menor_id)
        print()
        print(" >>> O paciente de menor ID foi removido: ", menor_id)
        print(f'---------- PACIENTE REMOVIDO - ID: {menor_id} ----------\n{paciente_menor_id}')
        print()

    def remover_primeiro(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        print()
        print(f'---------- PRIMEIRO PACIENTE DA LISTA > ID: {lista.inicio.paciente.id} ----------\n{lista.inicio.paciente}')
        print()
        lista.remover_por_id(lista.inicio.paciente.id)

    def remover_ultimo(self):
        if self.tamanho == 0:
            return "A lista está vazia"
        
        paciente = self.fim.paciente
        
        if self.tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            no_atual = self.inicio
            while no_atual.proximo != self.fim:
                no_atual = no_atual.proximo
            no_atual.proximo = None
            self.fim = no_atual
        x = self.tamanho
        self.tamanho -= 1
        return print(f'> O último paciente da lista foi removido com sucesso! \n>> POSICAO: {x}\nID: {paciente.id}\nNome: {paciente.nome}\nIdade: {paciente.idade}')


    def remover_todos(lista):
        if lista.inicio is None:
            return print('>> A lista está vazia! <<')
        lista.inicio = None
        lista.fim = None
        lista.tamanho = 0
        print()
        print(" >>> Todos os pacientes foram removidos da lista!")
        print()


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
                    telefone=fake.phone_number(),
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
            if lista.inicio is not None:
                ultimo_id = lista.fim.paciente.id
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
    def salvar_arquivo(lista, nome):
        import csv as csv
        import os.path as path
        if path.exists(nome + '.csv'):
            with open(nome + '.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo)
                no_atual = lista.inicio
                while no_atual is not None:
                    paciente = no_atual.paciente
                    writer.writerow([paciente.id, paciente.nome, paciente.idade, paciente.telefone, paciente.data_exame])
                    no_atual = no_atual.proximo
        else:
            with open(nome + '.csv', 'w', newline='') as arquivo:
                writer = csv.writer(arquivo)
                no_atual = lista.inicio
                while no_atual is not None:
                    paciente = no_atual.paciente
                    writer.writerow([paciente.id, paciente.nome, paciente.idade, paciente.telefone, paciente.data_exame])
                    no_atual = no_atual.proximo



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
    import faker as faker

    @staticmethod
    #BUBBLE SORT: Este algoritmo de ordenação compara dois elementos adjacentes da lista e os troca de posição se estiverem na ordem errada.
    def bubble_sort(lista):
        inicio = time.time()
        for i in range(lista.tamanho):
            no_atual = lista.inicio
            while no_atual.proximo is not None:
                if no_atual.paciente.id > no_atual.proximo.paciente.id:
                    no_atual.paciente, no_atual.proximo.paciente = no_atual.proximo.paciente, no_atual.paciente
                no_atual = no_atual.proximo
        fim = time.time()
        tempo_ordenar = fim - inicio
        print()
        print(f'> Tempo para ordenar a lista: {tempo_ordenar:.2f} segundos')
        print()

    @staticmethod
    #SELECTION SORT: Este algoritmo de ordenação percorre a lista e procura o menor elemento. Depois de encontrar o menor elemento, ele troca com o primeiro elemento da lista.
    def selection_sort(lista):
        if lista.inicio is None:
            return
        inicio = time.time()
        no_atual = lista.inicio
        while no_atual is not None:
            menor = no_atual
            no_atual2 = no_atual.proximo
            while no_atual2 is not None:
                if no_atual2.paciente.id < menor.paciente.id:
                    menor = no_atual2
                no_atual2 = no_atual2.proximo
            no_atual.paciente, menor.paciente = menor.paciente, no_atual.paciente
            no_atual = no_atual.proximo
        fim = time.time()
        tempo_ordenar = fim - inicio
        print()
        print(f'> Tempo para ordenar a lista: {tempo_ordenar:.2f} segundos')
        print()
        
        

    @staticmethod
    #INSERTION SORT: Este algoritmo de ordenação percorre a lista e insere cada elemento na posição correta.
    def insertion_sort(lista):
        inicio = time.time()
        for i in range(lista.tamanho):
            no_atual = lista.inicio
            while no_atual.proximo is not None:
                if no_atual.paciente.id > no_atual.proximo.paciente.id:
                    no_atual.paciente, no_atual.proximo.paciente = no_atual.proximo.paciente, no_atual.paciente
                no_atual = no_atual.proximo
        fim = time.time()
        tempo_ordenar = fim - inicio
        print()
        print(f'> Tempo para ordenar a lista: {tempo_ordenar:.2f} segundos')
        print()




def main():
    lista = ListaEncadeada()
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
            ListaEncadeada.imprimir_lista(lista)
        elif opcao == 3:
        
            modo_busca = int(input('\n1 - Pesquisar um ID específico  \n2 - Pesquisar o maior ID \n3 - Pesquisar o menor ID \n4 - Pesquisar o primeiro paciente da lista \n5 - Pesquisar o último paciente da lista \n6 - Retornar ao menu \n> Digite o modo de busca: '))
            if modo_busca == 1:
                print()
                id = int(input('Digite o ID do paciente que deseja buscar: '))
                print()
                inicio = time.time()
                ListaEncadeada.buscar_por_id(lista, id)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 2:
                print()
                inicio = time.time()
                ListaEncadeada.buscar_maior_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 3:
                print()
                inicio = time.time()
                ListaEncadeada.buscar_menor_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 4:
                print()
                inicio = time.time()
                ListaEncadeada.buscar_primeiro(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 5:
                print()
                inicio = time.time()
                ListaEncadeada.buscar_ultimo(lista)
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
                ListaEncadeada.remover_por_id(lista, id)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 2:
                print()
                inicio = time.time()
                ListaEncadeada.remover_maior_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 3:
                print()
                inicio = time.time()
                ListaEncadeada.remover_menor_id(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 4:
                print()
                inicio = time.time()
                ListaEncadeada.remover_primeiro(lista)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_exlusao == 5:
                print()
                inicio = time.time()
                ListaEncadeada.remover_ultimo(lista)
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
            ListaEncadeada.remover_todos(lista)
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