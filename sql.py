import pyodbc

# server_name = "localhost"

# db_name = "userdb"

# uname = "root"

# upass = "123mpaka8"

conn = pyodbc.connect("Driver={Mysql ODBC 9.0 unicode Driver};"
                      "Server=localhost;"
                      "Database=userdb;"
                      "UID = root;"
                      "PWD= 123mpaka8;"
                      "Trusted_Connection=yes;")

#Query1
cursor = conn.cursor()
cursor.execute("Select * from staff")

res = cursor.fetchall()
for row in res:
    print(row)

conn.close()