from collections import UserDict

class Field:
    """Базовий клас для полів запису"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Клас для зберігання імені контакту"""
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    """Клас для зберігання номера телефону з валідацією"""
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону повинен складатися рівно з 10 цифр.")
        super().__init__(value)

class Record:
    """Клас для зберігання інформації про контакт"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        """Додати номер телефону до контакту"""
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        """Видалити номер телефону з контакту"""
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_number, new_number):
        """Редагувати номер телефону"""
        for idx, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[idx] = Phone(new_number)
                return
        raise ValueError("Старий номер телефону не знайдено.")

    def find_phone(self, phone_number):
        """Знайти номер телефону в контакті"""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phones_str = "; ".join(phone.value for phone in self.phones)
        return f"Ім'я контакту: {self.name.value}, телефони: {phones_str}"

class AddressBook(UserDict):
    """Клас для зберігання та управління записами контактів"""
    
    def add_record(self, record):
        """Додати запис до адресної книги"""
        self.data[record.name.value] = record

    def find(self, name):
        """Знайти запис за ім'ям"""
        return self.data.get(name, None)

    def delete(self, name):
        """Видалити запис з адресної книги"""
        if name in self.data:
            del self.data[name]
            return True
        return False

    def __str__(self):
        if not self.data:
            return "Адресна книга порожня."
        return "\n".join(str(record) for record in self.data.values())

