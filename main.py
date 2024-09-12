class Person: 
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print("Name: ", self.name, "\nID: ", self.id)

class Employee(Person):    
    def __init__(self, name, id, salary, post):
            Person.__init__(self, name, id)
            self.salary = salary
            self.post = post

x = str(input("Enter your name: "))
y = int(input("Enter your id: "))
z = float(input("Enter your salary: "))
v = str(input("Enetr your post: "))
print("\n Your details:- ")
Emp = Employee(x, y, z, v)
Emp.display()