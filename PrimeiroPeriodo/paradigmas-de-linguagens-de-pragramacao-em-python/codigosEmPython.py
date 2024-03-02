# TEMA 2: Paradigmas e Linguagem Python

# Módulo 3: Distinguir os paradigmas e suas características

# Função que calcula quantos números pares existem de 0 a n
def conta_numeros_pares(n):
    p = 0
    for num in range(n+1):
        if num % 2 == 0:
            p += 1
    return p

print(conta_numeros_pares(10))  # 6

# Mesmo código que o anterior, porém usando o conceito de função recursiva (a função chama ela mesma dentro do código)
def conta_numeros_pares(n):
    if n == 0: return 1  # 0 é par
    elif n % 2 == 0: return 1 + conta_numeros_pares(n - 1)
    else: return conta_numeros_pares(n - 1)

print(conta_numeros_pares(5))  # 3


# TEMA 3: PYTHON BÁSICO

# Módulo 1: Linguagem Python e suas características

print("Olá, Mundo!")

# variável x tem o valor 5 e é do tipo int
x=5
print(x,type(x))

# Módulo 3: Tipos de dados e expressões em Python

# Tipo "int", underline como separador de milhar
print(type(1_000_000))

# Tipo "Float", com parte inteira e parte decimal, usado para Reais
print(type(50.0))
print(type(2+3+1.0)) # Se tiver apenas um valor "Float", o resultado será do tipo "Float"

# Exponenciação
print(2**3) # 2 elevado à 3 = 8

# Tipo "Bool"
print(2<3) # True

# Operador "Not"
print(not(2<3)) # False

# Delimitadores de String
curso = 'Ensino a Distância';
print(curso.upper()) #'ENSINO A DISTÂNCIA'
print(curso.lower()) #'ensino a distância'
print(curso.split()) #['Ensino', 'a', 'Distância']

# Listas
a=['10']
b=['20']
c=['30']
r=a+b+c
print(f'r={r}')  # r=['10', '20', '30']

r2=a*2+b*3+c*4
print(f'r={r2}')  # r=['10', '10', '20', '20', '20', '30', '30', '30', '30']

# Módulo 4: Atribuição, entrada e saída de dados em Python

# Atribuição Múltipla
x, y = 2, 5
print(x)
print(y)

# Operadores de atribuição compostos
x = 10
x = x + 1 # x += 1
print(x)  # 11

# Troca de variáveis
a = 1
b = 2
# troca de variáveis usando variável auxiliar ‘temp’
temp = a
a = b
b = temp
print(f"O valor da variável a é: {a}") # 2
print(f"O valor da variável b é: {b}") # 1
# troca de variáveis através de atribuição múltipla
a, b = b, a
print(f"O valor da variável a é: {a}") # 1
print(f"O valor da variável b é: {b}") # 2

# Entrada de dados com a função Input()
nome = input('Entre com seu nome: ')  # input trata tudo o que for digitado pelo usuário como uma string
print(nome) 

# Entrada de dados com a função Input() com Eval()
numero = eval(input('Entre com um numero inteiro: ')) # input+eval trata tudo o que for digitado pelo usuário como número
numero = numero + 2
print(numero)

# Cálculo do IMC
peso = eval(input('Digite o seu peso: '))
altura = eval(input('Digite sua altura: ').replace(',', '.')) # a função eval(input()) está interpretando a entrada da altura como uma tupla, por isso tem que substituir "," por "." caso o usuário digite ","
imc = peso/(altura**2)
print('IMC = ', imc) # Valor do IMC conforme cálculo feito a partir dos dados digitados pelo usuário

# Formatação de dados de saída
hora = 10
minutos = 26
segundos = 18
print(f'{hora} : {minutos} : {segundos}')  # 10 : 26 : 18

print('{:4},{:5}'.format(10,100))  # '    10,     100' - 4 espaços em antes do n° 10 e 5 antes do nº 100

# Impressão de sequências
str = 'Hello World'
print(str[0:4])  # Hell
print(str[2:8])  # llo Wo
print(str[::-1]) # dlroW olleH


# TEMA 4: PYTHON ESTRUTURADO

# Módulo 1: Estruturas de decisão e repetição em Python

# As listas do tipo range()
# Simples
print(list(range(3)))  # [0,1,2]
# Não iniciado em zero
print(list(range(2,7)))  # [2,3,4,5,6]
# Indicando início, fim e passo
print(list(range(2,9,3)))  # [2,5,8]

# A sintaxe da estrutura for
for item in range(2, 9, 3):
    print(item)  # 2, 5, 8

# O laço for com uma string
nome = 'Marcela'
for letra in nome:
    print(letra)  # M, a, r, c, e, l, a

# O laço for com várias strings
nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)  # Laura, Lis, Guilherme, Enzo, Arthur

# Estrutura de repetição while
palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

# A instrução break
for num in range(1, 11):
    if num == 5:
        break
    else:
        print(num)
print('Laço encerrado')  # 1, 2, 3, 4, Laço encerrado # Parou no nº 5, imprimiu até nº 4

# A instrução continue
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)  
print('Laço encerrado')  # 1, 2, 3, 4, 6, 7, 8, 9, 10, Laço encerrado # Pula o nº 5

# A instrução pass
for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')  # 1, 3, 5, 7, 9, Laço encerrado # Quando o nº é par ele passa para o Else e imprimi os nº ímpar

# Módulo 2: Conceitos de subprogramas e a sua utilização em Python

# Subprogramas (Funções - def)
escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1  
    s = func1(10)
else:
    def func2(x):
        return x + 2
    s = func2(10)
print(s)  # Se escolher 1 resposta 11, se escolher 2 resposta 12

# Subprogramas aninhados (uma função dentro de outra)
def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = eval(input("Entre com a distancia a ser percorrida em km: \n"))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')

# Funções recursivas (função que chama a si mesma)
def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)

regressiva(3)  # 3, 2, 1, Acabou

# Função recursiva fatorial
def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)
    
print(fatorial(5))  # 120

# Função fatorial com laço for (não recursiva)
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
               fat = fat*x
        return fat
    
print(fatorial(5))  # 120

# Módulo 3: Bibliotecas em Python

# Módulo math (dedicado a operações matemáticas)
import math

x = math.sqrt(5)  # Raiz quadrada de 5
print(x)  # 2.23606797749979

# Módulo time (Usado para implementar contadores temporais)
import time

x = time.time()
print(f'Local time: {time.ctime(x)}')  # String com data e horário local

# Módulo tkinter (Usado para desenvolver interfaces gráficas)
from tkinter import *

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.place(x = 50, y = 100)
janelaPrincipal.mainloop()  # Exibi uma janela com a mensagem da variável text

# Módulo 4: Eventos em Python

# Tratamento de exceções na linguagem Python
# Bloco try/except
try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except:
    print("Entre com o valor numérico e não letras")


# TEMA 5: PYTHON ORIENTADO A OBJETOS
    
# Módulo 2: Orientação a objetos na linguagem Python
    
# Instanciar um novo objeto com método __init__
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

def main():
    c1 = Conta(1,1,"Joao",1000) # Objeto sendo instanciado
    print (f"Nome do titular da conta: {c1.nomeTitular}")
    print (f"Número da conta: {c1.numero}")
    print (f"CPF do titular da conta: {c1.cpf}")
    print (f"Saldo da conta: {c1.saldo}")

if __name__ == "__main__": 
    main()

# Classe sem método construtor
class A():
    def f(self):
        print("foo") 


def main():
    obj_A = A() # Objeto sendo instanciado
    obj_A.f()

if __name__ == "__main__": 
    main()


# TEMA 6: PYTHON EM OUTROS PARADIGMAS
    
# Módulo 1: Linguagem funcional no Python

# Função não pura
valor = 20

def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)

def main():
    numero =int(input("Entre com um número inteiro: \n"))
    multiplica(numero)
    multiplica(numero)

if __name__ == "__main__":
    main()

# Função pura
# (A função multiplica deste script é um exemplo de função pura, pois depende apenas de seus parâmetros para gerar o resultado, 
# e não acessa ou modifica nenhuma variável externa à função e retorna um valor)
valor = 20

def multiplica(valor, fator):
    valor = valor * fator
    return valor

def main():
    numero = int(input("Entre com um número inteiro: \n"))
    print("Resultado", multiplica(valor, numero))
    print("Resultado", multiplica(valor, numero))

if __name__ == "__main__":
    main()

# Funções lambda
# Função para multiplicar dois números:
def multiplicar(a, b):
    return a*b
print(multiplicar(5, 2))  # 10
# Função lambda equivalente é:
print((lambda a, b: a*b)(5, 2))  # 10

# Função lambda e função map
lista = [1, 2, 3, 4, 5]

nova_lista = map(lambda item: item * 3, lista)  # função map e lambda

def main():
    print(list(nova_lista))  # [3, 6, 9, 12, 15]

if __name__ == "__main__":
    main()

# Função lambda e função filter
lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 != 0, lista)

def main():
    print(list(nova_lista))  # [1, 3, 5]

if __name__ == "__main__":
    main()

# Módulo 2: Computação concorrente em Python
    
# Threads e processos
from threading import Thread
from multiprocessing import Process

def funcao_a(nome):
    print(nome)

def main():
    t = Thread(target=funcao_a, args=("Minha Thread",))
    t.start()

    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()

if __name__ == '__main__':
    main()