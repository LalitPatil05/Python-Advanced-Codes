class Student:
    def Getdata(self, rollno, name, marks):
        #rollno = int(input("Enter the Roll Number : "))
        #name = input("Enter the Name : ")
        #marks = float(input("Enter the Marks : "))
        rollno = self.rollno
        name = self.name
        marks = self.marks

    def Display(self):
        print("Roll no. is : ",rollno)
        print("Name is : ",name)
        print("Marks is : ",marks)


obj = Student()

obj.Getdata(101,"Lalit",90)

obj.Display()
