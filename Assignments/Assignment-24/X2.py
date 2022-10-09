class user:
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        print("Welcome to Ineuron school",self.name)
obj = user(input("Enter you are name : "))
obj.greet()
