# Função para adicionar uma pessoa á lista
def adicionar_pessoa(lista, nome, idade, profissao):
    pessoa = {"nome": nome, "idade": idade, "profissao": profissao}
    lista.append(pessoa)

#Função para mostrar as pessoas da lista

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissao: {pessoa['profissao']}")

# Lista para armazenar pessoas
pessoas = []

# Adicionando pessoas em uma lista 
adicionar_pessoa(pessoas, "Ana", 25, "Engenheira")
adicionar_pessoa(pessoas, "Bruno", 30, "Professor")
adicionar_pessoa(pessoas, "Carla", 22, "Médica")
adicionar_pessoa(pessoas ,"Luan" , 35 , "Mecanico")

# Exebir a lista de pessoas
exibir_pessoas(pessoas)