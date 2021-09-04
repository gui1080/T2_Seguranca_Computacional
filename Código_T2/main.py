# 
# Trabalho 2 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------
from AES_enc import create_input, sub_bytes
from AES_enc import add_round_key
from AES_enc import shift_rows
from AES_enc import mix_columns

from key_gen import gera_key
# ------------------------------------------------

# strings de exemplo
a = '5a746f2a4f6e15202e696e642054a46f'
b = 'a46f15205a746f2a4f6e2e696e642054'
c = 'd42711aee0bf98f1b8b45de51e415230'
d = 'd4bf5d30e0b452aeb84111f11e2798e5'
# cria matriz e key a partir das strings 
matriz = create_input(a)
key = create_input(b)

# teste com passos do AES ENC
matriz = add_round_key(matriz, key)
matriz = sub_bytes(matriz)

key = gera_key(key, 1)

print("CT")
print(matriz)
print("KEY")
print(key)

print("testes com shiftrows")
matrix=create_input(c)
print(matrix)
matrix=shift_rows(matrix)
print("\n")
print(matrix)

print("testes com mixcolumns")
matrix=create_input(d)
print(matrix)
matrix=mix_columns(matrix)
print("\n")
print(matrix)

#matriz esperada:
#04 e0 48 28
#66 cb f8 06
#81 19 d3 26
#e5 9a 7a 4c