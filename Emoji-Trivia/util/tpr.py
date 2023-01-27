import mysql.connector 
db = mysql.connector.connect(host = "localhost",port = "3308",username = "root",password = "",db = "emojigame")

# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = "SELECT * FROM word WHERE id = 1"
cursor.execute(sql)

results = cursor.fetchall()
for r in results:
    print(r)