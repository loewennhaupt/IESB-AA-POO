# veja os arquivos .py correspondentes a cada tópico para maiores detalhes.

#Inicio da construcao das Classes

#Uma classe aluno, onde será criada contendo o nome do aluno, a matricula,
#idade e disciplinas associadas;
class Aluno:
    seq = 0
    alunos = []

    def __init__(self, nome, idade, matricula, disciplina):
        self.id = None
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.disciplina = disciplina

    def salvar(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.alunos.append(self)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "{} - {} - {}".format(self.id, self.nome, self.matricula)

    @classmethod
    def all(cls):
        return cls.alunos
        


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

while True:
    Menu()
    user_input = int(input())

    if user_input == 1:
        print("Nome do aluno: ")
        alunoNome = str(input())
        print("Idade do aluno: ")
        alunoIdade = int(input())
        print("Matricula do aluno")
        alunoMatricula = int(input())

        novoAluno = Aluno(alunoNome, alunoIdade, alunoMatricula, None)
        novoAluno.salvar()
        print("Aluno salvo com sucesso")
        print("tecle Enter para continuar")
        input()

    elif user_input == 2:
        print("Selecionado 1")
        print("tecle Enter para continuar")
        input()
    elif user_input == 9:
        break
    else:
        print("Seleção fora das opções")






