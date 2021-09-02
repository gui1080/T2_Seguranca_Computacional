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