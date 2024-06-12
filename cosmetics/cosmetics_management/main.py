from database import get_connection
from utils import clear_screen

def cosmetics_insert(cursor, conn):
    l = []
    code = int(input("Enter the cosmetic ID number: "))
    l.append(code)
    name = input("Enter the Cosmetics Name: ")
    l.append(name)
    company = input("Enter company of Cosmetics: ")
    l.append(company)
    cost = float(input("Enter the Cost: "))
    l.append(cost)
    manudate = input("Enter the Date of Manufacture (YYYY-MM-DD): ")
    l.append(manudate)
    expdate = input("Enter the Date of Expiry (YYYY-MM-DD): ")
    l.append(expdate)
    sql = "INSERT INTO product (code, name, company, cost, manudate, expdate) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, l)
    conn.commit()

def customer_insert(cursor, conn):
    l = []
    cust_id = int(input("Enter the Customer number: "))
    l.append(cust_id)
    cname = input("Enter the Customer Name: ")
    l.append(cname)
    c_phoneno = input("Enter Phone no. of Customer: ")
    l.append(c_phoneno)
    c_address = input("Enter Address: ")
    l.append(c_address)
    gender = input("Enter gender of customer (M/F): ")
    l.append(gender)
    membership = input("Enter the membership: ")
    l.append(membership)
    sql = "INSERT INTO customer (cust_id, cname, c_phoneno, c_address, gender, membership) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, l)
    conn.commit()

def cosmetics_view(cursor):
    print("Select the search criteria: ")
    print("1. Product Id")
    print("2. Product Name")
    print("3. All")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        s = int(input("Enter Product ID: "))
        sql = "SELECT * FROM product WHERE code=%s"
        cursor.execute(sql, (s,))
    elif ch == 2:
        s = input("Enter Product Name: ")
        sql = "SELECT * FROM product WHERE name=%s"
        cursor.execute(sql, (s,))
    elif ch == 3:
        sql = "SELECT * FROM product"
        cursor.execute(sql)
    else:
        print("Invalid choice!")
        return
    
    res = cursor.fetchall()
    for x in res:
        print(x)

def view_customer(cursor):
    print("Select the search criteria: ")
    print("1. Customer ID")
    print("2. Customer Name")
    print("3. All")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        s = int(input("Enter Customer ID: "))
        sql = "SELECT * FROM customer WHERE cust_id=%s"
        cursor.execute(sql, (s,))
    elif ch == 2:
        s = input("Enter Customer Name: ")
        sql = "SELECT * FROM customer WHERE cname=%s"
        cursor.execute(sql, (s,))
    elif ch == 3:
        sql = "SELECT * FROM customer"
        cursor.execute(sql)
    else:
        print("Invalid choice!")
        return
    
    res = cursor.fetchall()
    for x in res:
        print(x)

def customer_purchase(cursor, conn):
    print("Please enter the details to purchase cosmetics product:")
    cursor.execute("SELECT * FROM product")
    res = cursor.fetchall()
    for x in res:
        print(x)
    
    total_cost = 0.0
    while True:
        c1 = input("Enter the product name to be purchased: ")
        sql = "SELECT cost FROM product WHERE name=%s"
        cursor.execute(sql, (c1,))
        res = cursor.fetchall()
        if not res:
            print("Product not found!")
            continue
        cost = res[0][0]
        print("Cost per item:", cost)
        q1 = int(input("Enter the item quantity: "))
        total_cost += q1 * cost
        ch = input("Want to purchase more items (y/n)? ")
        if ch.lower() != 'y':
            break
    
    print("Total cost of items purchased is Rs.", total_cost)

def remove_cosmetics(cursor, conn):
    name = input("Enter the cosmetics name to be deleted: ")
    sql = "DELETE FROM product WHERE name=%s"
    cursor.execute(sql, (name,))
    sql = "DELETE FROM customer WHERE cname=%s"
    cursor.execute(sql, (name,))
    conn.commit()

def menu_set():
    conn = get_connection()
    cursor = conn.cursor()
    ans='y'
    while ans =="Y" or ans=="y" :
        clear_screen()

        print("\nMain Menu:")
        print("1: Add Cosmetics Product")
        print("2: View Complete Cosmetics Stock")
        print("3: Purchase Cosmetics Product")
        print("4: Remove Cosmetics Product")
        print("5: Add Customer Details")
        print("6: View Customer Details")
        try:
            user_input = int(input("Please Select an Option: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if user_input == 1:
            cosmetics_insert(cursor, conn)
        elif user_input == 2:
            cosmetics_view(cursor)
        elif user_input == 3:
            customer_purchase(cursor, conn)
        elif user_input == 4:
            remove_cosmetics(cursor, conn)
        elif user_input == 5:
            customer_insert(cursor, conn)
        elif user_input == 6:
            view_customer(cursor)
        else:
            print("Invalid choice! Please select a valid option.")
        
        ans=input("Continue(Y/N) ?:")
        

    cursor.close()
    conn.close()

if __name__ == "__main__":
    menu_set()
