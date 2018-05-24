import csv
import os
import socket


# function to get unique values
def unique(list1):

    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        print (x)

def getHora(hora):
    try:
        hora = str(i[7].split(':')[0])
    except Exception as e:
        return hora

def getipDestino(ip):
    try:
        destino = socket.gethostbyaddr(ip)
        return destino
    except Exception as e:
        return ip

def getipOrigem(ip):
    try:
        iporigem = socket.gethostbyaddr(ip)
        return iporigem[0]
    except Exception as e:
        return ip

def lerlog():
    with open('conn-dmz_sem_virgula.csv', 'r') as f:
      reader = csv.reader(f, delimiter=' ')
      log_list = list(reader)

    novaLista = []
    for i in log_list:
        iporigem = getipOrigem(str(i[3].split(':')[0]))
        ipdestino = getipDestino(str(i[6].split(':')[0]))
        hora = getHora(str(i[8]))
        linha = str(iporigem) + '|' + str(ipdestino) + '|' + str(hora)
        novaLista.append(linha)

    with open('outputdatalog.csv', 'w') as outfile:
        mywriter = csv.DictWriter(outfile)
        mywriter.writeheader()

        for d in novaLista:
            mywriter.writerow(d)

        # for i in novaLista:
        #     print(i)

        #['UDP', 'NTPSYNCEX', '', '172.22.131.5:123', 'INSIDE', '', '172.18.60.54:123', 'idle', '0:00:00', 'bytes', '96', 'flags', '-', '']
        # try:
        #     print('IPORIGEM: {} IPDESTINO: {} HORA: {}'.format(iporigem, ipdestino, hora))
        #     break
        # except Exception as e:
        #     print('error: origem: {} destino: {} erro: {}'.format(iporigem, ipdestino, e))

lerlog()
