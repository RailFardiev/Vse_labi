class Worker:
    'doc class Worker'
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1
        self.id = Worker.count

    def display(self):
        print("Worker: ")
        print("{} {}".format(self.name, self.surname))

class Animal:
    count = 0

    def __init__(self, name, age):
        Animal.count += 1
        self.id = Animal.count
        self.name = name
        self.age = age

    def display(self):
        print("Animal id: ", self.id)
        print("Name: ", self.name)
        print("Age: ", self.age)


w1 = Worker("Rail", "Fardiev")
print("w1.count: ", w1.count)
w2 = Worker("Anton", "Gromov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count:  {0} \n".format(Worker.count))

# Создание трех объектов класса Animal и вывод информации о них
a1 = Animal("Frog", 5)
a2 = Animal("Lion", 3)
a3 = Animal("Dog", 2)

a1.display()
a2.display()
a3.display()