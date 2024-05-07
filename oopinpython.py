
class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        
        print("your name is ", self.name ,"and your average marks is",sum/3)




s1 = Student("ahmad" , [90,92,94])
s1.name="zeeshan"
s1.get_avg()
