class user:
    obj1 = 3
    obj2 = 2
    obj3 = 16
    
    def compare(self):
        if self.obj1>self.obj2 and self.obj1>self.obj3:
            print(self.obj1)
        elif self.obj2>self.obj1 and self.obj2>self.obj3:
            print(self.obj2)
        else:
            print(self.obj3)

ob = user()

ob.compare()
