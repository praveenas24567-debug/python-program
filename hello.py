#student Marks,percentage and Grade
name = input("Enter student name:")
n = int(input("Enter number of subjects:"))
total = 0
for i in range(1 , n + 1):
    mark = float(input(f"Enter mark for subjects{i}:"))
    total += mark 
percentage = total / n
if percentage >= 90:
     Grade = "A+"
     performance = "Outstanding"
elif percentage >= 80:
     Grade = "A"
     performance = "Excellent"
elif percentage >= 70:
     Grade = "B"
     performance = "Very good"
elif percentage >= 60:
     Grade = "C"
     performance = "good"
elif percentage >= 50:
    Grade = "D"
    performance = "D"
else:
   Grade = "F"
   performance = "Needs improvement"
   print("\n---Academic performance---")
   print("student name:", name)
   print("percentage : ", round(percentage , 2) , "%")
   print("total marks:",total)
   print("grade :", Grade)
   print("performance:", performance)    

