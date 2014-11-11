#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ptc
from tp3_config import SERVER_IP, SERVER_PORT, TRANSFER_DATA, TRANSFER_CHUNK_SIZE
import time

def main():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")

    with ptc.Socket() as client_sock:
        client_sock.connect((SERVER_IP, SERVER_PORT), timeout = 30)
        client_sock.shutdown(ptc.SHUT_WR)
        client_sock.protocol.set_ack_drop_rate(0.05)
        client_sock.protocol.set_ack_delay(0.01)
        data_received = ''
        while len(data_received) < len(TRANSFER_DATA):
          data_received += client_sock.recv(TRANSFER_CHUNK_SIZE)
          print len(data_received), ' out of ', len(TRANSFER_DATA), 'bytes received.\r',
        print ''
        time.sleep(1) # sin este sleep se queda bloqueado el server (??)

if __name__ == '__main__':
    main()