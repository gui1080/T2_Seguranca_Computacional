# 
# Trabalho 2 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------

import numpy as np
import math

from imagem import pega_string_da_imagem

# ------------------------------------------------

# AES encryption (etapas)
# add round key
# sub bytes
# shift rows
# mix columns

def create_input(entrada):
    
    # essa função pega 32 caracteres e retorna a matrix correta de hexadecimais 4x4
    
    x = [entrada[i:i+2] for i in range(0, len(entrada), 2)]

    matriz = np.array(x).reshape(4, 4).T
    
    return matriz

# ------------------------------------------------

def add_round_key(matriz, key):
    
    # o resultado dessa operação aqui é o xor entre a key e a matriz de texto
    
    for i in range(4):
        for j in range(4):
            elem1 = matriz[i][j]
            elem2 = key[i][j]
            
            resultado = int(elem1, 16) ^ int(elem2, 16)
            matriz[i][j] = '{:x}'.format(resultado)
    
    return matriz

# ------------------------------------------------

def sub_bytes(matriz):
    
    # mapeamos da matriz para seu novo elemento correspondente da S_BOX
    
    S_BOX = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
            ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
            ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
            ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
            ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
            ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
            ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
            ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
            ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
            ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
            ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
            ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
            ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
            ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
            ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'cE', '55', '28', 'df'],
            ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]
    
    for i in range(4):
        for j in range(4):
            elem = int(matriz[i][j], 16)
            
            elem_i = math.trunc(elem / 16)
            elem_j = (elem - (elem_i*16))
            
            matriz[i][j] = S_BOX[elem_i][elem_j]
    
    return matriz

# ------------------------------------------------

def shift_rows(matriz):
    #embaralha as colunas: segunda linha uma vez, terceira 2 vezes e quarta linha vezes
    for i in range(3):
        temp0 = matriz[i+1][0]
        temp1 = matriz[i+1][1]
        temp2 = matriz[i+1][2]
        temp3 = matriz[i+1][3]
        matriz[i+1][0]= temp1
        matriz[i+1][1]= temp2
        matriz[i+1][2]= temp3
        matriz[i+1][3]= temp0
        if i>0:
            temp0 = matriz[i+1][0]
            temp1 = matriz[i+1][1]
            temp2 = matriz[i+1][2]
            temp3 = matriz[i+1][3]
            matriz[i+1][0]= temp1
            matriz[i+1][1]= temp2
            matriz[i+1][2]= temp3
            matriz[i+1][3]= temp0
            if i==2:
                temp0 = matriz[i+1][0]
                temp1 = matriz[i+1][1]
                temp2 = matriz[i+1][2]
                temp3 = matriz[i+1][3]
                matriz[i+1][0]= temp1
                matriz[i+1][1]= temp2
                matriz[i+1][2]= temp3
                matriz[i+1][3]= temp0

    return matriz

# ------------------------------------------------

def multiplica_por_2(v):
    s = v << 1
    s &= 0xff
    if (v & 128) != 0:
        s = s ^ 0x1b
    return s


def multiplica_por_3(v):
    return multiplica_por_2(v) ^ v


def mix_columns(matriz):

    matriztemp = matriz.copy()
    
    for i in range(4):
        for j in range(4):
            matriztemp[i][j] = int(matriz[i][j], 16)

    coluna=[0, 0, 0, 0]
    
    for i in range(4):
        
        for j in range(4):
            coluna[j] = matriztemp[i][j]
        
        matriztemp[i][0] = multiplica_por_2(int(coluna[0], 16)) ^ multiplica_por_3(int(coluna[1], 16)) ^ int(coluna[2], 16) ^ int(coluna[3], 16) 
        
        matriztemp[i][1] = multiplica_por_2(int(coluna[1], 16)) ^ multiplica_por_3(int(coluna[2], 16)) ^ int(coluna[3], 16) ^ int(coluna[0], 16)
        
        matriztemp[i][2] = multiplica_por_2(int(coluna[2], 16)) ^ multiplica_por_3(int(coluna[3], 16)) ^ int(coluna[0], 16) ^ int(coluna[1], 16)
        
        matriztemp[i][3] = multiplica_por_2(int(coluna[3], 16)) ^ multiplica_por_3(int(coluna[0], 16)) ^ int(coluna[1], 16) ^ int(coluna[2], 16)

    for i in range(4):
        for j in range(4):
            
            elem = (hex(int(matriztemp[i][j]))[2:])
            matriz[i][j] = elem

    return matriz

# ------------------------------------------------

# SIMPLE AES ENC
# funciona para uma string de tamanho x
# faz AES n vezes para cada subsegmento da string

def aes(key, string, qntd_iteracoes):
    
    # aes recebe a string inteira a ser cifrada
    # deve-se pegar os grupos de 32 numeros, transformar em matriz
    # e fazer isso até a string original acabar
    
    string_final = ""
    
    # tamanho da string (eita)
    tamanho_img = len(string) 

    # arredonda pra baixo
    qtnd_float = tamanho_img / 32
    quantidade = math.floor(qtnd_float) 
    
    key_atual = create_input(key)
    
    for i in range(quantidade):
        
        iteracao = pega_string_da_imagem(string, i)
        
        matriz_atual = create_input(iteracao)
        
        # for j in range(qntd_iteracoes):
        
            # keygen(j) 
        
            # add  round key
        
            # substitute bytes
        
            # shift rows
        
            # mix columns
            
        # string_final = string_final + matriz_to_string(matriz_atual)
        
    
    
    return string_final


# ------------------------------------------------

