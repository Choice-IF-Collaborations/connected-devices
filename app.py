import json
import random
import socket
import sqlite3
import time

# Config
UDP_IP = "127.0.0.1"
UDP_PORT = 5005


def main():
    while True:
        send_payload()
        time.sleep(10)


def send_payload():
    payload = {

    }

    payload = json.dumps(payload)

    print(payload)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(payload, (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    main()
