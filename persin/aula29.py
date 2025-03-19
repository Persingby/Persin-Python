def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - Novo cadastro")
    print("2 - Ver cadastro")
    print("3 - Sair")
    print("-------------------")

def cadastrar_pessoa(cadastros):
    nome = input("Nome:")
    idade = input("Idade:")
    turma = input("Turma:")
    curso = input("Curso:")
    cadastros.append({"Nome" : Nome, "idade" : idade, "Turma" : turma})
    print("Cadastro realizado com sucesso!")

def ver_cadastro(cadastros):
    if not cadastros:
        print("/n Nenhum cadastro no sistema")
    else:
        print("/n------Lista de cadastros------")

        for i, pessoa in enumerate (cadastros, 1):
            print(f"{i}. nome: {pessoa['nome']}, idade: {pessoa['idade']}, Turma {pessoa['Turma']}, Curso{pessoa['Curso']}")

def main():
    cadastro = [ ]
    while True:
        exibir_menu ()
        opção = input("Escolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa (cadastro)
        elif opção == "2":
            ver_cadastro (cadastro)
        elif opção == "3":
            print ("Obrigado por utilizar nosso sistema!")
            break
        else:
            print("Opção incorreta, tente de novo.")


if__name__ == "__main_":
    main()