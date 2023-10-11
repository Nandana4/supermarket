import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="test", database="supermarket")
mycursor=mydb.cursor()
mycursor.execute ('''CREATE TABLE Users
(Id int not null Primary Key AUTO_INCREMENT,
LastName varchar(255),
FirstName varchar(255),
UserName varchar(255),
EmailId varchar(255),
Address varchar(255),
PhoneNumber varchar(50),
Password varchar(20),
Active BOOLEAN,
Role varchar(40))''');
mycursor.execute('INSERT INTO Users VALUES (1,"Rema","Karta","rema.karta","rema@hotmail.com","Thillakam house KRA lane 7","8712673451","F2F_market_admin",0,"Admin")')
mycursor.execute('INSERT INTO Users VALUES (2,"Anu", "Guptha", "anu.guptha", "anu.guptha@test.com","lily gardens,KM Road","92656489267","Ag1987",0,"Customer")')
mycursor.execute('INSERT INTO Users VALUES (3,"Tiya", "George", "tiya.george", "tiya.george@try.com","ace nimbus,kara lane5","9895350929","tiya@86",0,"Customer")')
mycursor.execute('INSERT INTO Users VALUES (4,"Liya ", "Mathew", "liya.mathew", "liya.mathew@test.com","31,nivya road,","92678989267","Mat88",0,"Customer")')
mycursor.execute('INSERT INTO Users VALUES (5,"Taniya", "Cheriyan", "taniya.cheriyan", "taniya.cheriyan@pint.com","leela gardens,infopark rd","8382387999","Tan01",0,"Customer")')
mycursor.execute('INSERT INTO Users VALUES (6,"Alen", "Xavier", "alen.xavier", "alen.xavier@test.com","pearl avenue,RRT Road","9298267765","Xavi47",0,"Customer")')
mydb.commit()
print('Executed')
