
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
        print("/----------- PACIENTE ID: ", self.id, "-----------/")
        return f'\nNome: { self.nome } \nIdade: { self.idade } \nTelefone: { self.telefone } \nData do exame: { self.data_exame }\n'
    
    def get_id(self):
        return self.id
    
class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.direita = None
        self.esquerda = None

######## CLASSE ÁRVORE BINÁRIA DE BUSCA :
class Arvore:
    def __init__(self):
        self.raiz = None

    def nivel(self):
        return self.nivel_rec(self.raiz)
    
    def nivel_rec(self, no_atual):
        if no_atual == None:
            return 0
        else:
            esquerda = self.nivel_rec(no_atual.esquerda)
            direita = self.nivel_rec(no_atual.direita)
            return 1 + (esquerda if esquerda > direita else direita)
        



######### INSERÇÕES:

    def inserir_final(self, valor):
        no = No(valor)
        if self.isVazia():
            self.raiz = no
        else:
            self.inserir_final_rec(self.raiz, no)

    def inserir_final_rec(self, no_atual, novo_no):
        if no_atual.direita == None:
            no_atual.direita = novo_no
        else:
            self.inserir_final_rec(no_atual.direita, novo_no)

    def inserir_inicio(self, valor):
        no = No(valor)
        if self.isVazia():
            self.raiz = no
        else:
            self.inserir_inicio_rec(self.raiz, no)

    def inserir_inicio_rec(self, no_atual, novo_no):
        if no_atual.esquerda == None:
            no_atual.esquerda = novo_no
        else:
            self.inserir_inicio_rec(no_atual.esquerda, novo_no)

##### IMPRESSÕES:

    def imprimir_arvore_rec(self, no_atual, nivel, pacientes_impressos):
        if no_atual is not None:
            self.imprimir_arvore_rec(no_atual.direita, nivel + 1, pacientes_impressos)
            if no_atual.valor not in pacientes_impressos:
                pacientes_impressos.append(no_atual.valor)
                print(no_atual.valor)
            self.imprimir_arvore_rec(no_atual.esquerda, nivel + 1, pacientes_impressos)

    def imprimir_arvore(self):
        pacientes_impressos = []
        self.imprimir_arvore_rec(self.raiz, 0, pacientes_impressos)

    def imprimir_em_ordem(self):
        self.imprimir_em_ordem_rec(self.raiz)

    def imprimir_em_ordem_rec(self, no_atual):
        if no_atual != None:
            self.imprimir_em_ordem_rec(no_atual.esquerda)
            print(no_atual.valor)
            self.imprimir_em_ordem_rec(no_atual.direita)

##### BUSCAS: 

    def buscar_primeiro(self):
        return self.buscar_primeiro_rec(self.raiz)
    
    def buscar_primeiro_rec(self, no_atual):
        if no_atual == None:
            return print("A árvore está vazia!")
        elif no_atual.esquerda == None:
            return print("ID: ", no_atual.valor.get_id(), "| Nome: ", no_atual.valor.nome, "| Nível da árvore: ", self.nivel())
        else:
            return self.buscar_primeiro_rec(no_atual.esquerda)
        
    def buscar_ultimo(self):
        return self.buscar_ultimo_rec(self.raiz)
    
    def buscar_ultimo_rec(self, no_atual):
        if no_atual == None:
            return print("A árvore está vazia!")
        elif no_atual.direita == None:
            return print("ID: ", no_atual.valor.get_id(), "| Nome: ", no_atual.valor.nome)
        else:
            return self.buscar_ultimo_rec(no_atual.direita)
        
    def buscar_maior_id(self):
        return self.buscar_maior_rec(self.raiz)
    
    def buscar_maior_rec(self, no_atual):
        if no_atual == None:
            return print("A árvore está vazia!")
        elif no_atual.direita == None:
            return print("ID: ", no_atual.valor.get_id(), "| Nome: ", no_atual.valor.nome)
        else:
            return self.buscar_maior_rec(no_atual.direita)
        
    def buscar_menor_id(self):
        return self.buscar_menor_rec(self.raiz)
    
    def buscar_menor_rec(self, no_atual):
        if no_atual == None:
            return print("A árvore está vazia!")
        elif no_atual.esquerda == None:
            return print("ID: ", no_atual.valor.get_id(), "| Nome: ", no_atual.valor.nome)
        else:
            return self.buscar_menor_rec(no_atual.esquerda)
        
    def buscar_id(self, id):
        return self.buscar_id_rec(self.raiz, id)
    
    def buscar_id_rec(self, no_atual, id):
        if no_atual == None:
            return print("ID não encontrado!")
        elif id == no_atual.valor.get_id():
            return print("ID: ", no_atual.valor.get_id(), "| Nome: ", no_atual.valor.nome)
        elif id < no_atual.valor.get_id():
            return self.buscar_id_rec(no_atual.esquerda, id)
        else:
            return self.buscar_id_rec(no_atual.direita, id)

    

            
##### CONTAGEM:

    def contar(self):
        return self.contar_rec(self.raiz)
    
    def contar_rec(self, no_atual):
        if no_atual == None:
            return 0
        else:
            return 1 + self.contar_rec(no_atual.esquerda) + self.contar_rec(no_atual.direita)
        
    def altura(self):
        return self.altura_rec(self.raiz)
    
    def altura_rec(self, no_atual):
        if no_atual == None:
            return 0
        else:
            esquerda = self.altura_rec(no_atual.esquerda)
            direita = self.altura_rec(no_atual.direita)
            return 1 + (esquerda if esquerda > direita else direita)

##### REMOÇÕES:

    def isVazia(self):
        return self.raiz == None
    
    def remover_todos(self):
        self.raiz = None
        print("--- Todos os pacientes foram removidos ---")

    def remover_por_id(self, id):
        self.raiz = self.remover_por_id_rec(self.raiz, id)


######## ARQUIVO:

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
            # Código para gerar dados organizados e ordenados
            print("... Gerando dados organizados...")
            if Arvore.isVazia(lista) == False:
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
                    data_exame=fake.date_this_month().strftime('%d/%m/%Y'),
                )
                elementos.append(paciente)
            inicio = time.time()
            for paciente in elementos:
                Arvore.inserir_final(lista, paciente)
            fim = time.time()
            tempo_criar_elementos = fim - inicio
            print()
            print(f'> Tempo para criar {n} elementos de forma ORDENADA/CRESCENTE: {tempo_criar_elementos}')
    
        for paciente in elementos:
            Arvore.inserir_final(lista, paciente)


######### ARQUIVO:


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
            if Arvore.isVazia(lista) == False:
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
                    data_exame=fake.date_this_month().strftime('%d/%m/%Y'),
                )
                elementos.append(paciente)
            inicio = time.time()
            for paciente in elementos:
                Arvore.inserir_final(lista, paciente)
            fim = time.time()
            tempo_criar_elementos = fim - inicio
            print()
            print(f'> Tempo para criar {n} elementos de forma ORDENADA/CRESCENTE: {tempo_criar_elementos}')

        for paciente in elementos:
            Arvore.inserir_final(lista, paciente)

            



    @staticmethod
    def salvar_arquivo(lista, nome):
        import csv as csv
        import os.path as path
        if path.exists(nome + '.csv'):
            with open(nome + '.csv', 'a', newline='') as arquivo:
                #LEMBRE-SE QUE É UMA ARVOREB BINÁRIA DE BUSCA:
                write = csv.writer(arquivo)
                write.writerow([lista.paciente.id, lista.paciente.nome, lista.paciente.idade, lista.paciente.telefone, lista.paciente.data_exame])
                print()
                print(f'> Paciente {lista.paciente.nome} salvo com sucesso!')


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




######## MENU :

def main():
    lista = Arvore()
    while True:
        print()
        print(" //----------------- MENU -----------------//")
        print(' 1 - Cadastrar pacientes')
        print(' 2 - Listar pacientes')
        print(' 3 - Buscar paciente')
        print(' 4 - Limpar lista')
        print(' 5 - Sair')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            n = int(input('Digite a quantidade de pacientes que deseja cadastrar: '))
            print("---------- ESCOLHA O MODO DE CADASTRO ----------")
            sequencia = input('\nA - Cadastro com sequencia aleatória \nO - Cadastro com sequencia ordenada \n> Digite a opção desejada: ')
            Arquivo.cadastrar_pacientes(lista, n, sequencia)
            print()
            print("#### Pacientes cadastrados com sucesso! ####")
            print()
        elif opcao == 2:
            Arvore.imprimir_arvore(lista)
        elif opcao == 3:
        
            modo_busca = int(input('\n1 - Pesquisar um ID específico  \n2 - Pesquisar o maior ID \n3 - Pesquisar o menor ID \n4 - Pesquisar o primeiro paciente da lista \n5 - Pesquisar o último paciente da lista \n6 - Retornar ao menu \n> Digite o modo de busca: '))
            if modo_busca == 1:
                print()
                id = int(input('Digite o ID do paciente que deseja buscar: '))
                print()
                inicio = time.time()
                lista.buscar_id(id)
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 2:
                print()
                inicio = time.time()
                lista.buscar_maior_id()
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 3:
                print()
                inicio = time.time()
                lista.buscar_menor_id()
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 4:
                print()
                inicio = time.time()
                lista.buscar_primeiro()
                fim = time.time()
                tempo = fim - inicio
                print()
                print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
                print()
            elif modo_busca == 5:
                print()
                inicio = time.time()
                lista.buscar_ultimo()
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
            print()
            inicio = time.time()
            Arvore.remover_todos(lista)
            fim = time.time()
            tempo = fim - inicio
            print()
            print(f'>> TEMPO DE EXECUÇÃO DESTA OPERAÇÃO: {tempo:.2f} segundos <<')
            print()
        elif opcao == 5:
            print('Saindo...')
            break

           

if __name__ == '__main__':
    main()
