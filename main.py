from collections import UserDict


class AddressBook(UserDict):
    
    def add_record(self, rec):
        self.data[rec.name.value] = rec 


class Record:
    
    def __init__(self, name, phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i.value == old_phone.value:
                i.value = new_phone.value

    def delite_phone(self, phone):
        for i in self.phones:
            if i.value == phone.value:
                self.phones.remove(phone)



class Field:

    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')

