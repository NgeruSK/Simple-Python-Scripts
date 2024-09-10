class Employee:
    def __init__(self, name, _id, title):
        self.name = name
        self._id = _id
        self.title = title
    
    def do_work(self):
        if self.title == "IT Manager":
            print(self.name,"is lead IT")
        elif self.title == "Procurement":
            print(self.name,"is lead Procurement")
        else:
            print(self.name,"unknown tasks")

    def speak(self):
        print(self.name,"asks how much")

tom = Employee("Tomy Heighs", "909000","Procurement")
tom.do_work()
tom.speak()