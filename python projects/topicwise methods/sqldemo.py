import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="jors",passwd="2048")
mycur = mydb.cursor()
mycur.execute("show databases")
for i in mycur:
	print(i)