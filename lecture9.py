# print("write two numbers and get thier sum")
# a = int(input("write first no. :"))
# b = int(input("write second no. :"))
# sum = a+b
# print(sum)
# wap to input side of a square and give its area
# print("WRITE THE SIDE OF THE SQUARE TO KNOW ITS AREA")
# side = int(input("write the side here >>> "))
# print(side*side)
# program for two flating point numbers to get thier average
# a = int(input("write first no here >> "))
# b = int(input("write second no here >> "))
# if(a>=b):
#     print("True")
# else:
#     print("False")
# str = "Apple"
# print(str[-5:-1])
# print(str[:len(str):-1])
# print(len(str))







# user_name = input("know occurances of anything just type it here >>")
# print(user_name.count(input("what you want to know occurances of :")))
# age = int(input("Age >>>"))
# if age>= 18 :
#     print("you are eligible to mostly every document in india")
# else:
#     print("you are under 18 so you are not eligible to most of the documents in india")



# student_grade = int(input("what is your marks :"))
# if student_grade>= 90:
#     print("Your grade is A")
# elif student_grade < 90 and student_grade >= 80:
#     print("Your grade is B")
# elif student_grade< 80 and student_grade >= 70:
#     print("Your grade is C")
# elif student_grade< 70:
#     print("Your grade is D")
# number = 0
# if number/2 == 0 or number%2 == 0 :
#     print("even")
# else:
#     print("odd")
# a = 5
# b = 9
# c = 6
# if a > b and a > c:
#     print(a)
#     if b > a and b > c:
#         print(b)
#         if c > a and c > b:
#             print(c)
# else:
#     print("all are same")
# movies = []
# mov1 = input("write your first movie :")
# movies.append(mov1)
# mov2 = input("write your second movie :")
# movies.append(mov2)
# mov3 = input("write your third movie :")
# movies.append(mov3)
# print(movies)
# list = [1,2,3,2,1]
# pal = list.copy()
# pal.reverse()
# if pal == list:
#     print("yes it is palindrom")
# else:
#     print("no its not palindrom")
# list = ["A","D","C","A","B"]
# list.sort()
# print(list)
# my_dict = {
#             "table" : ["a peice of furniture","list of facts and figures"],
#             "cat" : "a small animal"
#             }
# print(my_dict)
# set1 = {"python","java","c++","python","javascript","java","python","c++","c"}
# print("classrooms needed for the students are :",len(set1))


# for i in range(1,6):
#     print(i)
# i = 100
# while i >= 1: #should work properly.
#     print(i)
#     i -= 1

# list1 = ("aadil","aakil","bilal")
# print(type(list1))
# numbers = [3, 8, 15, 22, 7]
# for i in numbers[4::-1]:
#     print(i)
# dict1 = {
#     "Name" : input("your name : "),
#     "age" : int(input("age : ")),
#     "city" : input("city : ")
# }
# for key,value in dict1.items():
#     print(key,":",value)
# countries = {
#     "India" : "New delhi",
#     "Japan" : "Tokyo",
#     "France" : "Paris"
# }
# for value in countries.values():
#     print(value)
# def ferenhight_to_celsius(ferenhight):
#     return (ferenhight - 32) * 5 / 9

# # calculate sum of 2 numbers.
# def calculate_sum (a,b):
#     print(a+b)
# calculate_sum(4,5)

# #check if a number is even/odd
# def even_odd_check (a):
#     if a%2 == 0:
#         print("even")
#     else:
#         print("odd")

# even_odd_check(5)

# #prints your name 5 times
# x = input("name : ")
# def name_5_times ():
#    print(x)
#    print(x)
#    print(x)
#    print(x)
#    print(x)
# name_5_times()

# def hello_name (x):
#     return "Hello " +x+ " welcome to coding."  
# print(hello_name("Aadil"))
# def bigger_one (a,b):
#     if a>b :
#         return a
#     elif b>a :
#         return b
#     else:
#         return "Both are same"
# a = int(input("first no. : "))
# b = int(input("second no. : "))
# print(bigger_one(a,b))
# def above_50 (a,b,c):
#     if a >= 50:
#         return a
#     if b >= 50:
#         return b
#     if c >= 50:
#         return c
    
# students = {
#     "Rahul": 72,
#     "Amit": 35,
#     "Priya": 88
# }
# a = students["Rahul"]
# b = students["Amit"]
# c = students["Priya"]
# print(above_50(a,b,c))


# def above_50 (students):
#     passed = []
#     for name,marks in students.items():
#         if marks >= 50:
#             passed.append(name)
#     return passed


# students = {
#     "Rahul": 72,
#     "Amit": 35,
#     "Priya": 88
# }

# print(above_50(students))




# def above_10 (numbers):
#     result = []
#     for x in numbers:
#         if x > 10:
#             result.append(x)
#     return result
        

# numbers = [5, 15, 3, 22, 8, 17]
# print(above_10(numbers))

# def above_18 (people):
#     adult = []
#     for name,age in people.items():
#         if age >= 18:
#             adult.append(name)
#     return adult
        
# # people = {"Aadil":17, "Rahul":21, "Priya":16, "Amit":19}
# # print(above_18(people))
# def get_age(ditc):
#     for key,value in ditc.items():
#         age = []
#         if value == 20:
#             age.append(key)
#             print(age)
#             return age

# ditc = {
#     "name" : "aadil",
#     "age" : 20,
#     "habit" : "running"
# }

# get_age(ditc)
    


# number guessing game first project.
# numbers  = [1,2,3,4,5,6,7,8,9,10]
# print(numbers)

from random import randint
# computer picks a random number and you pick and the program will tell whether its high or low.
comp_pick = randint(1,100)
guess = int(input("guess a number between 1 to 100 : "))
attempts = 1
while comp_pick != guess:
    Difference = abs(comp_pick - guess)
    print("Wrong")
    print(comp_pick)
    if Difference <= 3:
        print("Extremely close🔥")
    elif Difference <= 9:
        print("close")
    elif Difference <= 20:
        print("High")
    elif guess > comp_pick:
        print("Very high")
    else:
        print("Very Low")
    attempts += 1
    guess = int(input("Try again :"))
print("You got it in",attempts,"attempts🔥")