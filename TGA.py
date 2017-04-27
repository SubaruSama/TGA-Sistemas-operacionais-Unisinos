'''
Definicao TGA:
    Criar um algoritmo que ira gerenciar processos, criando duas filas: uma para processos I/O Bound (que ira cuidar do processamento de IO)
    e uma fila para CPU Bound (que ira cuidar de processamento para a CPU) cada uma tendo o seu quantum (unidade de tempo para uso da CPU).
    Quantum para as filas: I/O Bound = 200 unidades de Quantum
                           CPU Bound = 100 unidades de Quantum
    Cada processo ira seguir a logica de FIFO (First In, First Out), ou seja, o que for criado primeiro ira ser executado.
    Uso da cpu deve ser compartilhado em: 80% para I/O Bound e 20% para CPU Bound
'''

'''
.pop() pode ser atribuido a uma variavel
exemplo: frutas['pera', 'maracuja', 'morango']
ultimo = frutas.pop()
print ultimo # ira sair morango
'''

'''
list serve exatamente como uma estrutura de dado FIFO (First In, First Out). Tudo o que entra primeiro sai primeiro.
'''

import os

# Limpando a tela
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

fila_IO = list() # fila de nomes dos nomes de bound tipo IO
fila_quantum_IO = list() # fila de quantum dos processos de bound tipo IO
fila_CPU = list() # fila de quantum dos nomes de bound tipo CPU
fila_quantum_CPU = list() # fila de quantum dos processos de bound tipo CPU
quantum_IO, quantum_CPU = 100, 200

def processamento_fila(nomeProcesso, quantum, tipoProcesso):
    '''
        Testing
    '''

    # Tipo Processo:
    # I = I/O Bound
    # C = CPU bound
    if tipoProcesso == 'I' or tipoProcesso.lower() == 'i': # THE EVIL IS LAUGHING AT ME; sem o metodo lower(), nao entra certo nas filas. com o metodo lower(), entra. vai saber...
        fila_IO.append(nomeProcesso)
        fila_quantum_IO.append(quantum)
    elif tipoProcesso == 'C' or tipoProcesso.lower() == 'c': # THE EVIL IS LAUGHING AT ME; sem o metodo lower(), nao entra certo nas filas. com o metodo lower(), entra. vai saber...
        fila_CPU.append(nomeProcesso)
        fila_quantum_CPU.append(quantum)
    else:
        print("Bound desconhecido")

    print("FIla IO: {} Fila IO quantum: {}".format(fila_IO, fila_quantum_IO))
    print("Fila CPU: {} Fila CPU quantum: {}".format(fila_CPU, fila_quantum_CPU))
    return

while True:
    print("Devera seguir a ordem: Nome do processo,Quantum,Tipo do processo")
    processos = raw_input() # Devera seguir a ordem: Nome do processos,unidades de tempo (quantum),Bound type

    if processos != 'X':
        splitted_processos = processos.split(',')
        nome_processo = splitted_processos[0]
        quantum_processo = splitted_processos[1]
        tipo_processo = splitted_processos[2]

        processamento_fila(nome_processo, quantum_processo, tipo_processo)
    else:
        print("Exiting. Bye...")