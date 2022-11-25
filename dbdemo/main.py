import sqlite3 as sqlite


def getSqliteCur():
    conn = sqlite.connect('test.db')
    cur = conn.cursor()
    return cur


def generateTable():
    sql_text_1 = '''CREATE TABLE scores
           (Name TEXT)'''
    # 执行sql语句
    cur = getSqliteCur()
    cur.execute(sql_text_1)


def insertTable():
    sql_text_2 = "INSERT INTO scores (Name) VALUES ('A');"
    cur = getSqliteCur()
    cur.execute(sql_text_2)
    cur.connection.commit()
    #一定要提交


def getTable():
    sql_text = "SELECT * FROM scores"
    cur = getSqliteCur()
    cur.execute(sql_text)
    h = cur.fetchall()
    return h


def main_test():
    con = sqlite.connect("test.db")
    cur = con.cursor()
    cur.execute()


conn = sqlite.connect("helloDb.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE scores
           (Name TEXT)''')
