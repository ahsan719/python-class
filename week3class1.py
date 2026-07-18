
# marks=[10,20,30,40,50]
# names=["Ahsan", "Ali","Hassan"]
# mixed=[1,"Ahsan",True]


# #append
# # marks.append(60)

# #insert
# # marks.insert(4,70)

# #remove
# # marks.remove(30)
# # marks.pop()

# #functions

# # print(len(marks))
# # print(sum(marks))

# # for mark in marks:
# #     print(mark)

# # for i in names:
# #     print(i)  


# # if 100 in marks:
# #     print("Found")

# # else:
# #     print("Not found")   

# students=[

#     ["Ahsan",80,30,50],
#     ["Ali", 90,40,40],
#     ["Hassan",50,30,50]
    
#     ]

# for  student in students:
#     print(student[0],student[1],student[2], student[3])    


#movielist

movies= []


total=int(input("How many movies do you want to add?"))

for i in range(total):
    movie=input(f"Enter movie {i+1}")
    movies.append(movie)


print("\n ----- Your watch list------")
for movie in movies:
    print(movie)

movies.sort()
print("\n -----SOrted list----")
for movie in movies:
    print(movie)







