#creating database
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='test')
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE supermarket')
