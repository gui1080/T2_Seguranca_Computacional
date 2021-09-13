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
from key_gen import gera_key
from AES_enc import multiplica_por_2, multiplica_por_3, create_input, add_round_key, vira_string

# ------------------------------------------------

def inv_sub_bytes(matriz):
    
     	
    INV_S_BOX = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
                ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
                ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
                ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
                ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
                ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
                ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
                ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
                ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
                ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
                ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
                ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
                ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
                ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
                ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
                ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]
    
    for i in range(4):
        for j in range(4):
            elem = int(matriz[i][j], 16)
            
            elem_i = math.trunc(elem / 16)
            elem_j = (elem - (elem_i*16))
            
            matriz[i][j] = INV_S_BOX[elem_i][elem_j]
    
    return matriz

# ------------------------------------------------

def inv_shift_rows(matriz):
    
    # desfaz os shifts pro lado
    
    temp0 = matriz[1][0]
    temp1 = matriz[1][1]
    temp2 = matriz[1][2]
    temp3 = matriz[1][3]
    
    matriz[1][3] = temp0
    matriz[1][0] = temp3
    
    temp0 = matriz[2][0]
    temp1 = matriz[2][1]
    temp2 = matriz[2][2]
    temp3 = matriz[2][3]
    
    matriz[2][0] = temp1
    matriz[2][1] = temp0
    matriz[2][2] = temp2
    matriz[2][3] = temp3
    
    temp0 = matriz[3][0]
    temp1 = matriz[3][1]
    temp2 = matriz[3][2]
    temp3 = matriz[3][3]
    
    matriz[3][0] = temp0
    matriz[3][1] = temp3
    matriz[3][2] = temp2
    matriz[3][3] = temp1
    
    return matriz

# ------------------------------------------------

def inv_mix_columns(matriz):
    
    # igual ao mix columns normal, porém com 3 mudanças nas colunas no lugar de apenas 1

    matriztemp = matriz.copy()
    
    for i in range(4):
        for j in range(4):
            matriztemp[i][j] = int(matriz[i][j], 16)

    coluna = [0, 0, 0, 0]
    resultado_parcial1 = [0, 0, 0, 0]
    resultado_parcial2 = [0, 0, 0, 0]
    
    for i in range(4):
        
        for j in range(4):
            coluna[j] = matriztemp[i][j]
        
        resultado_parcial1[0] = multiplica_por_2(int(coluna[0], 16)) ^ multiplica_por_3(int(coluna[1], 16)) ^ int(coluna[2], 16) ^ int(coluna[3], 16) 
        resultado_parcial1[1] = multiplica_por_2(int(coluna[1], 16)) ^ multiplica_por_3(int(coluna[2], 16)) ^ int(coluna[3], 16) ^ int(coluna[0], 16)
        resultado_parcial1[2] = multiplica_por_2(int(coluna[2], 16)) ^ multiplica_por_3(int(coluna[3], 16)) ^ int(coluna[0], 16) ^ int(coluna[1], 16)
        resultado_parcial1[3] = multiplica_por_2(int(coluna[3], 16)) ^ multiplica_por_3(int(coluna[0], 16)) ^ int(coluna[1], 16) ^ int(coluna[2], 16)

        resultado_parcial2[0] = multiplica_por_2(int(hex(resultado_parcial1[0])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial1[1])[2:], 16)) ^ int(hex(resultado_parcial1[2])[2:], 16) ^ int(hex(resultado_parcial1[3])[2:], 16) 
        resultado_parcial2[1] = multiplica_por_2(int(hex(resultado_parcial1[1])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial1[2])[2:], 16)) ^ int(hex(resultado_parcial1[3])[2:], 16) ^ int(hex(resultado_parcial1[0])[2:], 16)
        resultado_parcial2[2] = multiplica_por_2(int(hex(resultado_parcial1[2])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial1[3])[2:], 16)) ^ int(hex(resultado_parcial1[0])[2:], 16) ^ int(hex(resultado_parcial1[1])[2:], 16)
        resultado_parcial2[3] = multiplica_por_2(int(hex(resultado_parcial1[3])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial1[0])[2:], 16)) ^ int(hex(resultado_parcial1[1])[2:], 16) ^ int(hex(resultado_parcial1[2])[2:], 16)

        matriztemp[i][0] = multiplica_por_2(int(hex(resultado_parcial2[0])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial2[1])[2:], 16)) ^ int(hex(resultado_parcial2[2])[2:], 16) ^ int(hex(resultado_parcial2[3])[2:], 16) 
        matriztemp[i][1] = multiplica_por_2(int(hex(resultado_parcial2[1])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial2[2])[2:], 16)) ^ int(hex(resultado_parcial2[3])[2:], 16) ^ int(hex(resultado_parcial2[0])[2:], 16)
        matriztemp[i][2] = multiplica_por_2(int(hex(resultado_parcial2[2])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial2[3])[2:], 16)) ^ int(hex(resultado_parcial2[0])[2:], 16) ^ int(hex(resultado_parcial2[1])[2:], 16)
        matriztemp[i][3] = multiplica_por_2(int(hex(resultado_parcial2[3])[2:], 16)) ^ multiplica_por_3(int(hex(resultado_parcial2[0])[2:], 16)) ^ int(hex(resultado_parcial2[1])[2:], 16) ^ int(hex(resultado_parcial2[2])[2:], 16)


    for i in range(4):
        for j in range(4):
            
            elem = (hex(int(matriztemp[i][j]))[2:])
            matriz[i][j] = elem

    return matriz

# ------------------------------------------------

def dec_aes_ecb(key, string, qntd_iteracoes):
    
    # aes recebe a string inteira a ser cifrada
    # deve-se pegar os grupos de 32 numeros, transformar em matriz
    # e fazer isso até a string original acabar
    
    string_final = ""
    
    # tamanho da string 
    tamanho_img = len(string) 

    # arredonda pra baixo
    qtnd_float = tamanho_img / 32
    quantidade = math.floor(qtnd_float) 
    
    for i in range(quantidade):
        
        iteracao = pega_string_da_imagem(string, i)
        
        matriz_atual = create_input(iteracao)
        
        key_atual = create_input(key)
                
        if(i == 0):
            print("\n\nPasso a passo, exemplo para primeira iteração da primeira parte da string")
            print("Key:")
            print(key_atual)
            print("Matriz atual:")
            print(matriz_atual)
        
        for j in range(qntd_iteracoes):
        
            key_atual = gera_key(key_atual, j)
        
            matriz_atual = add_round_key(matriz_atual, key_atual)
            
            if((i == 0) and (j == 0)):
                print("Add round key")
                print(matriz_atual)
        
            matriz_atual = inv_sub_bytes(matriz_atual)
            
            if((i == 0) and (j == 0)):
                print("Inv sub bytes")
                print(matriz_atual)
        
            matriz_atual = inv_shift_rows(matriz_atual)
            
            if((i == 0) and (j == 0)):
                print("Inv shift rows")
                print(matriz_atual)
        
            matriz_atual = inv_mix_columns(matriz_atual)
            
            if((i == 0) and (j == 0)):
                print("Inv mix columns")
                print(matriz_atual)
            
        string_final = string_final + vira_string(matriz_atual)
        
    return string_final


# ------------------------------------------------

# ------------------------------------------------

def dec_aes_ctr(key, string, qntd_iteracoes):
    
    # aes recebe a string inteira a ser cifrada
    # deve-se pegar os grupos de 32 numeros, transformar em matriz
    # e fazer isso até a string original acabar
    
    string_final = ""
    
    # tamanho da string 
    tamanho_img = len(string) 

    # arredonda pra baixo
    qtnd_float = tamanho_img / 32
    quantidade = math.floor(qtnd_float) 
    
    for i in range(quantidade):
        
        iteracao = pega_string_da_imagem(string, i)
        
        matriz_atual = create_input(iteracao)
        
        key_atual = create_input(key)
        
        # lidando com o contador do modo CTR
        # no começo de cada iteração, ele pega a key e soma o contador
        # contador vira string de hexadecimal
        # que então vira matriz 4x4, e passa por um xor da matriz da entrada
        contador = str(hex(i)[2:])
        while(len(contador) != 32):
            temp = '0' + contador
            contador = temp

        contador = create_input(contador)

        matriz_atual = add_round_key(matriz_atual, contador)
        
        if(i == 0):
            print("\n\nPasso a passo, exemplo para primeira iteração da primeira parte da string")
            print("Key:")
            print(key_atual)
            print("Matriz atual:")
            print(matriz_atual)
        
        for j in range(qntd_iteracoes):
        
            key_atual = gera_key(key_atual, j)
        
            matriz_atual = add_round_key(matriz_atual, key_atual)
            
            if((i == 0) and (j == 0)):
                print("Add round key")
                print(matriz_atual)
        
            matriz_atual = inv_sub_bytes(matriz_atual)
            
            if((i == 0) and (j == 0)):
                print("Sub bytes")
                print(matriz_atual)
        
            matriz_atual = inv_shift_rows(matriz_atual)
            
            if((i == 0) and (j == 0)):
                print("Shift rows")
                print(matriz_atual)
        
            matriz_atual = inv_mix_columns(matriz_atual)
            
            if((i == 0) and (j == 0)):
                print("Mix columns")
                print(matriz_atual)
            
        string_final = string_final + vira_string(matriz_atual)
        
    return string_final
