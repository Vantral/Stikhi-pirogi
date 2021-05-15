import sqlite3 as sql

def __init__():    
    with sql.connect('subscribers.db') as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `subscribers` (id integer)")
        cur.close()

def subscribe(id):
    with sql.connect('subscribers.db') as con:
        cur = con.cursor()
        try:
            cur.execute(f"INSERT INTO `subscribers` (id) VALUES ({id})")
        except sql.IntegrityError:
            pass
        con.commit()
        cur.close()

def unsubscribe(id):
    with sql.connect('subscribers.db') as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM `subscribers` WHERE id = {id}")
        con.commit()
        cur.close()

def get_list():
    with sql.connect('subscribers.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `subscribers`")
        rows = cur.fetchall()
        rows = [x[0] for x in rows]
        cur.close()
        return rows