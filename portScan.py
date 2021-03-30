if __name__ == '__main__':
    exit(0)

import os
from easysnmp import Session,SNMPVariable
from tabulate import tabulate

known_tcp = ['.1.3.6.1.2.1.6.13.1.1']#,'.1.3.6.1.2.1.4.20']
known_udp = ['.1.3.6.1.2.1.7.7.1']

def valueBuild(str1):
    if str1 == '2':
        return "listen"
    elif str1 == '5':
        return 'established'
    elif str1 == '8':
        return 'close_wait'
    else:
        return str1

def list_to_string(list1):
    strr=""
    for l in list1:
        strr+=l+"."
    return strr[:-1]

def varreduraPortas(ip='',protocols=[]):
    
    session = Session(
        hostname=ip,
        community='public',
        version=3,
        security_username='bootstrap',
        auth_password='udescUdesc',
        privacy_password='udescUdesc',
        security_level='authPriv',
        auth_protocol='MD5',
        privacy_protocol="DES")

    for p in protocols:
        print("Over",p)
        query = []
        query_oid=''
        if p.lower() == 'tcp' or p.lower() == '-tcp':
            for oid in known_tcp:
                try:
                    query = session.walk(oid)
                    query_oid=oid
                except SystemError as ex:
                    pass
                except Exception as ex:
                    print(ex)
                if len(query) > 0:
                    break
                else:
                    print("query empty for",oid,end="\n\n")
            rm_oid = len(query_oid)+2
            table = []
            for variable in query:
                #variable = SNMPVariable()
                spl_1 = variable.oid[rm_oid:].split(".")
                table.append([
                    list_to_string(spl_1[0:4]),
                    list_to_string(spl_1[4:5]),
                    list_to_string(spl_1[5:9]),
                    list_to_string(spl_1[9:10]),
                    valueBuild(variable.value)])
            print(tabulate(table, headers=['IP LOCAL', 'PORTA (local)','REMOTO','PORTA (remoto)','SNMP TYPE']))


        if p.lower() == 'udp' or p.lower() == '-udp':
            for oid in known_udp:
                try:
                    query = session.walk(oid)
                    query_oid=oid
                except SystemError as ex:
                    pass
                except Exception as ex:
                    print(ex)
                if len(query) > 0:
                    break
                else:
                    print("query empty for",oid,end="\n\n")

            rm_oid = len(query_oid)+2
            table = []
            for variable in query:
                #variable = SNMPVariable()
                spl_1 = variable.oid[rm_oid:].split(".")
                table.append([
                    #.1.3.6.1.2.1.7.7.1
                    #.1.3.6.1.2.1.7.7.1.8.1.4.0.0.0.0.161.1.4.0.0.0.0.0.26191
                    list_to_string(spl_1[0:7]),
                    list_to_string(spl_1[7:8]),
                    list_to_string(spl_1[8:15]),
                    list_to_string(spl_1[15:16]),
                    valueBuild(variable.value)])
            print(tabulate(table, headers=['IP LOCAL', 'PORTA (local)','REMOTO','PORTA (remoto)','SNMP TYPE']))