# 
# Trabalho 2 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------

import base64
import math
from PIL import Image
import binascii


from AES_enc import create_input, vira_string
from AES_enc import add_round_key, mix_columns, shift_rows, sub_bytes
from AES_enc import enc_aes_ecb, enc_aes_ctr

from AES_dec import inv_sub_bytes, inv_shift_rows, inv_mix_columns
from AES_dec import dec_aes_ecb, dec_aes_ctr

from key_gen import gera_key

from imagem import pega_string_da_imagem

from salvar import salva


# ------------------------------------------------

# pegar do usuário o que é para ser executado!
op = int(input("Que operação realizar?\nResponda com número correspondente.\n\n1- Cifrar (AES ECB)\n2- Decifrar(AES ECB)\n3- Cifrar (AES CTR)\n4- Decifrar (AES CTR)\n"))


if(op == 1):
    
    imagem = input("Entre com o nome da imagem.\nExemplo: 'lenna.png'\n")
    
    # abrindo a imagem
    with open(imagem, "rb") as image2string:
        string_convertida = base64.b16encode(image2string.read())

    # string contendo a imagem
    string_analisada = str(string_convertida, "utf-8").lower()

    # passa a chave
    key = input("Entre com a sua chave\nEspera-se 32 caracteres (HEX)\n")
    key = key.lower()  

    # repetições
    rep = int(input("Entre com o número de repetições desejadas na cifragem!\n"))

    # faz o aes enc
    cifra = enc_aes_ecb(key, string_analisada, rep)
    #print(cifra)
    
    # salva a cifra e a string original num arquivo
    salvar = salva(cifra)
    
    
if(op == 2):
    
    # string contendo a imagem
    string_analisada = input("Entre com a sua mensagem cifrada\n")
    string_analisada = string_analisada.lower()

    # passa a chave
    key = input("Entre com a sua chave\nEspera-se 32 caracteres (HEX)\n")
    key = key.lower() 
    
    # repetições
    rep = int(input("Entre com o número de repetições desejadas na cifragem!\n"))

    # faz o aes dec
    plaintext = dec_aes_ecb(key, string_analisada, rep)
    
    print("PT")
    
    salvar = salva(plaintext)
    
    
if(op == 3):
    
    imagem = input("Entre com o nome da imagem.\nExemplo: 'lenna.png'\n")
    
    # abrindo a imagem
    with open(imagem, "rb") as image2string:
        string_convertida = base64.b16encode(image2string.read())

    # string contendo a imagem
    string_analisada = str(string_convertida, "utf-8").lower()

    # passa a chave
    key = input("Entre com a sua chave\nEspera-se 32 caracteres (HEX)\n")
    key = key.lower()  

    # repetições
    rep = int(input("Entre com o número de repetições desejadas na cifragem!\n"))

    # faz o aes enc ctr
    cifra = enc_aes_ctr(key, string_analisada, rep)
    #print(cifra)
    
    # salva a cifra e a string original num arquivo
    salvar = salva(cifra)
    
if(op == 4):
    
    # string contendo a imagem
    string_analisada = input("Entre com a sua mensagem cifrada\n")
    string_analisada = string_analisada.lower()

    # passa a chave
    key = input("Entre com a sua chave\nEspera-se 32 caracteres (HEX)\n")
    key = key.lower() 
    
    # repetições
    rep = int(input("Entre com o número de repetições desejadas na cifragem!\n"))

    # faz o aes dec
    plaintext = dec_aes_ctr(key, string_analisada, rep)
    
    print("PT")
    
    salvar = salva(plaintext)

# ------------------------------------------------

# strings de exemplo
#a = '5a746f2a4f6e15202e696e642054a46f'
#b = 'a46f15205a746f2a4f6e2e696e642054'
#c = 'd42711aee0bf98f1b8b45de51e415230'
#d = 'd4bf5d30e0b452aeb84111f11e2798e5'


