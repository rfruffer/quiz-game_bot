import sqlite3

patch = 'Table.db'

def createTables():
    conn = sqlite3.connect(patch)
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS Part (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Reporter INTEGER UNIQUE,
        Status TEXT,
        Question_1 INTEGER,
        Question_2 INTEGER,
        Question_3 INTEGER,
        Question_4 INTEGER,
        Question_5 INTEGER,
        Question_6 INTEGER,
        Question_7 INTEGER,
        Question_8 INTEGER,
        Question_9 INTEGER,
        Question_10 INTEGER,
        Total INTEGER
    );
    ''')
    conn.commit()

    c.close()
    conn.close()

def setParticipant(User_id):
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "INSERT OR IGNORE INTO Part (Reporter,Status) VALUES (?,?)"
    c.execute(sql, (User_id,"Awaiting",))
    conn.commit()
    c.close()
    conn.close()

def setTotal(User_id, sum):
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "UPDATE Part SET Total=? where Reporter=?"
    c.execute(sql, (sum, User_id,))
    conn.commit()
    c.close()
    conn.close()

def setStatus(User_id):
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "UPDATE Part SET Status=? where Reporter=?"
    c.execute(sql, ("Successful", User_id,))
    conn.commit()
    c.close()
    conn.close()

def setQuestion(User_id, guest, ball):
    number = "Question_"+ guest
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "UPDATE Part SET %s=? where Reporter=?"%(number)
    c.execute(sql, (ball, User_id,))
    conn.commit()
    c.close()
    conn.close()

def getSum(User_id):
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "SELECT SUM(IFNULL(Question_1, 0) + IFNULL(Question_2, 0) + IFNULL(Question_3, 0) + IFNULL(Question_4, 0) + IFNULL(Question_5, 0) + IFNULL(Question_6, 0) + IFNULL(Question_7, 0) + IFNULL(Question_8, 0) + IFNULL(Question_9, 0) + IFNULL(Question_10, 0)) AS Total FROM Part WHERE Reporter=?"
    c.execute(sql, (User_id,))
    rows = c.fetchone()[0]
    c.close()
    return (rows)

def getQuestion(User_id, guest):
    number = "Question_"+ guest
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "SELECT %s FROM Part WHERE Reporter=?"%(number)
    c.execute(sql, (User_id,))
    rows = c.fetchone()[0]
    c.close()
    return (rows)

def getTotal(User_id):
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "SELECT Total FROM Part WHERE Reporter=?"
    c.execute(sql, (User_id,))
    rows = c.fetchone()[0]
    c.close()
    return (rows)

def getStatus(User_id):
    conn = sqlite3.connect(patch)
    c = conn.cursor()
    sql = "SELECT Status FROM Part WHERE Reporter=?"
    c.execute(sql, (User_id,))
    rows = c.fetchone()[0]
    c.close()
    return (rows)

def getAllData():
    conn = sqlite3.connect(patch)
    # conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = "SELECT Id as Id, Reporter as UserId, Status as Status, Total as Total, IFNULL(Question_1, 0) as Question_1,IFNULL(Question_2, 0) as Question_2,IFNULL(Question_3, 0) as Question_3,IFNULL(Question_4, 0) as Question_4,IFNULL(Question_5, 0) as Question_5,IFNULL(Question_6, 0) as Question_6,IFNULL(Question_7, 0)as Question_7,IFNULL(Question_8, 0) as Question_8, IFNULL(Question_9, 0) as Question_9,IFNULL(Question_10, 0) as Question_10 FROM Part"
    c.execute(sql)
    rows = c.fetchall()
    c.close()
    return (rows)
