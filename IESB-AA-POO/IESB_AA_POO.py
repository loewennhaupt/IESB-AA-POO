# veja os arquivos .py correspondentes a cada tópico para maiores detalhes.

#Inicio da construcao das Classes

#Uma classe aluno, onde será criada contendo o nome do aluno, a matricula,
#idade e disciplinas associadas;
class Aluno:

    def AdicionarAluno(self, name, idade, matricula, discipplina):
        self.name = name
        self.idade = idade
        self.matricula = matricula
        self.disciplina = disciplina

#Uma classe chamada disciplinas, onde receberá os dados de nome da disciplina,
#alunos matriculados e o código
class Disciplina:

    def CadastrarDisciplina(self, nome, descricao, codigo):
        self.nome = nome
        self.descricao = descricao
        self.codigo = codigo
        self.alunosMatriculados


#classe Menu
class Menu:

    def __init__(self):
        print("##### Menu Principal ######")
        print("---------------------------")
        print(" 1 - Cadastrar Aluno")
        print(" 2 - Cadastrar Disciplinas" )
        print(" 9 - Sair")
        print("---------------------------")


# Codigo de execução
import os


while True:
    Menu()
    user_input = int(input())

    if user_input == 1:
        print("Selecionado 1")
        print("tecle Enter para continuar")
        input()
    elif user_input == 2:
        print("Selecionado 1")
        print("tecle Enter para continuar")
        input()
    elif user_input == 3:
        break
    else:
        print("Seleção fora das opções")






