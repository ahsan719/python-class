name=input("Enter your name")
department=input("Enter depart")
age=int(input("Enter age"))

programming= int(input("Enter Programming Makrs"))
Math= int(input("Enter math Makrs"))
English= int(input("Enter English Makrs"))

total_Marks= programming+Math+English
average_marks=total_Marks/3

print(f"Total Marks: {total_Marks}") 
print("Average Marks:", average_marks)
