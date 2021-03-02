import sqlite3
from sqlite3 import Error
import os

def create_database_known_rumors():
    if os.path.isfile('known_rumors.sqlite'):
        os.remove('known_rumors.sqlite')
    conn = sqlite3.connect('known_rumors.sqlite')
    c = conn.cursor()
    create_table_sql = """CREATE TABLE rumors (id int PRIMARY KEY,l_name1 text,f_name1 text,l_name2 text,f_name2 text,importance integrer,nature text, details text, veracity boolean, l_name3 text, f_name3 text, l_name4 text, f_name4 text)"""
    # create_table_sql = """CREATE TABLE rumors (id int PRIMARY KEY,l_name1 text,f_name1 text,l_name2 text,f_name2 text,importance integrer, id_rumor integrer)"""
    c.execute(create_table_sql)

def add_rumor(l_name1,f_name1,l_name2,f_name2,importance,nature,details,veracity,l_name3,f_name3,l_name4,f_name4):
    # file = nature + "_" + f_name4 + "_" + l_name4 + ".sqlite"
    # con = sqlite3.connect(file)

    #     os.
    conn = sqlite3.connect('known_rumors.sqlite')
    sql = ''' INSERT INTO rumors (l_name1,f_name1,l_name2,f_name2,importance,nature,details,veracity,l_name3,f_name3,l_name4,f_name4) VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    data = (l_name1,f_name1,l_name2,f_name2,importance,nature,details,veracity,l_name3,f_name3,l_name4,f_name4)
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

    sqlite> SELECT
   ...> a.first_name || ' ' || a.last_name AS author_name,
   ...> b.title AS book_title
   ...> FROM author a
   ...> JOIN book b ON b.author_id = a.author_id
   ...> ORDER BY a.last_name ASC;