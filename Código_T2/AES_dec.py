# 
# Trabalho 2 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------

import numpy as np
import math

from AES_enc import multiplica_por_2, multiplica_por_3

# ------------------------------------------------

def inv_sub_bytes(matriz):
    
    return(matriz)

# ------------------------------------------------

def inv_shift_rows(matriz):
    
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

        resultado_parcial2[0] = multiplica_por_2(int(resultado_parcial1, 16)) ^ multiplica_por_3(int(resultado_parcial1, 16)) ^ int(resultado_parcial1, 16) ^ int(resultado_parcial1, 16) 
        resultado_parcial2[1] = multiplica_por_2(int(resultado_parcial1, 16)) ^ multiplica_por_3(int(resultado_parcial1, 16)) ^ int(resultado_parcial1, 16) ^ int(resultado_parcial1, 16)
        resultado_parcial2[2] = multiplica_por_2(int(resultado_parcial1, 16)) ^ multiplica_por_3(int(resultado_parcial1, 16)) ^ int(resultado_parcial1, 16) ^ int(resultado_parcial1, 16)
        resultado_parcial2[3] = multiplica_por_2(int(resultado_parcial1, 16)) ^ multiplica_por_3(int(resultado_parcial1, 16)) ^ int(resultado_parcial1, 16) ^ int(resultado_parcial1, 16)

        matriztemp[i][0] = multiplica_por_2(int(resultado_parcial2, 16)) ^ multiplica_por_3(int(resultado_parcial2, 16)) ^ int(resultado_parcial2, 16) ^ int(resultado_parcial2, 16) 
        matriztemp[i][1] = multiplica_por_2(int(resultado_parcial2, 16)) ^ multiplica_por_3(int(resultado_parcial2, 16)) ^ int(resultado_parcial2, 16) ^ int(resultado_parcial2, 16)
        matriztemp[i][2] = multiplica_por_2(int(resultado_parcial2, 16)) ^ multiplica_por_3(int(resultado_parcial2, 16)) ^ int(resultado_parcial2, 16) ^ int(resultado_parcial2, 16)
        matriztemp[i][3] = multiplica_por_2(int(resultado_parcial2, 16)) ^ multiplica_por_3(int(resultado_parcial2, 16)) ^ int(resultado_parcial2, 16) ^ int(resultado_parcial2, 16)


    for i in range(4):
        for j in range(4):
            
            elem = (hex(int(matriztemp[i][j]))[2:])
            matriz[i][j] = elem

    return matriz

# ------------------------------------------------

def dec_aes_ecb(key, string, qntd_iteracoes):
    
    return string

# ------------------------------------------------