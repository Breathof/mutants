from flask import Flask, request, jsonify, make_response
from mutant import isMutant, get_adn_ratio, ratio_worker, saveHuman, saveMutant

import sqlite3 as sl
import threading


app = Flask(__name__)
app.config["DEBUG"] = False

mutant_queue = []
human_queue = []


@app.route('/mutant', methods=['POST'])
def checkMutant():
    mutant = isMutant(request.get_json())
    if mutant:
        global mutant_queue
        mutant_queue.append(request.get_json())
        return make_response("Is mutant", 200)
    else:
        global human_queue
        human_queue.append(request.get_json())
        return make_response("Is not mutant", 403)

@app.route('/stats', methods=['GET'])
def get_stats():
    ratio = get_adn_ratio()
    return make_response(ratio, 200)


def worker():
    while True:
        while len(mutant_queue) > 0:
            data = mutant_queue.pop(0)
            saveMutant(data)
        while len(human_queue) > 0:
            data = human_queue.pop(0)
            saveHuman(data)

def init_workers():
    worker_thread = threading.Thread(target=worker)
    worker_thread.start()

def init_server():
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080, backlog=1000000)

def init_ratio_worker():
    ratio_thread = threading.Thread(target=ratio_worker)
    ratio_thread.start()

if __name__ == "__main__":
    init_ratio_worker()
    init_workers()
    init_server()
