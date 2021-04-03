import sqlite3 as sl
import json


def insert_mutant(adn_data):
    con = sl.connect('adn.db')
    sql = 'INSERT INTO mutants (adn) values(?)'
    data = [json.dumps(adn_data["dna"])]
    with con:
        try:
            con.execute(sql, data)
        except:
            print("ADN already in base")

def insert_human(adn_data):
    con = sl.connect('adn.db')
    sql = '''
            INSERT INTO humans (adn) values(?)

          '''
    data = [json.dumps(adn_data["dna"])]
    with con:
        try:
            con.execute(sql, data)
        except:
            print("ADN already in base")

def get_human_count():
    con = sl.connect('adn.db')
    sql = 'SELECT COUNT(1) FROM humans'
    with con:
        return con.execute(sql).fetchone()[0]

def get_mutant_count():
    con = sl.connect('adn.db')
    sql = 'SELECT COUNT(1) FROM mutants'
    with con:
        return con.execute(sql).fetchone()[0]

