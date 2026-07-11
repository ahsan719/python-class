students=int(input("Enter no of students"))

total=0
highest=0
passed=0
count=0

for i in range(1,students+1):
    marks=int(input(f"Enter marks of student {i}"))

    if marks<0:
        print("program stopped")
        break

    if marks>100:
        print("Invalid, ignored") 
        continue

    total=total+marks
    count+=1


    if marks>highest:
        highest=marks

    if marks>50:
        passed=passed+1   

    if count>0:
        average=total/count       


print("Total marks", total)
print("Average Marks", average)
print("Highest Marks", highest)
print("passed Students", passed)     