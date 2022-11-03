import mysql.connector


connection=mysql.connector.connect(host="your host name",user="your user name",password="your password",database="database name")
cursor=connection.cursor()

def insertProduct(self):

        sql="INSERT INTO Products (name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
        values=(self.name,self.price,self.imageUrl,self.description)

        cursor.execute(sql,values)

        

        try:
            connection.commit()
            print(f'{cursor.rowcount} records added.')
            print(f'The id number of the last added record is: {cursor.lastrowid}')
        except  mysql.connector.Error as err:
            print("Error: ",err)
        finally:
            connection.close()
            print("Database connection closed.")

def insertProducts(liste):
        

        sql="INSERT INTO Products (name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
        values=liste

        cursor.executemany(sql,values)

        

        try:
            connection.commit()
            print(f'{cursor.rowcount} records added.')
            print(f'The id number of the last added record is: {cursor.lastrowid}')
        except  mysql.connector.Error as err:
            print("Error: ",err)
        finally:
            connection.close()
            print("Database connection closed.")

def getProducts():
        

        cursor.execute("Select * From Products Where name='Input a name'")
        
        result=cursor.fetchall()
        print(result)

liste=[]
while True:
            name=input("Input product name: ")
            price=int(input("Input product price: "))
            imageUrl=input("Input image url: ")
            description=input("Input description: ")

            liste.append((name,price,imageUrl,description))

            result=input("Do you want to continue y/n ")
            if result=="n":
                print("Your records have been added to your database...")
                print(liste)
                insertProducts(liste)
                break
            

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),adress VARCHAR(255))")
