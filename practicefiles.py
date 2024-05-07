# #create and write a file
# with open("file2.txt","w") as f:
#     f.write("hello i am a software engineer")
#     f.write("\nhows about you")
#     f.write("\ni am a quick learner")

# #read the file
# with open("file2.txt","r") as f:
#     data=f.read()
#     print(data)

# replace the string by replace method
# new_data = data.replace("hello","hi")
# print(new_data)

#overwrite the file data by write
# with open("file2.txt","w") as f:
#     f.write(new_data)

#search the string that exist in txt file or not
# word = "hi"
# with open("file2.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

# find the line in which word is exist

# def check_line():
#     word = "learner"
#     line_no=1
#     data=True
#     with open("file2.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
    
#     return -1


# check_line()

#check how many no in the list in odd and even

# def check_no():
    
#     with open("num.txt","r") as f:
#         count_even =0
#         count_odd =0
#         data = f.read()
#         print(data)
#         num = data.split(",")
#         print(num)

#         for i in num:
#             if(int(i) % 2== 0):
#                 count_even +=1
#             elif(int(i) % 2 ==1):
#                 count_odd +=1
#     print("even no is ",count_even, "odd no is",count_odd)
        
# check_no()