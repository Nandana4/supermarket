import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='test',database='supermarket')
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE shopping_cart(UserId int NOT NULL,ProductId int NOT NULL,Qty int ,Active boolean ,Date_of_Purchase date,FOREIGN KEY (ProductId) REFERENCES Product(Id ), FOREIGN KEY (UserId) REFERENCES Users(Id))')
mydb.close()
print('Exceuted')
