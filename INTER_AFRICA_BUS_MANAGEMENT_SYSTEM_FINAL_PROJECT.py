#AUTHENTICATON
#decleration of database
def createme():
    userInformation = open('userinfo.txt','r')
    d = []
    f = []
    for i in userInformation:
        a,b = i.split(", ")
        b = b.strip
        d.append(a)
        f.append(b)
        data = dict(zip(d,f))
        print(data)

    #decleration an input
    user = input("Create username: ")
    pword = input("Create password: ")
    pword2 = input("Confirm password: ")

    #process
    if pword != pword2:
        print("Different passwords, Restart")
        createme()
    elif pword == pword2:
        if len(pword)<=6:
            print("Password has to be more than seven characters \n", "Restart")
            createme()
        elif user in d:
            print("username exists")
            createme()
        else:
            #entering user into database
            userInformation = open('userinfo.txt','a')
            userInformation.write(user+', '+pword + '\n')
            print("Success in creating acccount")
            print("\n Login")
        userInformation.close()
        axcessme()
    
def axcessme():
    userInformation = open('userinfo.txt','r')
    user = input("Enter username: ")
    pword = input("Enter password: ")

    if not len(user or pword)<1:
        d = []
        f = []
        for i in userInformation:
            a,b = i.split(", ")
            c = a,b
            b = b.strip
            d.append(a)
            f.append(b)
            data = dict(zip(d,f))
        try:
            if data[user]:
                try:
                    if pword == data[user]:
                        print("Login succesfull")
                        print("Hello", user)
                        welcome_page()
                    else:
                        
                        print("Welcome",user)
                        #axcessme()
                        welcome_page()
                except:
                    print(">>>>>>>>>>>INCORRECT PASSWORD OR USERNAME<<<<<<<<<<<<<<")
                    print("======================================================")
                    axcessme()
            else:
                print(">>>>>>>>>>>USER DOES NOT EXIST<<<<<<<<<<<<<<")
                print("======================================================")
                axcessme()
        except:
            print(">>>>>>>>>>>USERNAME OR PASSWORD DOES NOT EXIST<<<<<<<<<<<<<<")
            print("======================================================")
            axcessme()
    else:
        print("Please enter a value")
        axcessme()

#INSYSTEM

bus_management=[]
route_lst=[]
employees_lst=[]
passangers_lst=[]

                  # BUS CLASS
class Bus():
    def __init__(self,Type,engine_number,seating_capacity,route,route_time):
        self.Type=type
        self.engine_number=engene_nomber
        self.seating_capacity=seating_capacity
        self.route=route
        self.route_time=route_time
        

    def register_bus():
        bus1={  
     }
        
        bus1["type"]=input("Enter bus type :")
        bus1["engine_number"]=input("Enter engine number :")
        bus1["seating_capacity"]=input("Enter bus capacity :")
        bus1["route"]=input("Enter bus route :")
        bus1["route_time"]=input("At what time is the departure : ")
        bus_management.append(bus1)
        print("-------------------------------------------------")
        print("SUCCESSFULY ADDED--")
        print("")
        print(bus1)
        print("")

        bus_file= open("busses1.txt", "w")
        for a in bus_management:
             bus_file.write(str(a)+"\n")
        bus_file.close()

                    #ROUTE CLASS

class Route():
    def __init__(self,name,time,bus_going,number_of_seats):
        self.name=route_name
        self.bus_going=bus_going
        self.number_of_seats=number_of_seats
        self.time=time
        
    def register_route():
        route={
            }
        route["name"]=input("Enter route name : ")
        route["time"]=input("What time is the departure :")
        route["bus_going"]=input("Which bus is going there :")
  #AUTOMATE NUMBER OF SEATS      
        route["number_of_seats"]=input("Enter number of seats :")
        route_lst.append(route)
        print("-------------------------------------------------")
        print("SUCCESSFULY ADDED--")
        print("")
        print(route)
        print("")
            
        route_file=open("routes.txt", "w")
        for a in route_lst:
            route_file.write(str(a)+"\n")
        route_file.close()

                         # EMPLOYEE CLASS

class Employee():
    def __init__(self,name,occupation,duty_time,salary):
        self.name=employee_name
        self.occupation=employee_occupation
        self.duty_time=duty_time
        self.salary=employee_salary

    def register_employee():
        employees={
            }
        employees["employee_name"]=input("Enter Employees name : ")
        employees["occupation"]=input("Enter Employees occupation : ")
        employees["duty_time"]=input("Enter employees duty time :  ")
        employees["employee_name"]=input("Enter Employees salary : ")

        employees_lst.append(employees)
        print("-------------------------------------------------")
        print("SUCCESSFULY ADDED--")
        print("")
        print(employees)
        print("")

        employees_file=open("employees.txt","w")
        for a in employees_lst:
             employees_file.write(str(a)+"\n")
             
        employees_file.close()

                            #PASSANGER CLASS

class Passanger():
    def __init__(self,name_of_passanger,age_of_passanger):
        self.name_of_passanger=name_of_passanger
        self.age_of_passanger=age_of_passanger

    def register_passanger():
        passanger={
               }
        passanger["name_of_passanger"]=input("Enter name of passanger : ")
        passanger["age_of_passanger"]=input("Enter age of passanger : ")
        passangers_lst.append(passanger)
        print("-------------------------------------------------")
        print("SUCCESSFULY ADDED--")
        print("")
        print(passanger)
        print("")

        passangers_file=open("passangers.txt","w")
        for a in passangers_lst:
            passangers_file.write(str(a)+"\n")
        passangers_file.close()

#         AM ON THE BUS MODULE
def bus_module():
        print(">>>>>>>>>>>YOU HAVE ENTERED THE BUS MODULE<<<<<<<<<<<<<<")
        print("======================================================")
        print("These are availabe buses :")
        print("-")
        for a in bus_management:
            print(a)
            print("")
        #     DO NOT FORGATE THE BUS UPDATE
        print("======================================================")
        print("")
        print("To add a bus press-A, to delete a bus press-D, to update a bus press-U, press * to go back")
        print("")
        print("------------------------------------------------------")

        choice = input("Enter your choice : ")
        print("")
        #  REMEMBER TO UPDATE THE UPDATE MODULES
        if choice=="A":
            Bus.register_bus()
            bus_module()
        elif choice=="*":
            welcome_page()
        elif choice=="D":
            delete_bus()
            print(bus_management)

            bus_file = open("busses1.txt", "w")
            for a in bus_management:
                bus_file.write(str(a) + "\n")
            bus_file.close()
            bus_module()

        #       TO BE ADDED
        elif choice=="U":
            update_bus()

def route_module():
        print(">>>>>>>>>>>YOU HAVE ENTERED THE ROUTE MODULE<<<<<<<<<<<<<<")
        print("======================================================")
        print("these are available routes : ")
        print("-")
        for a in route_lst:
            print(a)
            print("")
        print("======================================================")
        print("")
        print("To add a route press-A, to delete a route press-D, to update a route press-U, press * to go back")
        print("")
        print("------------------------------------------------------")

        choice = input("Enter your choice : ")
        print("")
        #  REMEMBER TO UPDATE THE UPDATE MODULES
        if choice == "A":
            Route.register_route()
            route_module()
        elif choice == "*":
            welcome_page()
        elif choice == "D":
            delete_route()

            route_file = open("routes.txt", "w")
            for a in route_lst:
                route_file.write(str(a) + "\n")
            route_file.close()
            route_module()

        elif choice == "U":
            update_route()
            route_module()

def employee_module():
    print(">>>>>>>>>>>YOU HAVE ENTERED THE EMPLOYEE MODULE<<<<<<<<<<<<<<")
    print("======================================================")
    print("These are available employees : ")
    for a in employees_lst:
        print(a)
        print("")
    print("======================================================")
    print("")
    print("To add an employee press-A, to delete an employee press-D, to update an employee press-U, press * to go back")
    print("")
    print("------------------------------------------------------")


    choice = input("Enter your choice : ")
    print("")
    #  REMEMBER TO UPDATE THE UPDATE MODULES
    if choice == "A":
        Employee.register_employee()
        employee_module()
    elif choice == "*":
        welcome_page()
    elif choice == "D":
        delete_employee()

        employees_file = open("employees.txt", "w")
        for a in employees_lst:
            employees_file.write(str(a) + "\n")

        employees_file.close()
        employee_module()

    elif choice == "U":
        update_employee()
        employee_module()

def passenger_module():
        print(">>>>>>>>>>>YOU HAVE ENTERED THE PASSANGER MODULE<<<<<<<<<<<<<<")
        print("======================================================")
        print("These are available passangers : ")
        for a in passangers_lst:
            print(a)
            print("")
        print("======================================================")
        print("")
        print("To add a passanger press-A, to delete a passanger press-D, to update a passanger press-U, press * to go back")
        print("")
        print("------------------------------------------------------")

        choice = input("Enter your choice : ")
        print("")
        #  REMEMBER TO UPDATE THE UPDATE MODULES
        if choice == "A":
            Passanger.register_passanger()
            passenger_module()
        elif choice == "*":
            welcome_page()
        elif choice == "D":
            delete_passanger()

            passangers_file = open("passangers.txt", "w")
            for a in passangers_lst:
                passangers_file.write(str(a) + "\n")
            passangers_file.close()
            passenger_module()

        elif choice == "U":
            update_passanger()
            passenger_module()


#                 DELETING MODULES
def delete_bus():
    print("To delete enter the index of the item")
    for a in bus_management:
        print(f"[{bus_management.index(a)}] {a}")

    index = int(input("Enter the index : "))
    print("----------------------------------------------------")
    print("Successfuly removed ", bus_management[index])
    print("----------------------------------------------------")
    bus_management.remove(bus_management[index])

def delete_route():
    print("To delete enter the index of the item")
    for a in route_lst:
        print(f"[{route_lst.index(a)}] {a}")

    index = int(input("Enter the index : "))
    print("----------------------------------------------------")
    print("Successfuly removed ", route_lst[index])
    print("----------------------------------------------------")
    route_lst.remove(route_lst[index])

def delete_employee():
    print("To delete enter the index of the item")
    for a in employees_lst:
        print(f"[{employees_lst.index(a)}] {a}")

    index = int(input("Enter the index : "))
    print("----------------------------------------------------")
    print("Successfuly removed ", employees_lst[index])
    print("----------------------------------------------------")
    employees_lst.remove(employees_lst[index])

def delete_passanger():
    print("To delete enter the index of the item")
    for a in passangers_lst:
        print(f"[{passangers_lst.index(a)}] {a}")

    index = int(input("Enter the index : "))
    print("----------------------------------------------------")
    print("Successfuly removed ", passangers_lst[index])
    print("----------------------------------------------------")
    passangers_lst.remove(passangers_lst[index])

#                                 UPDATING MODULES

def update_bus():
    print("To update enter the index of the item to be udpated")

    for a in bus_management:
        print(f"[{bus_management.index(a)}] {a}")

    index=int(input("Enter the index of the item to be updated : "))
    print("-----------------------------------------------------")
    print("You have selected ",bus_management[index])
    print("-----------------------------------------------------")
    key=input("What would you like to update? : ")
    bus_management[index][key]=input(f"Update {key} to : ")
    print("-----------------------------------------------------")
    print("Update Successful!!!!!")
    print(bus_management[index])
    print("-----------------------------------------------------")

    bus_file=open("busses1.txt","w")
    for a in bus_management:
        bus_file.write(str(a)+"\n")
    bus_file.close()
    bus_module()

def update_route():
    print("To update enter the index of the item to be udpated")

    for a in route_lst:
        print(f"[{route_lst.index(a)}] {a}")

    index=int(input("Enter the index of the item to be updated : "))
    print("-----------------------------------------------------")
    print("You have selected ",route_lst[index])
    print("-----------------------------------------------------")
    key=input("What would you like to update? : ")
    route_lst[index][key]=input(f"Update {key} to : ")
    print("-----------------------------------------------------")
    print("Update Successful!!!!!")
    print(route_lst[index])
    print("-----------------------------------------------------")

    route_file=open("routes.txt","w")
    for a in route_lst:
        route_file.write(str(a)+"\n")
    route_file.close()
    route_module()

def update_employee():
    print("To update enter the index of the item to be udpated")

    for a in employees_lst:
        print(f"[{employees_lst.index(a)}] {a}")

    index=int(input("Enter the index of the item to be updated : "))
    print("-----------------------------------------------------")
    print("You have selected ",employees_lst[index])
    print("-----------------------------------------------------")
    key=input("What would you like to update? : ")
    employees_lst[index][key]=input(f"Update {key} to : ")
    print("-----------------------------------------------------")
    print("Update Successful!!!!!")
    print(employees_lst[index])
    print("-----------------------------------------------------")

    employees_file=open("employees.txt","w")
    for a in employees_lst:
        employees_file.write(str(a)+"\n")
    employees_file.close()
    employee_module()

def update_passanger():
    print("To update enter the index of the item to be udpated")

    for a in passangers_lst:
        print(f"[{passangers_lst.index(a)}] {a}")

    index=int(input("Enter the index of the item to be updated : "))
    print("-----------------------------------------------------")
    print("You have selected ",passangers_lst[index])
    print("-----------------------------------------------------")
    key=input("What would you like to update? : ")
    passangers_lst[index][key]=input(f"Update {key} to : ")
    print("-----------------------------------------------------")
    print("Update Successful!!!!!")
    print(passangers_lst[index])
    print("-----------------------------------------------------")

    passangers_file=open("passangers.txt","w")
    for a in passangers_lst:
        passangers_file.write(str(a)+"\n")
    passangers_file.close()
    passenger_module()

#                       WELCOME PAGE
def welcome_page():
    print(">>>>>>>WELCOME TO THE INTER AFRICA BUS MANAGEMENT SYSTEM!!!!<<<<<<< ")
    print("To managage buses enter-1")
    print("To managage routes enter-2")
    print("To managage employees enter-3")
    print("To managage passangers enter-4")
    print("___________________________________________________")

    choice=input("Enter your choice : ")
    if choice=="1":
        bus_module()
    elif choice=="2":
        route_module()

    elif choice=="3":
        employee_module()
    elif choice=="4":
        passenger_module()


#welcome_page()
        
                            
        

#HOME FUNCTION

def home(option=None):
    print(">>>>>>>>>>>WELCOME USER<<<<<<<<<<<<<<")
    print("======================================================")
    option = input("Login or Signup: ")
    if option == "Login":
        print(">>>>>>>>>>>LOGIN<<<<<<<<<<<<<<")
        axcessme()
    elif option == "Signup":
        print(">>>>>>>>>>>CREATE USER<<<<<<<<<<<<<<")
        createme()
    else:
        print(">>>>>>>>>>>INVALID FORMAT<<<<<<<<<<<<<<")
        print("Please enter an option")
        home()
home()

