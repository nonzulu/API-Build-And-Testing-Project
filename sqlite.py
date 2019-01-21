import sqlite3

conn = sqlite3.connect('tutorial.db')

c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS students(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
def data_entry():
    c.execute("INSERT INTO students VALUES(12345, '2019-01-10', 'Python', 8 )")
    conn.commit()
    c.close()
    conn.close()

# def dynamic_data_entry():
#     unix = time.time()
#     date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%D %H:%M:%S'))    
#     keywowrd='Python'
#     value = random.randrange(0,10)
#     c.execute("INSERT INTO students(unix,datestamp, keyword,value) VALUES(?, ?, ?, ?)",
#     (unix, date, kwyword, value))
#     conn.commit()

#     create_table()
#     #data_entry()
#     for i in range(10):
#         dynamic_data_entry()
#         time.sleep(1)
#         c.close()
#         conn.close()