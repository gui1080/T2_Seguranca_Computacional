# 
# Trabalho 2 de Segurança Computacional
# Alunos: Guilherme Braga (17/0162290) e Gabriel Moretto (15/0154917)
# UnB, 2021/01
#

# Imports
# ------------------------------------------------

import time     # usado para gerar o nome do arquivo de saída, valor único por execução

# ------------------------------------------------

def salva(msg):
    # parte extra, salvar o resultado por conveniência
    salvar = input("Deseja salvar o resultado em um arquivo de texto?[Y/N]?\n\n")

    if(salvar == 'y' or salvar == 'Y'):

        nome_arquivo = "resultado" + str(time.time())
    
        arquivo = open(nome_arquivo, 'w+')

        arquivo.writelines(msg)

        arquivo.close()

        print("Arquivo salvo!")

    return 0