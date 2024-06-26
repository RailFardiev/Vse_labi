import time

class Ticket:
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket: ", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print("createDate: ", time.asctime(self.createDate))
        print("owner: ", self.owner)
        print("deadline: ", time.strftime("%d.%m.%Y", self.deadline))

# Создание объекта класса
ticket1 = Ticket(time.localtime(), "Rail Fardiev", time.strptime("13.03.2023", "%d.%m.%Y"))
# Вызов метода
ticket1.display()
# Получение значения атрибута
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))
# Проверка наличия атрибута
print("hasattr: ", hasattr(ticket1, "owner"))
setattr(ticket1, "owner", "Vasikiy Stalin")  # Установка значения атрибута
print("Owner(setattr): ", ticket1.owner)
delattr(ticket1, "owner")  # Удаления значения атрибута
print("After delattr: ", hasattr(ticket1, "owner"))
del ticket1  # Удаление объекта

# Получение текущего времени и вывод на экран
current_time = time.localtime()
formatted_time = time.strftime("%d %b %Y %H:%M:%S", current_time)
print("Current time: ", formatted_time)

# Создание объекта time с указанным временем и форматирование в нужный вид
specified_time = time.strptime("17.07.2017 10:53:00", "%d.%m.%Y %H:%M:%S")
formatted_specified_time = time.strftime("%d %b %Y %H:%M:%S", specified_time)
print("Specified time: ", specified_time)
print("Specified time2: ", formatted_specified_time)