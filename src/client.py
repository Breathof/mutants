import random
import requests
import json
import threading
import multiprocessing

BASES = ["A","T","C","G"]
MAX_SIZE = 8

PROD_URL='http://18.188.95.255/'
DEV_URL='http://localhost:8080/'
ENV_URL=DEV_URL

def postMutants():
    string = ""
    data = []
    for x in range(MAX_SIZE):
        for y in range(MAX_SIZE):
            string = string + random.choice(BASES)
        data.append(string)
        string = ""
    payload = {"dna": data}    
    response = requests.post(ENV_URL + '/mutant', json=payload)
    print(response)

def getStats():
    response = requests.get(ENV_URL + 'stats')
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
    for x in range(200):
        print(x)
        x = threading.Thread(target=getStats)
        threads.append(x)
        x.start()

def main():
    runGetStats()
    # runPostMutants()

main()
