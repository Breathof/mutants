import sqlite3 as sl


def init_data_base():
    con = sl.connect('adn.db')

    with con:
        con.execute("""
            CREATE TABLE mutants (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                adn JSON,
                UNIQUE(adn)
            );
        """)
        

    with con:
        con.execute("""
            CREATE TABLE humans (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                adn JSON,
                UNIQUE(adn)

            );
        """)

init_data_base()