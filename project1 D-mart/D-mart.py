import mysql.connector
import numpy as np

# ============ CONNECTION ============
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="d-mart"
)
cursor = conn.cursor()

conn.autocommit = True

class Admin_login():
    def admin_login(self):
        print("\nAdmin Login")
        username = input("Enter Username: ").title()
        password = input("Enter Password: ")
        cursor.execute("""SELECT * FROM admin_login WHERE username = %s AND password = %s """, (username,password))
        exist = cursor.fetchone()
        if exist:
            if username == exist[0] and password == exist[1]:
                print(f"\n {username} Login Successful")
                return exist[0]
            else:
                print(f"\n {username} Login Failed")
                return None
        else:
            print(f"\n {username} Login Failed")
            return None

    def admin_signup(self):
        print("\nAdmin Signup")
        username = input("Enter Username: ").title()
        password = input("Enter Password: ")
        cursor.execute("""INSERT INTO admin_login (username, password) VALUES (%s, %s)""", (username,password))
        conn.commit()
        print(f"\n {username} Signup Successful")

class Customer_login():
    def customer_login(self):
        print("\nCustomer Login")
        username = input("Enter Username: ").title()
        password = input("Enter Password: ")
        cursor.execute("""SELECT * FROM customer_login WHERE username = %s AND password = %s """, (username,password))
        exist = cursor.fetchone()
        if exist:
            if username == exist[0] and password == exist[1]:
                print(f"\n {username} Login Successful")
                return exist[0]
            else:
                print(f"\n {username} Login Failed")
                return None
        else:
            print(f"\n {username} Login Failed")
            return None

    def customer_signup(self):
        print("\nCustomer Signup")
        username = input("Enter Username: ").title()
        password = input("Enter Password: ")
        gender = input("Enter Gender: ")
        contact = int(input("Enter Contact Number: "))
        address = input("Enter Address: ")
        cursor.execute("""INSERT INTO customer_login (username,password,gender,contact,address) VALUES (%s, %s,%s,%s,%s)""",(username,password,gender,contact,address))
        conn.commit()
        print(f"\n {username} Signup Successful")


class Admin_work():
    def add_product_admin(self):
        print("\n=============Add Product ==============")

        name = input("Enter Product Name: ").title()
        quantity = int(input("Enter Product Quantity: "))
        price = float(input("Enter Product Price: "))
        id = np.random.randint(100,1000,size = 1)
        line_total = quantity * price

        cursor.execute("""INSERT INTO product_store (id,name,quantity,price,line_total) VALUES (%s, %s, %s, %s, %s)""",(int(id[0]),name,quantity,price,line_total))
        conn.commit()
        print(f" product {name} quantity of {quantity} added Successful at {price}")

    def delete_product_admin(self):
        print("============= Delete Product===========")
        name = input("Enter Product Name : ").title()
        cursor.execute("""SELECT * FROM product_store WHERE name = %s """,(name,))
        exist = cursor.fetchone()
        if exist:
            if name == exist[1] :
                cursor.execute("""DELETE FROM product_store WHERE name = %s """,(name,))
                conn.commit()
                print(f"{name} has deleted...")
                return exist[1]

            else:
                print(f"{name} not found in product store")
                return None
        else:
            print(f"{name} product not found")
            return None

    def update_product_admin(self):
        print("=========Update Product ==========")
        name = input("Enter Product name :").title()
        cursor.execute("""SELECT * FROM product_store WHERE name = %s """,(name,))
        exist = cursor.fetchone()
        if exist:
            if name == exist[1] :

                quantity = int(input("Enter Product quantity : "))
                price = float(input("Enter Product price : "))
                line_total = quantity * price

                cursor.execute("""UPDATE product_store SET quantity = quantity + %s, price = %s ,line_total= %s WHERE name = %s""",(quantity,price,line_total,name ))
                conn.commit()
                print(f"product {name} has been updated Successful.....")
                return exist[1]
            else:
                print(f"{name} product not found...")
                return None
        else:
            print(f"{name} product not found...")
            return None

    def view_all_product_admin(self):
        cursor.execute("""SELECT * FROM product_store """)
        exist = cursor.fetchall()
        ground_total = 0

        if exist:
            for item in exist:
                print(f"{item[0]}: name - {item[1]} | quantity - {item[2]} | price - {item[3]} | line_total - {item[4]}")
                ground_total += item[4]
            print(f"Total = {ground_total} ")
        else:
            print("No product added..")

    def search_product_admin(self):

        self.view_all_product_admin()

        name = input("Enter Product name for search : ").title()
        print(" ")
        cursor.execute("""SELECT * FROM product_store WHERE name = %s """,(name,))
        exist = cursor.fetchone()
        if exist:
            if name == exist[1]:

                print(f"{exist[0]}: name - {exist[1]} | quantity - {exist[2]} | price - {exist[3]} | line_total - {exist[4]}")
                return exist[1]
            else:
                print(f"{name}product not found")
                return None
        else:
            print(f"{name} product not found..")
            return None

class Customer_work():

    def add_product_kart(self):
        self.view_all_product_store()
        name = input("Enter product name : ").title()
        quantity = int(input("Enter quantity : "))

        cursor.execute("""SELECT * FROM product_store WHERE name = %s """,(name,))
        exist = cursor.fetchone()
        if exist:
            price = exist[3]
            line_total = price * quantity

            cursor.execute("INSERT INTO kart_store (name,quantity,price,line_total)VALUES (%s,%s,%s,%s)",(name,quantity,price,line_total))
            conn.commit()
            print(f"{name} : quantity = {quantity} | price = {price} | line_total = {line_total}")

            print("Product Added Successfully")


        cursor.execute(
            """UPDATE product_store SET quantity = quantity - %s WHERE name = %s""",
            (quantity,name))
        conn.commit()

        print(f"{name}product Updated from product_store to kart ")

    def view_all_product_store(self):
        cursor.execute("""SELECT * FROM product_store """)
        exist = cursor.fetchall()
        if exist:
            for item in exist:
                print(f"{item[0]}: name - {item[1]} | quantity - {item[2]} | price - {item[4]} | line_total - {item[4]}")
                print("========================================================")
        else:
            print("No products in Store..... ")

    def delete_product_kart(self):
        cursor.execute("""SELECT * FROM kart_store """)
        exist = cursor.fetchall()
        if exist:
            for item in exist:
                print(f"{item[0]}: name - {item[1]} | quantity - {item[2]} | price - {item[3]} | line_total - {item[4]}")
                print("========================================================")
        else:
            print("No products in Store..... ")

        name = input(f"Enter name of product : ").title()
        cursor.execute("""SELECT * FROM kart_store WHERE name = %s """,(name,))
        exist = cursor.fetchone()
        if exist:
            cursor.execute("""DELETE FROM kart_store WHERE name = %s """,(name,))
            conn.commit()
            print(f"{name} is deleted from kart_store... ")
            cursor.execute("""UPDATE product_store SET quantity = quantity + %s  WHERE name = %s """,(item[2],name))
            conn.commit()

        else:
            print(f"{name} is not found in kart...")
            return

    def bill_product_kart(self):
        cursor.execute("""SELECT * FROM kart_store """)
        exist = cursor.fetchall()
        ground_total = 0

        if exist:
            for item in exist:
                print(f"{item[0]}: name - {item[1]} | quantity - {item[2]} | price - {item[3]} | line_total - {item[4]}")
                ground_total += item[4]
            tax = ground_total * 0.10
            ground_total_tax = ground_total + tax
            print(f"Total : {ground_total} + 10% : {tax} = {ground_total_tax} ")
            print(" ")
            print("==============Payment Mode =====================")

            print("1.UPI ")
            print("2.Cash")
            print("3.Cancle Order")
            choice = int(input("which mode you want to choose for payment :"))
            if choice == 1 :
                print(f"your bill {ground_total_tax} has payed through UPI mode has Successful....")
            elif choice == 2:
                print(f"your bill {ground_total_tax} has been payed through Cash mode has Successful...")
            elif choice == 3:
                print(f"Your bill {ground_total_tax} has been Cancled ")


while True:
    admin = Admin_login()
    customer = Customer_login()
    admin_work = Admin_work()
    customer_work = Customer_work()

    while True:
        print("\n========== Welcome to D-Mart ============")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        choice = int(input("Who are you (1/2/3): "))

        if choice == 1:
            while True:
                print("\n========= Admin ===========")
                print("1. Login")
                print("2. SignUp")
                print("3. Exit to Main Menu")
                admin_choice = int(input("Login / SignUp / Exit: "))

                if admin_choice == 1:
                    user = admin.admin_login()
                    if user:
                        while True:
                            print("\n==== Admin Menu ====")
                            print("1. Add Product")
                            print("2. Delete Product")
                            print("3. Update Product")
                            print("4. View All Products")
                            print("5. Search Product")
                            print("6. Logout")
                            work_choice = int(input("Choose option: "))
                            if work_choice == 1:
                                admin_work.add_product_admin()
                            elif work_choice == 2:
                                admin_work.delete_product_admin()
                            elif work_choice == 3:
                                admin_work.update_product_admin()
                            elif work_choice == 4:
                                admin_work.view_all_product_admin()
                            elif work_choice == 5:
                                admin_work.search_product_admin()
                            elif work_choice == 6:
                                print("Logged out from Admin.")
                                break
                            else:
                                print("Invalid choice.")
                    else:
                        print("Invalid credentials.")
                elif admin_choice == 2:
                    admin.admin_signup()
                elif admin_choice == 3:
                    break
                else:
                    print("Invalid choice.")

        elif choice == 2:
            while True:
                print("\n=========== Customer ===========")
                print("1. Login")
                print("2. SignUp")
                print("3. Exit to Main Menu")
                customer_choice = int(input("Login / SignUp / Exit: "))

                if customer_choice == 1:
                    user = customer.customer_login()
                    if user:
                        while True:
                            print("\n==== Customer Menu ====")
                            print("1. View Products")
                            print("2. Add Product to Cart")
                            print("3. Delete Product from Cart")
                            print("4. Checkout & Bill")
                            print("5. Logout")
                            cust_choice = int(input("Choose option: "))
                            if cust_choice == 1:
                                customer_work.view_all_product_store()
                            elif cust_choice == 2:
                                customer_work.add_product_kart()
                            elif cust_choice == 3:
                                customer_work.delete_product_kart()
                            elif cust_choice == 4:
                                customer_work.bill_product_kart()
                            elif cust_choice == 5:
                                print("Logged out from Customer.")
                                break
                            else:
                                print("Invalid choice.")
                    else:
                        print("Invalid credentials.")
                elif customer_choice == 2:
                    customer.customer_signup()
                elif customer_choice == 3:
                    break
                else:
                    print("Invalid choice.")

        elif choice == 3:
            print("Thank you for visiting D-Mart. Goodbye!")
            break
        else:
            print("Invalid choice.")



