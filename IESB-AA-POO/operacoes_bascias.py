#Como declarar uma variavel com número no Python
numero1 = 1
numero2 = 2
nome = "João"

#Operações matemáticas básica com Python
soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2
multiplicacao = numero1 * numero2

#Como imprimir uma varivel em tela
print(soma) #Imprime somente o numero em tela.  Note que usamos o comando print simples
print("A soma dos números é " + str(soma)) #Concatenando uma string com numero.  o str transforma o numero para string
                                           #para impressao conjunta
print("A soma dos números é {} ".format(soma)) #A mesma coisa que o acima, porem, usando o format
print("A soma dos números {} e {} é {} ".format(numero1, numero2, soma)) #Outro exemplo
print("{} somou os números {} e {} é o resultado foi {} ".format(nome, numero1, numero2, soma)) #Outro exemplo
print("{0} dividiu {1} por {2} é o resultado foi {3} ".format(nome, numero1, numero2, divisao)) #Outro exemplo ordenando

#Como solicitar um input em tela do usuario
print("Digite qualquer coisa: ")
input_usuario = input() #Aguardo o usuario deigitar algo
print("Você digitou:", input_usuario) #imprimindo o que o usuario digitou

#como declarar uma classe no python
class Classe_teste:
    pass

#como declarar um método
def metodo(argumentos):
   return argumentos

#exemplo de uma classe funcional

class Teste:

    def __init__(self, numero1, numero2):
        self.a = numero1
        self.b = numero2

    def soma(self):
        return self.a + self.b

teste = Teste(10, 5)
imprimir_resultado = print("O resultado do teste da classe é:", teste.soma())