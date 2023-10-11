import stdiomask #To hide password
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='test',database='supermarket')
mycursor=mydb.cursor()
from Admin import admin #To import admin functions
def category():
    print('********** CATEGORIES *************')
    mycursor.execute('select id,Category from category')#To display categories
    c=mycursor.fetchall()
    print('{:<5} {:<20}'.format('Id','Category'))#to format the data
    print('---------------------------')
    for i in c:
        Id,Category=i
        print('{:<5} {:<20}'.format(Id,Category))#formating
    print('---------------------------')
    global a
    a=[]
    for x in c:
        a.append(x[0])#Storibg Category Id
    global y
    try:
        y=int(input('Enter category number:'))
    except ValueError:
        print('Enter the correct value')
        y=int(input(' Enter category number:'))
    if y not in a:
        print('Category doesnt exist')
        print('Enter the correct value')
        y=int(input('Enter category number:'))
    print()
    products()
def products():
    print('*********** PRODUCTS *************')
    print()
    import datetime
    idlist=[]
    global y
    mycursor.execute("select id,ItemName,Price from product where CategoryId='{}'".format(y)+"and active=1")
    c=mycursor.fetchall()
    print ("{:<5} {:<25} {:<15}".format('Id','Name','Price'))#to format the data
    print('--------------------------------------')
    for i in c:
        Id,Name,Price = i
        print ("{:<5} {:<25} {:<15} ".format(Id,Name,Price))#formating
    print('--------------------------------------')
    try:
        proid=int(input('Enter product id:'))
    except ValueError:
        print('Enter the correct value')
        proid=int(input('Enter product id:'))
    for i in c :
        idlist=idlist+list(i)#list of items in the selected category
    a=mycursor.execute("select id,ItemName,Price from product where id='{}'".format(proid))
    b=mycursor.fetchall()
    for i in b:
        if i[0]==proid:#to check if product list
            if proid in idlist:# to check if product is in category
                qt=input('Enter quantity :')
                act=1
                dt=datetime.date.today()
                sql_insert_query = """insert into shopping_cart(Userid,productid,qty,active,date_of_purchase) VALUES (%s,%s,%s,%s,%s)"""
                tup=(LoginId,proid,qt,act,dt)
                mycursor.execute(sql_insert_query,tup)
                mydb.commit()
                y="Update product set stock=stock-{}".format(qt)+" where id="+str(proid)#to reduce stock of item purchased
                mycursor.execute(y)
                print('* Added * ')
                p="Update product set active=0 where stock=0"
                mycursor.execute(p)
                mydb.commit()
                print()
                gocart()
            else:
                print('*Product not found *')
                products()
        else:
            print('* Invalid choice * ')
            products()
def gocart():
    a=input('''
    * If you want to go to cart press 1 *
    * if you want to add more items press 2 *
    Please enter:''')
    print()
    if a=='1':
        cart()
        print('')
    elif a=='2':
        category()
        print('')
    else:
        print('error')
        gocart()
def choice():
    x=input('''
    * Enter 1 to go to main menu *
    * Enter 2 to log out *
    * Please enter:''')
    print()
    if x=='1':
        main()
    elif x=='2':
        q="Update users set active=0 where Id="+str(LoginId)
        mycursor.execute(q)
        mydb.commit()
        mydb.close()
        print('Thank you for shopping with us ')
    else:
        print('Invalid choice')
        choice()
def cart():
    total=0
    shop_list=[]
    print('********** SHOPPING CART *************')
    print ("{:<15} {:<25} {:<10} {:<10}".format('ProductId','ItemName','Quantity','Price'))#to format the data
    mycursor.execute( "Select ProductId,Qty from shopping_cart where active=1 and UserId='{}'".format(LoginId))
    x=mycursor.fetchall()
    mycursor.execute('Select Id,ItemName,Price from Product')
    y=mycursor.fetchall()
    for i in x:
        for j in y:
            if(i[0]==j[0]):
                shop_list=shop_list+[(str(i[0]),str(j[1]),str(i[1]),str(j[2]))]
    for i in shop_list:
        ProductId,ItemName,Quantity,Price=i
        print ("{:<15} {:<25} {:<10} {:<10}".format(ProductId,ItemName,Quantity,Price))#formating
    for z in range(0,len(shop_list),1):
        total=total+(float(shop_list[z][3])*int(shop_list[z][2]))#to calculate total amount
    print('--------------------------------------------------------------')
    print('* Total amouunt :',total,' *' )
    a=input('''
    * If you want to continue shopping press 1 *
    * If you want to remove an item press 2 *
    * If you want checkout press 3 *
    * If you want to log out press 4 *
    Please press:''')
    print()
    if a=='1':
        category()
        print('')
    elif a =='2':
        try:
            dele=int(input("Enter the product id of item to be remove :"))
        except ValueError:
            print('Enter the correct value')
            dele=int(input("Enter the product id of item to be remove :"))
            mycursor.execute("Delete from shopping_cart where ProductId="+str(dele))
        cart()
    elif a=='3':#products are purchased and will removed from the cart
        q="Update shopping_cart set active=0 where UserId='{}'".format(LoginId)
        mycursor.execute(q)
        mydb.commit()
        print(' Thank you for shopping with us ')
        print('''
        Please be ready with change
        Our delivery executive will be at your doorstep shortly
        For order details please check order history''')
        print('--------------------------------------------------------------')
        choice()
    elif a=='4':#products will remain in the cart
        q="Update users set active=0 where Id='{}'".format(LoginId)
        mycursor.execute(q)
        mydb.commit()
        mydb.close()
        print("Thank you for shopping with us ")
    else:
        print('Error')
def history():
    print('******** ORDER HISTORY *************')
    shop_list=[]
    mycursor.execute( "Select ProductId,Qty,Date_of_purchase from shopping_cart where active=0 and UserId='{}'".format(LoginId))
    a=mycursor.fetchall()
    mycursor.execute('Select Id,ItemName,Price from Product')
    b=mycursor.fetchall()
    print (" {:<25} {:<10} {:<10} {:<15}".format('ItemName','Quantity','Price','Date'))#to format
    for i in a:
        for j in b:
            if(i[0]==j[0]):
                shop_list=shop_list+[(str(j[1]),str(i[1]),str(j[2]),str(i[2]))]
    for i in shop_list:
        ItemName,Quantity,Price,Date=i
        print (" {:<25} {:<10} {:<10} {:<15}".format(ItemName,Quantity,Price,Date))#formating
def login():
    global LoginId
    print("* To Register press 1 *")
    print("* To Login press 2 *")
    print("* To Logout 3 *")
    ch=input("Please Enter:")
    if ch=='1':#to add a new user
        FN=input("Enter first name :")
        LN=input("Enter last name :")
        UN=(str.lower(FN)+('.')+str.lower(LN))
        Add=input("Enter your address :")
        Phone=input("Enter valid phone number :")
        Pwd=stdiomask.getpass("Enter password :")#to hide the password
        Em=input("Enter email :")
        Act=1
        rol="Customer "
        sql_insert_query = """insert into users(Lastname,Firstname,Username,EmailId,Address,Phonenumber,password,Active,Role) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        tup=(LN,FN,UN,Em,Add,Phone,Pwd,Act,rol)
        mycursor.execute(sql_insert_query,tup)
        mydb.commit()
        print('Account Created')
        mycursor.execute("select Id from users where Active=1")
        d=mycursor.fetchall()
        for i in d:
            for j in i:
                Id=j
        LoginId=Id
        print("Your UserId is :",LoginId)
        main()
    elif ch=='2':#for an existing user to shop
        try:
            userid=int(input("Enter your userid :"))
        except ValueError:
            print('Enter the correct value')
            login()
        pwd=stdiomask.getpass("Enter your password :")#to hide the password
        mycursor.execute("select password from users where Id="+str(userid))
        d=mycursor.fetchall()
        for i in d:
            for j in i:
                if j== pwd:
                    mycursor.execute("select role from users where Id="+str(userid))#to check if the user is admin or customer
                    b=mycursor.fetchall()
        for i in b:
            for j in i:
                if j== 'Admin':
                    LoginId=userid
                    admin()
                else:
                    mycursor.execute("Update users set Active=1 where id="+str(userid))
                    mydb.commit()
                    LoginId=userid
                    main()
        else:
            print('Password Incorrect')
            login()
    elif ch=='3':
        print("Thank you !")
    else:
        print("Invalid Choice")
        login()
def main():
    print('****************************')
    print('******** WELCOME TO F2F SUPERMARKET ************')
    print()
    x=int(input('''
    * Enter 1 to go to shop *
    * Enter 2 to go to cart *
    * Enter 3 to see order history *
    * Enter 4 to log out *
    Please enter:'''))
    if x==1:
        category()
    elif x==2:
        cart()
    elif x==3:
        history()
        main()
    elif x==4:
        q="Update users set active=0 where Id="+str(LoginId)
        mycursor.execute(q)
        mydb.commit()
        mydb.close()
        print('Thank you for shopping with us ')
    else :
        print('* Invalid choice * ')
        print()
        main()
login()
