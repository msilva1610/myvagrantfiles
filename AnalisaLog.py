import csv
import os
import socket
import pandas as pd
import numpy

def checkip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def lerlog():
    try:
        with open('conn-dmz.csv', 'r') as f:    
            reader = csv.reader(f, delimiter=' ')
            log_list = list(reader)

        iporigem = []
        ipdestino = []
        for i in log_list:
            iporigem.append(i[3].split(':')[0])
            ipdestino.append(i[6].split(':')[0])

        df = pd.DataFrame({'iporigem': iporigem,
                           'ipdestino': ipdestino,
                           'tot': 0}, columns=['iporigem', 'ipdestino', 'tot'])
                    
        #print(df)
        #groupby(['date','type']).count()['amount']
        #print(df.groupby(['iporigem', 'ipdestino']).count())
        dfg = df.groupby(['iporigem', 'ipdestino']).count()
        
        dfg.to_csv('out.csv')
        
    except Exception as e:
        print('erro: {}'.format(e))
    
lerlog()