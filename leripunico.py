import csv
import os
import socket


# for name, age in list.iteritems():    # for name, age in list.items():  (for Python 3.x)
#     if age == search_age:
#         print name


def finddns(searchip):
    for ip, dns in searchip.items():
        if ip == searchip:
            return dns

def lerarqdeips():
    with open('listaipunico.csv', 'r') as f:    
      reader = csv.reader(f, delimiter='|')
      next(reader, None)
      #listaips = list(reader)
      listaips = list(reader)
    
    ListaDns = []
    for i in listaips:
        ListaDns.append({'ip':i[0], 'dns':i[1]})
    #print(ListaDns)

    ip = '200.146.245.97'

    #print(ListaDns[0]['dns'])

    for id in range(len(ListaDns)):
        if ListaDns[id]['ip'] == ip:
            print(ListaDns[id]['dns'])

lerarqdeips()