# 
# Trabalho 2 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------

# pega x grupo de 32 caracteres para ser a string que será encriptada

def pega_string_da_imagem(string_imagem, n):
    
    # n = 0
    # string_imagem[0] até [32]
    # n = 1
    # string_imagem[32] até [32+31]
    # ...
    
    x = n * 32
    y = x + 32
        
    tamanho = len(string_imagem)
    
    # caso o indice não exista
    if(x > tamanho):
        return "00000000000000000000000000000000"
        
    # caso exista, pega aquela porção da imagem
    if(n == 0):
        string_nova = string_imagem[:32]
    
    else:
        string_nova = string_imagem[x:y]
    
    
    # tratar caso deseja-se o grupo de 32 chars final
    # precisa preencher o final da informação com zero para dar 32 no total
    tamanho_string_nova = len(string_nova)
    
    if(tamanho_string_nova < 32):
        restante = 32 - tamanho_string_nova
        
        for i in range(restante):
            string_nova = string_nova + "0"
    
    return string_nova
