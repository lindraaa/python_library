class library:
    def __init__(self, firstname,lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age= age
 
    def shownames(self):
        print(f"Firstname:  {self.firstname}|| Lastname:  {self.lastname} || Age : {self.age}")

firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
age = input("Enter age: ")

listofnames = library(firstname,lastname,age)
listofnames.shownames()
