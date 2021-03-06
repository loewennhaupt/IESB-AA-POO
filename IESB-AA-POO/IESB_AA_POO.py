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
        return "{} - {} - {} - {}\n".format(self.id, self.nome, self.idade, self.matricula)

    @classmethod
    def all(cls):
        return cls.alunos
        


#Uma classe chamada disciplinas, onde receberá os dados de nome da disciplina,
#alunos matriculados e o código
class Disciplina:
    seq = 0
    desciplinas = []

    def __init__(self, nome, descricao, codigo):
        self.nome = nome
        self.descricao = descricao
        self.codigo = codigo

    def salvar(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.desciplinas.append(self)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "{} - {} - {} - {}\n".format(self.id, self.nome, self.descricao, self.codigo)

    @classmethod
    def all(cls):
        return cls.desciplinas
    
#classe Menu
class Menu:

    def __init__(self):
        print("##### Menu Principal ######")
        print("---------------------------")
        print(" 1 - Cadastrar Aluno")
        print(" 2 - Listar Alunos")
        print(" 4 - Cadastrar Disciplinas" )
        print(" 5 - Listar Disciplinas" )
        print(" 9 - Sair")
        print("---------------------------")


# Codigo de execução

while True:
    Menu()
    user_input = int(input())

    if  user_input == 1:
        print("Nome do aluno: ")
        alunoNome = str(input())
        print("Idade do aluno: ")
        alunoIdade = int(input())
        print("Matricula do aluno: ")
        alunoMatricula = int(input())

        novoAluno = Aluno(alunoNome, alunoIdade, alunoMatricula, None)
        novoAluno.salvar()
        print("Aluno salvo com sucesso!")
        print("tecle Enter para continuar")
        input()

    elif user_input == 2:
        print(novoAluno.all())
        print("tecle Enter para continuar")
        input()

    elif user_input == 4:
        print("Nome da disciplina: ")
        disciplinaNome = str(input())
        print("Descrição da disciplina: ")
        disciplinaDescricao = str(input())
        print("Código da disciplina: ")
        disciplinaCodigo = int(input())

        novaDisciplina = Disciplina(disciplinaNome, disciplinaDescricao, disciplinaCodigo)
        novaDisciplina.salvar()
        print("Disciplina salva com sucesso!")
        print("tecle Enter para continuar")
        input()

    elif user_input == 5:
        print(novaDisciplina.all())
        print("tecle Enter para continuar")
        input()
    elif user_input == 9:
        break
    else:
        print("Seleção fora das opções")






