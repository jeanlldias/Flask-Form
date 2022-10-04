import pymysql
#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="12345678", database="testes", port=3307)
cursor = connection.cursor()

#inserting data to db
def add_text(add_text):
    cursor.execute("INSERT INTO form(ID, name) VALUES (DEFAULT, %s)", (name))
    connection.commit()
    return 1

def get_data():
    cursor.execute("SELECT * FROM form")
    rows = cursor.fetchall()    
    return rows