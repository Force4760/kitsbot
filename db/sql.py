import sqlite3

def create():
    db = sqlite3.connect("db/doom.db")
    c = db.cursor()
    c.execute("CREATE TABLE servers (id text, prefix text)")
    db.commit()
    db.close()

def getP(_id:str) -> str:
    db = sqlite3.connect("db/doom.db")
    c = db.cursor()
    c.execute("SELECT prefix FROM servers WHERE id = ?",[_id])
    r = c.fetchone()[0]
    db.commit()
    db.close()
    return r

def changeP(_id:str, prefix:str):
    db = sqlite3.connect("db/doom.db")
    c = db.cursor()
    c.execute("UPDATE servers SET prefix = ? WHERE id = ?",[prefix,_id])
    db.commit()
    db.close()

def insert(_id:str):
    db = sqlite3.connect("db/doom.db")
    c = db.cursor()
    c.execute("INSERT INTO servers VALUES (?,'>')",[_id])
    db.commit()
    db.close()

if __name__ == "__main__":
    create()