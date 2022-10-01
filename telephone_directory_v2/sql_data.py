#Работы с базой данных
import sqlite3
import input_data as id

con = sqlite3.connect('data_base.db')
cur = con.cursor()

def print_db(x):
    if x == 1:
        for row in cur.execute('SELECT rowid, *  FROM peoples'):
            print(*row)
    elif x == 2:
        fname = id.name()
        for row in cur.execute(f'SELECT rowid, *  FROM peoples WHERE fname LIKE "{fname}%" '):
            print(*row)
    
    elif x == 3:
        lname = id.last_name()
        for row in cur.execute(f'SELECT rowid, *  FROM peoples WHERE lname LIKE "{lname}%" '):
            print(*row)

    elif x == 4:
        t_phone = id.t_phone()
        for row in cur.execute(f'SELECT rowid, *  FROM peoples WHERE t_phone LIKE "{t_phone}%" '):
            print(*row)
def export(i):
    cur.execute(f'SELECT * FROM peoples WHERE rowid = {i}')
    return cur.fetchone()
def export_xlsx(data,i):
    cur.execute(f'SELECT {data} FROM peoples WHERE rowid = {i}')
    text = str(*cur.fetchone())
    return text

def add_data():
    cur.execute (f"INSERT INTO peoples VALUES ('{id.name()}','{id.last_name()}','{id.t_phone()}')")
    con.commit()

def delete_data(x,z=1):
    if x == 1:
        cur.execute (f"DELETE FROM peoples;")
        con.commit()
    elif x == 2:
        cur.execute (f"DELETE FROM peoples WHERE rowid = {z};")
        con.commit()
def f():#количество строк
    cur.execute('SELECT COUNT(*) FROM peoples')
    count = cur.fetchone()
    for c in count:
        return c

