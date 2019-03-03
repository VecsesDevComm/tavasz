import sqlite3
conn = sqlite3connect('questions.db')

def get_questions():
  cur=.conn.cursor()
  res=cur.execute('select*from questions')
  return res.fetchall()