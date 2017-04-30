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

fila_IO_nome = [] # fila de nomes dos nomes de bound tipo IO
fila_quantum_IO = [] # fila de quantum dos processos de bound tipo IO
fila_CPU_nome = [] # fila de quantum dos nomes de bound tipo CPU
fila_quantum_CPU = [] # fila de quantum dos processos de bound tipo CPU
fila_tipo_processo = []
quantum_IO, quantum_CPU = 100, 200

def preencher_fila(nomeProcesso, quantum, tipoProcesso):

    '''Essa funcao esta errada. Modificar essa funcao para que encha a fila. Criar uma funcao que processe o conteudo das filas'''

    # Tipo Processo:
    # I = I/O Bound
    # C = CPU bound
    if tipoProcesso.upper() == 'I' or tipoProcesso.lower() == 'i': # THE EVIL IS LAUGHING AT ME; sem o metodo lower(), nao entra certo nas filas. com o metodo lower(), entra. vai saber...
        fila_IO_nome.append(nomeProcesso)
        fila_quantum_IO.append(quantum)
        fila_tipo_processo.append(tipoProcesso.upper())
    elif tipoProcesso.upper() == 'C' or tipoProcesso.lower() == 'c': # THE EVIL IS LAUGHING AT ME; sem o metodo lower(), nao entra certo nas filas. com o metodo lower(), entra. vai saber...
        fila_CPU_nome.append(nomeProcesso)
        fila_quantum_CPU.append(quantum)
        fila_tipo_processo.append(tipoProcesso.upper())
    else:
        print("Bound desconhecido")

    print("\nFIla IO: {}\t Fila IO quantum: {}\n".format(fila_IO_nome, fila_quantum_IO))
    print("\nFila CPU: {}\t Fila CPU quantum: {}\n".format(fila_CPU_nome, fila_quantum_CPU))
    print("\nFila TIpo de Processo: {}\n".format(fila_tipo_processo))

    temp = fila_tipo_processo.pop()
    if temp == 'I':
        processar_fila(fila_IO_nome, fila_quantum_IO, quantum_IO)
    elif temp == 'C':
        processar_fila(fila_CPU_nome, fila_quantum_CPU, quantum_CPU)
    return

def processar_fila(*args):
    '''essa funcao recebe como argumento uma lista com um tamanho variavel de argumentos. 
        esta sendo passado listas (arrays) como argumentos. args eh uma lista que possue diversas posicoes, sendo que cada posicao possui um valor'''

    '''para poder passar uma lista como argumento, tem que usar o '*' quando estiver passando para a funcao. Exemplo: 
    def someFunction(*args):
        for x in args:
            print x

    eh o mesmo que: 
    def someFunction(myList = [], *args):
        for x in myList:
            print x

    thanks stackoverflow'''

    fila_de_espera = []
    processar_nome_fila = args[0]
    # POG = Programacao orientada a gambiarra CUIDADO NAO TOCAR
    temp = args[1]
    processar_quantum_processo_temp = map(int, temp)
    processar_quantum_processo = processar_quantum_processo_temp[0]
    # POG = Programacao orientada a gambiarra CUIDADO NAO TOCAR
    processar_quantum_max = args[2]

    # Se eu pegar todos os quantum dos processos e fazer a media?

    print("Nome processo: {}\nQuantum fila: {}\nQuantum max: {}\nDict espera: {}".format(processar_nome_fila, processar_quantum_processo, processar_quantum_max, fila_de_espera))
    # Cada vez que essa funcao for chamada, limpar o conteudo dela mas tem como guardar as variaveis temporarias?

while True:
    print("Devera seguir a ordem: Nome do processo,Quantum,Tipo do processo")
    processos = raw_input() # Devera seguir a ordem: Nome do processos,unidades de tempo (quantum),Bound type

    if processos != 'X':
        splitted_processos = processos.split(',')
        nome_processo = splitted_processos[0]
        quantum_processo = splitted_processos[1]
        tipo_processo = splitted_processos[2]

        preencher_fila(nome_processo, quantum_processo, tipo_processo)
    else:
        print("Exiting. Bye...")