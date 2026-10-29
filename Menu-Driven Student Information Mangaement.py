#Menu-Driven Student Information System
Students={}
def add_Students():
    roll=input("Enter Roll No:")
    name=input("Enter Name:")
    dept=input("Enter Department:")
    Students[roll]={"Name":name,"Department":dept}
    print("Students added successfully:")
def view_Students():
    if not Students:
        print("No Students records found")
        return
    print("\n---Students Records---")
    for roll, data in Students.items(): 
        print("Roll No:",roll,"|Name:",data["Name"],"|Department:",data["Department"]) 
def search_Students():
    roll = input("Enter Roll No to search:")
    if roll in Students:
        print(Students[roll])
    else:
        print("Students not found")
def delete_Students():
    roll = input("Enter Roll No to delete")
    if roll in students:
        del Students[roll]
        print("Students deleted successfully:")
    else:
        print("Students not found:")
while True:
    print("\n1.add Students")
    print("2.view Students")
    print("3.search Students")
    print("4.delete Students")
    print("5.Exit")
    choice = input("Enter your choice")
    if choice == "1":
        add_Students()
    elif choice =="2":
        view_Students()
    elif choice=="3":
        search_Students()
    elif choice=="4":
        delete_Students()
    elif choice=="5":
        print("Existing...")
        break
    else:
        print("Invalid choice:")
                      