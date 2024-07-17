#!pip install mysql-connector-python


import mysql.connector
connection = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'Dinosaurs@91',
database = 'mydb'
)

cursor = connection.cursor()
    
def menu():
    
    print("Welcome to the employee database")
    print("Select an option to work upon")
    print(" ")
    
    print("0    Exit")
    print("1    Add an employe")
    print("2    Modify/Update an employee")
    print("3    Exit/Delete an employee")
    print("4    Specify employee by employee ID")
    print("5    Department wise list of employees")
    print("6    All the employees")
    
    option = int(input("Enter your input: "))
    return option


#main program

while True:
    
    choice = menu()

    
#1    
    if choice == 0:
        print(" ")
        print("Thanks!")
        print(" ")
        
        break
        

#2
    elif choice == 1:
        sql = "INSERT INTO emps(id, name, age, salary, department_id) VALUES (%s, %s, %s, %s, %s)"

        while True:
            a_id = int(input("Enter ID: "))
            a_name = input("Enter Name: ")

            success = 0
            while success == 0:
                try:
                    a_age = int(input("Enter Age: "))
                    if 18 <= a_age <= 60:
                        success = 1
                    else:
                        print("Age should be between 18 to 60")
                except ValueError:
                    print("Invalid input. Please enter a valid age.")


            a_salary = float(input("Enter Salary: "))
            a_dept_id = input("Enter Department ID: ")

            data_ins = (a_id, a_name, a_age, a_salary, a_dept_id)
            cursor.execute(sql, data_ins)
            connection.commit()  

            print("Employee added successfully!")
            print(" ")


            add_another = input("Press ENTER to add another Employee")
            if add_another != '':
                print(" ")
                print("Thanks!")
                print(" ")
                break

                                
#3
    elif choice == 2:
        sql = ("UPDATE emps SET name = %s, age = %s, salary = %s, department_id = %s WHERE id = %s")
        
        print(" ")
        print("Enter the details for the employee record you want to update")

        data1 = int(input("Enter employee ID: "))
        data2 = None
        data3 = None
        data4 = None
        data5 = None

        update_name = input("Do you want to update the Name? (Y/N): ")
        if update_name == 'Y':
            data2 = input("Enter Name: ")
        else:
            data2 = None

        update_age = input("Do you want to update the Age? (Y/N): ")
        if update_age == 'Y':
            data3 = int(input("Enter Age: "))
        else:
            data3 = None

        update_salary = input("Do you want to update the Salary? (Y/N): ")
        if update_salary == 'Y':
            data4 = float(input("Enter Salary: "))
        else:
            data4 = None

        update_department_id = input("Do you want to update the Department ID? (Y/N): ")
        if update_department_id == 'Y':
            data5 = input("Enter Department ID: ")
        else:
            data5 = None

        data_mod = (data2,data3,data4,data5,data1)
        cursor.execute(sql,data_mod)
        connection.commit()

        print(" ")
        print("Employee Details Updated Successfully!")
        print(" ")

        
#4
    elif choice == 3:

        sql = ("DELETE FROM emps WHERE id = %s")
        emp_id = int(input("Enter the employee ID: "))
        data_del = (emp_id,)
        cursor.execute(sql,data_del)
        connection.commit()

        print(" ")
        print("Employee Deleted Successfully!")
        print(" ")


#5
    elif choice == 4:
        
        sql = "SELECT * FROM emps WHERE id = %s"
        emp_id = int(input("Enter employee ID: "))
        data = (emp_id,)
        cursor.execute(sql, data)
        records = cursor.fetchall()
        if records:
            print("Employee details:")
            for row in records:
                print(row)
        else:
            print("Employee not found.")

            
#6
    elif choice == 5: 
        
        sql = "SELECT * FROM emps WHERE department_id = %s"
        dept_id = input("Enter Department ID: ")
        cursor.execute(sql, (dept_id,))
        records = cursor.fetchall()
        if records:
            print("Employees in department:")
            for row in records:
                print(row)
        else:
            print("No employees found in the specified department!")
            print(" ")
            
            
#7
    elif choice == 6:
        
        sql = "SELECT * FROM emps"
        cursor.execute(sql)
        records = cursor.fetchall()
        if records:
            print("All employees:")
            for row in records:
                print(row)
        else:
            print("No employees found.")
            print(" ")

            
  #Commit and close

    connection.commit()
    cursor.close()
    connection.close()