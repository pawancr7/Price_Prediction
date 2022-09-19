import sqlite3
from venv import create

con = sqlite3.connect("Bengaluru_House_Database.db")
cur = con.cursor()


def insert():
    l = []
    f = open('scripts/Datasets/newnona.csv', 'r')
    c = f.readlines()

    for i in range(1, len(c)-1):
        c[i] = c[i].strip('\n')
        l.append(c[i])

    f = []
    for i in range(len(l)):
        for d in (l[i].split(',')):
            f.append(d)

    i = 0
    j = 0
    for k in range(len(f)):
        j = i+8
        df = (f[i:j+1])
        print(df)
        if f[i:j+1] == []:
            break
        con.executemany(
            "INSERT INTO Bengaluru_House_Data VALUES(?,?,?,?,?,?,?,?,?)", [df])
        i = j
        i += 1

    con.commit()


try:
    cur.execute(
        "CREATE TABLE Bengaluru_House_Data(area_type,availability,location,size,society,total_sqft,bath,balcony,price)")
    insert()

except sqlite3.OperationalError:
    if cur.execute('select * from Bengaluru_House_Data') == []:
        insert()
