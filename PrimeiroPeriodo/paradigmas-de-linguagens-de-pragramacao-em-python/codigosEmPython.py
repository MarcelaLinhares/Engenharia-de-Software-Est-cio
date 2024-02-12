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