import sqlite3

conn = sqlite3.connect('Assignment1.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

filename = 'mbox.txt'
fh = open(filename)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1].split("@")[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlStr = 'SELECT org, count FROM Counts order by count DESC LIMIT 1'
for row in cur.execute(sqlStr):
    print(str(row[0]), row[1])
cur.close()
