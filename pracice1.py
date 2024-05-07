
# s = int(input("enter the number n to sum the values: "))

# sum = 0

# for i in range(1,s+1):
#     sum += i


# print(sum)

# ss = int(input("enter the number n to sum the value: "))

# sum = 0

# i = 1
# while i<=ss:
#     sum +=i
#     i += 1

# print("the sum is ", sum)


# fac = int(input("enter the no to get factorial: "))

# f  = 1

# if fac == 0 and fac == 1:
#     print("the fac is ", f)
    
# else:
#     for i in range(1,fac+1):
#         f *= i
        
    
# print("the fac is  ",f)

# facc = int(input("enter the no to get facctorial: "))

# f  = 1
# i = 1

# if facc == 0 and facc == 1:
#     print("the facc is ", f)
    
# else:
#     while i<=facc:
#         f *= i
#         i += 1
# print(f)

# def check_number(n):
#     if n % 2== 0:
#         print("this no is even")
#     elif n % 2== 1:
#         print("this no is odd")
#     else:
#         print("it is not a no")    


# inp = int(input("enter the no. to check even and odd: "))
# check_number(inp)

# def recur_sum(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     return recur_sum(n - 1) + n


# print(recur_sum(1))

# def recur_list(list,index):
#     if index == len(list):
#         return
    
#     print(list[index])
#     recur_list(list,index+1)


# list = ["mango","apple","banana","lichii"]

# recur_list(list,0)