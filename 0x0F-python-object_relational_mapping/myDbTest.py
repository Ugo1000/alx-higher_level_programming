# try:
#     import MySQLdb
#     print("MySQLdb is installed.")
# except ImportError:
#     print("MySQLdb is not installed.")

import mysql.connector

# Establish connection to MySQL database
conn = mysql.connector.connect(
    host="sam-Latitude-5400",
    user="root",
    password="samuel10",
    database="hbtn_0c_0"
)

# Create cursor object
cursor = conn.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM tv_show_genres")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close cursor and connection
cursor.close()
conn.close()
