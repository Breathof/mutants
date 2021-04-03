import random
import requests
import json
import threading
import multiprocessing

BASES = ["A","T","C","G"]
MAX_SIZE = 8

def postMutants():
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

def getStats():
    response = requests.get('http://localhost:8080/stats')
    print(response.content)

def runPostMutants():
    threads = list()
    for x in range(1000):
        print(x)
        x = threading.Thread(target=postMutants)
        threads.append(x)
        x.start()

def runGetStats():
    threads = list()
    for x in range(100):
        print(x)
        x = threading.Thread(target=getStats)
        threads.append(x)
        x.start()

def main():
    runGetStats()
    # runPostMutants()

main()
