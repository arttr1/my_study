# class Phone:
#     def __init__ (self, number, name):
#         self.number = number
#         self.name = name

#     def __str__(self):
#         return f'Number: {self.number}, Name: {self.name}'
    
class PhoneBook: 
    def __init__(self):
        self.contacts = {}
    def add_contact(self, number, name):
        self.contacts[number] = name

    def check_caller(self, number):
        return self.contacts.get(number, 'Number is not defined')
    
    def send_message(self, target, message):
        if target in self.contacts.values():
            # Ищем номер по имени
            for number, name in self.contacts.items():
                if name == target:
                    return f"Сообщение '{message}' отправлено ({number} {name})"
        elif target in self.contacts.keys():
            # Ищем по номеру
            return f"Сообщение '{message}' отправлено ({target} {self.contacts[target]})"
        else:
            return "Контакт не найден"

# Создание телефонной книги
phone_book = PhoneBook()


phone_book.add_contact("1234567890", "Иван")
phone_book.add_contact("9876543210", "Мария")
phone_book.add_contact("5555555555", "Петр")
phone_book.add_contact("1111111111", "Анастасия")
phone_book.add_contact("2222222222", "Дмитрий")

# Проверка номера звонящего
print(phone_book.check_caller("1234567890"))  # Иван
print(phone_book.check_caller("9999999999"))  # Номер не определен

# Отправка сообщения
print(phone_book.send_message("Иван", "Привет!"))
print(phone_book.send_message("1234567890", "Привет!"))
print(phone_book.send_message("Неизвестный", "Привет!"))


# попоробовать сделать проверку чтобы номера соответсвовали маске
