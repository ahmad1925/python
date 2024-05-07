# light = input("color is: ")

# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# else:
#     print("light is broken")        


# food = input("food: ")

# eat= "yes" if food=="cake" else "no"
# print(eat)

# print("sweet") if food=="cake" or food=="jelabi" else print("no sweet")

# age = int(input("age: "))

# vote=("no","yes") [age>=18]

# print(vote)

# str = input("enter your string: ")
# print(str)
# print(len(str))

# str1 = input("enter: ")

# print(str1.count("$"))
# print(str1.find("o"))
# print(str1.capitalize())

# str2="hello world"
# print(str2.replace("lo","aa"))
# print(str2.count("l"))
# print(str2.endswith("ld"))
# print(str2.find("o"))
# print(str2[0:4])
# #negitive index
# print(str2[-3:-1])


# number = int(input("enter the number to check it odd and even: "))

# if(number%2==0):
#     print("number is even")
# elif(number%2>=1):
#     print("number is odd")    
# else:
#     print("this is not a number")    

# a= int(input("enter the value a: "))
# b= int(input("enter the value b: "))
# c= int(input("enter the value c: "))

# if(a>b and a>c):
#     print("greatest no is ",a)
# elif(b>a and b>c):
#     print("greatest no is ",b)
# elif(c>a and c>b):
#     print("greatest no is ",c)
# else:
#     print("more than one number is same value")        

# n=int(input("enter the number and check it is multiple of 7 or not: "))
# check = n % 7

# if(check ==0):
#     print("number is multiple of 7")
# else:
#     print("number is not multiple of 7")

# mov1=input("enter your first faviort movie: ")
# mov2=input("enter your 2nd faviort movie: ")
# mov3=input("enter your 3rd faviort movie: ")

# movies=[]
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# list = ["m",1,2,1,"m"]
# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == list):
#     print("pelidrome")
# else:
#     print("not pelidrome")

# list1 = ["B","A","A","B","A","C","B"]
# print(list1.count("A"))
# list1.sort()
# print(list1)

# students={
#     "name":"ahmad",
#     "graduation":"BS SE",
#     "subject":{
#         "c++":80,
#         "python":90,
#         "javascript":"95"
#     }
# }
# students["subject"]["python"] =95
# print(students["subject"]["python"])

# marks={}

# x=int(input("enter the marks of physics: "))
# marks.update({"phy":x})

# y=int(input("enter the marks of chemistry: "))
# marks.update({"chem":y})

# marks.update({"math":int(input("enter the marks of math: "))})

# print(marks)

# d=int(input("enter the first number"))
# e=float(input("enter the 2nd number"))

# myset=set()

# myset.add(d)
# myset.add(e)
# print(myset)

# values={
#     ("float",9.0),
#     ("int",9)
# }

# print(values)

# t=(1,"3","kdk")
# print(type(t))
# print(t.index(1))
# print(t.count(1))

# i=1
# while i<=100:
#     print(i)
#     i+=1


# i=100
# while i>=1:
#     print(i)
#     i-=1

# n =int(input("enter the number: "))

# i=1

# while i<=10:
#     print(n*i)
#     i+=1

# listt = [1,4,45,33,54,65,76]

# i=0
# while i<len(listt):
#     print(listt[i])
#     i+=1

# list2 = [1,2,3,4,5,6,7,8]

# for n in list2:
#     print(n)
# else:
#     print("end")    

# t =(1,5,20,30,40)

# x=30

# for s in t:
#     if(x==s):
#         print("found ",s)
#         break
    
# for ss in t:
#     if(x==ss):
#         print("found",ss)
#         continue
#     print(ss)

# for i in range(100,0,-1):
#     print(i)



# nm = int(input("enter the number : "))

# for n in range(1,11):
#     print( nm * n )

