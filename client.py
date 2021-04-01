import random
import requests
import json
import threading
import multiprocessing

BASES = ["A","T","C","G"]
MAX_SIZE = 8

def makeRequest():
    string = ""
    data = []
    for x in range(MAX_SIZE):
        for y in range(MAX_SIZE):
            string = string + random.choice(BASES)
        data.append(string)
        string = ""
    payload = {"dna": data}    
    response = requests.post('http://localhost:8080/mutant', json=payload)
    print(response)

def main():
    threads = list()
    for x in range(1000000):
        print(x)
        x = threading.Thread(target=makeRequest)
        threads.append(x)
        x.start()

main()
