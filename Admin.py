import stdiomask #To hide password
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='test',database='supermarket')
mycursor=mydb.cursor()
def admin():
    LoginId=0
    a=input('''
    You are the Admin
    * If you want to update Stocks press 1 *
    * If you want to update Categories press 2 *
    * If you want to update Products press 3 *
    * If you want to Add User press 4 *
    * If you want to Remove User press 5 *
    * If you want to log out press 6 *
    * Please enter:''')
    print()
    if a =='1':
        print ("{:<5} {:<25} {:<15} {:<15} {:<10} {:<15}".format('Id','Name','CategoryId','Price','Active','Stock'))#to format the data
        mycursor.execute("Select * from product")
        lis=mycursor.fetchall()
        for v in lis:
            Id,Name,CategoryId,Price,Active,Stock = v
            print ("{:<5} {:<25} {:<15} {:<15} {:<10} {:<15}".format(Id,Name,CategoryId,Price,Active,Stock))#formating
        print()
        pi=input("Enter the product id of item's stock to be updated:")
        try:
            stk=int(input("Enter the updated stock :"))
        except ValueError:
            print('Enter the correct value')
            stk=int(input("Enter the updated stock :"))
        q="Update product set stock= "+str(stk)+" where Id= " +pi
        mycursor.execute(q)
        mydb.commit()
        p="Update product set active=0 where stock=0"
        mycursor.execute(p)
        mydb.commit()
        a="Update product set active=1 where stock<0"
        mycursor.execute(a)
        mydb.commit()
        print('UPDATED')
        admin()
    elif a =='2':
        mycursor.execute("Select * from Category")
        bis=mycursor.fetchall()
        print('{:<5} {:<20}'.format('Id','Category'))#to format
        for i in bis:
            Id,Category=i
            print('{:<5} {:<20}'.format(Id,Category))#formating
        c=input('''
        * If you want to add Category press 1 *
        * If you want to delete Category press 2 *
        * Please enter:''')
        print('----------------------------------------------')
        if c=='1':
            cat=input("Enter the category name :")
            mycursor.execute("insert into Category(Category) VALUES ('"+str(cat)+"')")
            mydb.commit()
            print('Category created ')
            mycursor.execute("select id from category where category='{}'".format(cat))
            t=mycursor.fetchall()
            for x in t:
                print('Category id is ',x)
            print()
        elif c=='2':
            try:
                dele=int(input("Enter the id of category to be removed :"))
            except ValueError:
                print('Enter the correct value')
                dele=int(input("Enter the id of category to be removed :"))
            mycursor.execute("Delete from category where Id="+str(dele))
            mydb.commit()
            print("Category deleted")
            admin()
        else:
            print('Invalid Choice')
        admin()
    elif a =='3':
        mycursor.execute("Select * from Product")
        dis=mycursor.fetchall()
        print ("{:<5} {:<25} {:<15} {:<15} {:<10} {:<15}".format('Id','Name','CategoryId','Price','Active','Stock'))#to format the data
        for i in dis:
            Id,Name,CategoryId,Price,Active,Stock = i
            print ("{:<5} {:<25} {:<15} {:<15} {:<10} {:<15}".format(Id,Name,CategoryId,Price,Active,Stock))#formating
        c=input('''
        * If you want to add Product press 1 *
        * If you want to delete Product press 2 *
        * Please enter:''')
        print('----------------------------------------------')
        if c=='1':
            act=1
            pn =input("Enter the product name ")
            try:
                cid=int(input("Enter the category id "))
                rate=float(input("Enter the price per unit"))
                stock=int(input("Enter the stock "))
            except ValueError:
                print('Enter the correct value')
                cid=int(input("Enter the category id "))
                rate=float(input("Enter the price per unit "))
                stock=int(input("Enter the stock "))
            sql_insert_query = """insert into product(ItemName,CategoryId,Price,Active,Stock) VALUES (%s,%s,%s,%s,%s)"""
            tup=(pn,cid,rate,act,stock)
            mycursor.execute(sql_insert_query,tup)
            mydb.commit()
            print('Product Added ')
            mycursor.execute("select id from product where ItemName='{}'".format(pn))
            t=mycursor.fetchall()
            for x in t:
                print('Product id is ',x)
            print('ADDED')
            print()
        elif c=='2':
            try:
                dele=int(input("Enter the id of product to be removed :"))
            except ValueError:
                print('Enter the correct value')
                dele=int(input("Enter the id of product to be removed :"))
            mycursor.execute("Delete from product where Id="+str(dele))
            mydb.commit()
            print("Deleted")
        else:
            print('Invalid Choice')
            admin()
        admin()
    elif a =='4':
        mycursor.execute("Select * from users")
        use=mycursor.fetchall()
        print ("{:<5} {:<10} {:<10} {:<20} {:<25} {:<25} {:<15} {:<10} {:<10} {:<15}".format('Id','Lastname','Firstname','Username','EmailId','Address',
        'Phonenumber','password','Active','Role'))#to format the data
        for i in use:
            Id,Lastname,Firstname,Username,EmailId,Address,Phonenumber,password,Active,Role=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]
            print("{:<5} {:<10} {:<10} {:<20} {:<25} {:<25} {:<15} {:<10} {:<10} {:<15}".format(Id,Lastname,Firstname,Username,EmailId,Address,Phonenumber,
            password,Active,Role))#to format the data'''
            print('--------------------------------------------------------------------------------------------------------------------------------------------')
            FN=input("Enter first name :")
            LN=input("Enter last name :")
            UN=(str.lower(FN)+('.')+str.lower(LN))
            Add=input("Enter your address :")
            Phone=input("Enter valid phone number :")
            Pwd=stdiomask.getpass("Enter password :")#To hide password
            Em=input("Enter email :")
            Act=1
            rol=input("Enter the role (Customer/Admin):")
            sql_insert_query = """insert into users(Lastname,Firstname,Username,EmailId,Address,Phonenumber,password,Active,Role) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            tup=(LN,FN,UN,Em,Add,Phone,Pwd,Act,rol)
            mycursor.execute(sql_insert_query,tup)
            mydb.commit()
            print('User Added')
            mycursor.execute("select id from users where active=1")
            t=mycursor.fetchall()
            for x in t[-1]:
                print(' UserId is :',x)
                q="Update users set active=0 where Id="+str(x)
                mycursor.execute(q)
                mydb.commit()
        admin()
    elif a=='5':
        mycursor.execute("Select * from users")
        use=mycursor.fetchall()
        print ("{:<5} {:<10} {:<10} {:<20} {:<25} {:<25} {:<15} {:<10} {:<10} {:<15}".format('Id','Lastname','Firstname','Username','EmailId','Address',
        'Phonenumber','password','Active','Role'))#to format the data
        for i in use:
            Id,Lastname,Firstname,Username,EmailId,Address,Phonenumber,password,Active,Role=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]
            print("{:<5} {:<10} {:<10} {:<20} {:<25} {:<25} {:<15} {:<10} {:<10} {:<15}".format(Id,Lastname,Firstname,Username,EmailId,Address,Phonenumber,
            password,Active,Role))#to format the data
            print('--------------------------------------------------------------------------------------------------------------------------------------------')
            print()
            try:
                dele=int(input("Enter the id of user to be removed :"))
            except ValueError:
                print('Enter the correct value')
                dele=int(input("Enter the id of user to be removed :"))
            mycursor.execute("Delete from users where Id="+str(dele))
            mydb.commit()
            print('USER IS REMOVED')
            admin()
    elif a=='6':
        q="Update users set active=0 where Id="+str(LoginId)
        mycursor.execute(q)
        mydb.commit()
        print('Closed')
    else:
        print('Invalid Choice')
        admin()
admin()