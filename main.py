import sys

if __name__ == '__main__':
    addr = '127.0.0.1'
    port = '*'
    protocol = ['-TCP','-UDP']
    parameter_list = sys.argv

    if len(parameter_list) == 3:
        addr = parameter_list[1]
        protocol = [parameter_list[2]]
    elif len(parameter_list) == 2:
        protocol = [parameter_list[1]]

    from portScan import *
    varreduraPortas(addr,protocol)

else:
    exit(0)

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
