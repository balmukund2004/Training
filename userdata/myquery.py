

import mysql.connector

def connection():

	return mysql.connector.connect(

		host = 'database-2.cbq8u2c8s38t.ap-south-1.rds.amazonaws.com',
		user = 'admin',
		password = 'mypassword',
		database = 'golu'

		)

def insertuserdata(n,e,p):

	con = connection()
	cursor = con.cursor()

	qry = 'insert into golula(name,email,phone) values(%s,%s,%s)'
	value = (n,e,p)

	cursor.execute(qry,value)
	con.commit()

	cursor.close()
	con.close()

def fetchuserdata():
	con = connection()
	cursor = con.cursor()
	qry = 'select * from golula'

	cursor.execute(qry)
	data = cursor.fetchall()

	cursor.close()
	con.close()

	return data

def fetchuser_details(id):
	con = connection()
	cursor = con.cursor()
	qry = 'select * from golula where id='+str(id)

	cursor.execute(qry)
	data = cursor.fetchall()

	cursor.close()
	con.close()

	return data 


def update_userdata(n,e,p,id):

	con = connection()
	cursor = con.cursor()

	qry = 'update golula set name=%s,email=%s,phone=%s where id=%s'
	value = (n,e,p,id)

	cursor.execute(qry,value)
	con.commit()

	cursor.close()
	con.close()

def deluserdata(id):

	con = connection()
	cursor = con.cursor()

	qry = 'delete from golula where id='+str(id)

	cursor.execute(qry)
	con.commit()

	cursor.close()
	con.close()


