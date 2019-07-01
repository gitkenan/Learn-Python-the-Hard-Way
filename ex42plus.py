class MyClass(object): # my class is-a object

    def set_val(self, val): # myclass has-a value
        self.value = val

    def get_val(self): 
        print(self.value)
        return self.value

a = MyClass()
b = MyClass()
c = MyClass()


a.set_val(10)
b.set_val(100)
c.set_val(1000)

a.get_val()
b.get_val()
c.get_val()
