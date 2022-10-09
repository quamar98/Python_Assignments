class Laptop:
    
    def __init__(self):
        self.brand = "Apple"
        self.ram = "8gb"
        self.cpu = "8core"
        self.ssd = "256gb"
        
    def showConfig(self):
        print("Brand : ",self.brand)
        print("Ram : ",self.ram)
        print("CPU : ",self.cpu)
        print("SSD : ",self.ssd)
        
obj = Laptop()
obj.showConfig()
