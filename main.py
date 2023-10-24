from random import randint
import sys

def gerar_numero():
    numero_aleatorio = randint(1,100)
    print(numero_aleatorio)
    return numero_aleatorio

def verificar_tipo_de_entrada(valor_de_entrada):
    if valor_de_entrada.isdigit():
        valor_de_entrada = int(valor_de_entrada)
        return valor_de_entrada

def verificar_numero(numero,numero_aleatorio):
    if numero == numero_aleatorio:
        print(f'Você Ganhou\n'
              f'Parabéns ! O número era {numero}.')
        sys.exit()

numero_aleatorio_gerado = gerar_numero()

print('-'*40)
print(f"| {'Número Aleatório':^36} |")
print('-'*40)

while True:
    numero_palpite = input('Digite um número: ')
    verificar_numero(verificar_tipo_de_entrada(numero_palpite),numero_aleatorio_gerado)
    
