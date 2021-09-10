# 
# Trabalho 2 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------

import math
from copy import copy

# ------------------------------------------------

def gera_key(key, iteracao):

    if iteracao == 0:
        return key

    # essa função pega a key antiga e gera uma nova key para cada round do AES
    
    # definições
    #----------------------------------------- 
    
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
    
    
    rcon = ['8d', '01', '02', '04', '08', '10', '20', '40', '80', '1b', '36', '6c', 'd8', 'ab', '4d', '9a', 
            '2f', '5e', 'bc', '63', 'c6', '97', '35', '6a', 'd4', 'b3', '7d', 'fa', 'ef', 'c5', '91', '39', 
            '72', 'e4', 'd3', 'bd', '61', 'c2', '9f', '25', '4a', '94', '33', '66', 'cc', '83', '1d', '3a', 
            '74', 'e8', 'cb', '8d', '01', '02', '04', '08', '10', '20', '40', '80', '1b', '36', '6c', 'd8', 
            'ab', '4d', '9a', '2f', '5e', 'bc', '63', 'c6', '97', '35', '6a', 'd4', 'b3', '7d', 'fa', 'ef', 
            'c5', '91', '39', '72', 'e4', 'd3', 'bd', '61', 'c2', '9f', '25', '4a', '94', '33', '66', 'cc', 
            '83', '1d', '3a', '74', 'e8', 'cb', '8d', '01', '02', '04', '08', '10', '20', '40', '80', '1b', 
            '36', '6c', 'd8', 'ab', '4d', '9a', '2f', '5e', 'bc', '63', 'c6', '97', '35', '6a', 'd4', 'b3', 
            '7d', 'fa', 'ef', 'c5', '91', '39', '72', 'e4', 'd3', 'bd', '61', 'c2', '9f', '25', '4a', '94', 
            '33', '66', 'cc', '83', '1d', '3a', '74', 'e8', 'cb', '8d', '01', '02', '04', '08', '10', '20', 
            '40', '80', '1b', '36', '6c', 'd8', 'ab', '4d', '9a', '2f', '5e', 'bc', '63', 'c6', '97', '35', 
            '6a', 'd4', 'b3', '7d', 'fa', 'ef', 'c5', '91', '39', '72', 'e4', 'd3', 'bd', '61', 'c2', '9f', 
            '25', '4a', '94', '33', '66', 'cc', '83', '1d', '3a', '74', 'e8', 'cb', '8d', '01', '02', '04', 
            '08', '10', '20', '40', '80', '1b', '36', '6c', 'd8', 'ab', '4d', '9a', '2f', '5e', 'bc', '63', 
            'c6', '97', '35', '6a', 'd4', 'b3', '7d', 'fa', 'ef', 'c5', '91', '39', '72', 'e4', 'd3', 'bd', 
            '61', 'c2', '9f', '25', '4a', '94', '33', '66', 'cc', '83', '1d', '3a', '74', 'e8', 'cb', '8d']

    #-----------------------------------------  
    # muda o primeiro e o ultimo elemento da primeira coluna
    
    key_final = copy(key)
    
    elem_inicio = key[0][0]
    elem_final = key[0][3]
    
    key_final[0][0] = elem_final
    key_final[0][3] = elem_inicio
    
    #-----------------------------------------
    # primeira coluna na s_box
    
    for i in range(4):
        elem = int(key_final[0][i], 16)
        elem_i = math.trunc(elem / 16)
        elem_j = (elem - (elem_i*16))
        key_final[0][i] = S_BOX[elem_i][elem_j]
        
    #-----------------------------------------
    # xor da primeira coluna
    
    for i in range(4):
        elem1 = key_final[0][i]
        elem2 = key[0][i]
        
        if(i == 0):
            elem3 = rcon[iteracao]
        else:
            elem3 = '00'
        
        resultado = int(elem1, 16) ^ int(elem2, 16) ^ int(elem3, 16)
        key_final[0][i] = '{:x}'.format(resultado)
        
    #-----------------------------------------
    # resto 
    
    j = 1
    
    while(j < 4):
    
        for i in range(4):
            elem1 = key_final[j-1][i]
            elem2 = key[j][i]
            
            
            resultado = int(elem1, 16) ^ int(elem2, 16) 
            key_final[j][i] = '{:x}'.format(resultado)
        
        j = j + 1
        

    return key_final
