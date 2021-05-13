import sqlite3 as sql

con = sql.connect('subscribers.db')

def __init__():    
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `subscribers` (id integer)")
        cur.close()

def subscribe(id):
    with con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO `subscribers` (id) VALUES ({id})")
        con.commit()
        cur.close()

def unsubscribe(id):
    with con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM `subscribers` WHERE id = {id}")
        con.commit()
        cur.close()

def get_list():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `subscribers`")
        rows = cur.fetchall()
        rows = [x[0] for x in rows]
        cur.close()
        return rows