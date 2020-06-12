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
print(soma) #Imprime somente o numero em tela. Note que usamos o comando print simples
print("A soma dos números é " + str(soma)) #Concatenando uma string com numero. o str transforma o numero para string para impressao conjunta
print("A soma dos números é {} ".format(soma)) #A mesma coisa que o acima, porem, usando o format
print("A soma dos números {} e {} é {} ".format(numero1, numero2, soma)) #Outro exemplo
print("{} somou os números {} e {} é o resultado foi {} ".format(nome, numero1, numero2, soma)) #Outro exemplo
print("{0} dividiu {1} por {2} é o resultado foi {3} ".format(nome, numero1, numero2, divisao)) #Outro exemplo ordenando
