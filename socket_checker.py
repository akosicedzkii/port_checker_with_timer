import socket
import time
import logging


#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def check_port_status(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host,port))
    if result == 0:
        return "Port is open"
    else:
        return "Port is not open"
    sock.close()
counter = 0
while True:
    #print('\x1b[2J')
    port_stat = check_port_status('127.0.0.1',80)
    counter = counter + 1
    time.sleep(1)
    #print(counter)

    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    try:
        logging.warning('This will get logged to a file' + str(counter) + " " + port_stat)
    except:
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning('This will get logged to a file' + str(counter) + " " + port_stat)
