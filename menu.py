from alunos import Aluno, listar_alunos, mostrar_aluno

def menu():
    print("""
    -------------------------
          MENU ALUNOS
    -------------------------
    1 - CADASTRAR ALUNO
    2 - MOSTRAR MÉDIA ALUNO
    3 - ALUNO ESPECÍFICO   
    0 - SAIR
    -------------------------
    """)
    
def cadastrar():
    nome = input("Qual o nome do aluno: ")
    media = float(input("Qual a média: "))

    aluno = Aluno(nome, media)
    aluno.salvar()

def mostrar():
    for aluno in listar_alunos():
        aluno.mostrar()

def mostrar_aluno_menu():
    id_aluno = int(input("Qual o ID do aluno? "))
    aluno = mostrar_aluno(id_aluno)
    if aluno:
        aluno.mostrar_id()
    else:
        print("Aluno não encontrado.")

while True:
    menu()
    opçao = input("Escolha uma opção: ")
    if opçao == "0":
        break
    elif opçao == "1": cadastrar()
    elif opçao == "2": mostrar()
    elif opçao == "3": mostrar_aluno_menu()
    else: print("Opção inválida.")