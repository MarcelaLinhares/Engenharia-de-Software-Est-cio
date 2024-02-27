# TEMA 2: Paradigmas e Linguagem Python

# Módulo 3: Distinguir os paradigmas e suas características

# Função que calcula quantos números pares existem de 0 a n
def conta_numeros_pares(n):
    p = 0
    for num in range(n+1):
        if num % 2 == 0:
            p += 1
    return p

print(conta_numeros_pares(10))

# Mesmo código que o anterior, porém usando o conceito de função recursiva (a função chama ela mesma dentro do código)
def conta_numeros_pares(n):
    if n == 0: return 1  # 0 é par
    elif n % 2 == 0: return 1 + conta_numeros_pares(n - 1)
    else: return conta_numeros_pares(n - 1)

print(conta_numeros_pares(5))


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