import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "Shusaku Yusa"
person.email = "shu.yus@example.com"
phone = person.phones.add()
phone.number = "111-222"
phone.type = addressbook_pb2.Person.HOME
print(person)
print(phone)
