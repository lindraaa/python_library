name_array = []

class library:
    def __init__(self):
        self.firstname = input("Enter firstname: ")
        self.lastname = input("Enter lastname: ")
        self.age= input("Enter age: ")
 
    def shownames(self):
        print("Firstname: ", self.firstname, "|| Lastname: " , self.lastname ,"|| Age : ", self.age)

name1 = library()
name2 = library()
name3 = library()

name1.shownames()
name2.shownames()
name3.shownames()
