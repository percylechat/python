import sqlite3
from sqlite3 import Error
import os

def create_database():
    if os.path.isfile('relations_bazaar.sqlite'):
        os.remove('relations_bazaar.sqlite')
    conn = sqlite3.connect('relations_bazaar.sqlite')
    c = conn.cursor()
    create_table_sql = """CREATE TABLE relations (id int PRIMARY KEY,l_name1 text,l_name2 text,f_name1 text,f_name2 text,family bool,love bool,rel integrer)"""
    c.execute(create_table_sql)
    return conn

def create_relationship(conn, l_name1:str,l_name2:str,f_name1:str,f_name2:str,family:bool,love:bool,rel:int):
    sql = ''' INSERT INTO relations(l_name1,l_name2,f_name1,f_name2,family,love,rel) VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    relation = (l_name1, l_name2, f_name1, f_name2, family, love, rel)
    cur.execute(sql, relation)
    conn.commit()
    return cur.lastrowid

def update_relationship(l_name1:str, l_name2:str, f_name1:str, f_name2:str, rel:int):
    sqlfetch = '''SELECT rel from relations WHERE l_name1=? AND l_name2=? AND f_name1=? AND f_name2=?'''
    sqlupdate = ''' UPDATE relations SET rel=? WHERE l_name1=? ANd l_name2=? AND f_name1=? AND f_name2=?'''
    conn = sqlite3.connect('relations_bazaar.sqlite')
    cur = conn.cursor()
    cur.execute(sqlfetch, (l_name1, l_name2, f_name1, f_name2))
    rep = cur.fetchall()
    rest : int= [lis[0] for lis in rep]
    resti = rest[0]
    res = rel + resti
    cur.execute(sqlupdate, (res, l_name1, l_name2, f_name1, f_name2))
    conn.commit()

def check_relationship(conn, l_name1:str, l_name2:str, f_name1:str, f_name2:str):
    sqlsearch = '''SELECT * FROM relations WHERE l_name1=? AND l_name2=? AND f_name1=? AND f_name2=?'''
    cur = conn.cursor()
    cur.execute(sqlsearch, (l_name1, l_name2, f_name1, f_name2))
    rep = cur.fetchall()
    if not rep:
        return 0
    else:
        return 1