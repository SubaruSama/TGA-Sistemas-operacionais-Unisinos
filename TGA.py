'''
Definicao TGA:
    Criar um algoritmo que ira gerenciar processos, criando duas filas: uma para processos I/O Bound (que ira cuidar do processamento de IO)
    e uma fila para CPU Bound (que ira cuidar de processamento para a CPU) cada uma tendo o seu quantum (unidade de tempo para uso da CPU).
    Quantum para as filas: I/O Bound = 200 unidades de Quantum
                           CPU Bound = 100 unidades de Quantum
    Cada processo ira seguir a logica de FIFO (First In, First Out), ou seja, o que for criado primeiro ira ser executado.
    Uso da cpu deve ser compartilhado em: 80% para I/O Bound e 20% para CPU Bound
'''

import os

# Limpando a tela
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

fila_IO = list()
fila_CPU = list()
numero_processos = 0

def processamento_fila(nomeProcesso, quantum, tipoProcesso):
    '''
        Testing
    '''
    # Tipo Processo:
    # I = I/O Bound
    # C = CPU bound
    if tipoProcesso == 'I':
        fila_IO.append(nomeProcesso)
    elif tipoProcesso == 'C':
        fila_CPU.append(nomeProcesso)
    else:
        print("Bound desconhecido")

    print('FUNC: %s %s %s') % (nomeProcesso, quantum, tipoProcesso)
    print("FIla IO: {}".format(fila_IO))
    print("Fila CPU: {}".format(fila_CPU))
    return

filaProcessos = list() # Criacao da fila vazia

while True:
    print("Devera seguir a ordem: Nome do processo,Quantum,Tipo do processo")
    numero_processos = numero_processos + 1
    processos = raw_input() # Devera seguir a ordem: Nome do processos,unidades de tempo (quantum),Bound type

    if processos == 'X':
        print('{}'.format(filaProcessos))
        break

    splitted_processos = processos.split(',')
    nome_processo = splitted_processos[0]
    quantum_processo = splitted_processos[1]
    tipo_processo = splitted_processos[2]

    processamento_fila(nome_processo, quantum_processo, tipo_processo)
    
print fila_CPU