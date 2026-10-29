#Student Record Management with List,Tuple,Dictionary and csv
import csv
Students=[
      {"Roll No":"101","Name":"praveena","Department":"CSE","Mark":86},
      {"Roll No":"102","Name":"Anitha","Department":"CSE","Mark":91},
      {"Roll No":"103","Name":"Chitra","Department":"ECE","Mark":78}
]  
#Tuple example:fixed course details
course = ("python",4)
print("course Tuple:",course)
#write text file
with open("Student.txt","w")as file:
  for Student in Students:
    file.write(str(Student)+"\n")
#write csv file
with open("Students.csv","w",newline="") as file:
    fields = ["Roll No","Name","Department","Mark"] 
    write = csv.DictWriter(file,fieldnames=fields)
    write.writeheader()
    write.writerows(Students)
#Read csv file
# print("\n---Records from csv---")
with open("Students.csv","r")as file:
    reader = csv.DictReader(file)
    for rows in reader:
        print(rows["Roll No"],rows["Name"],rows["Department"],rows["Mark"])