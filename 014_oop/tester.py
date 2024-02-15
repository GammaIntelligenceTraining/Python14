class Employee:

    def __init__(self, first: str, last: str, pay: int):
        self.__first = first
        self.__last = last
        self.__pay = pay

    # GETTER
    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @property
    def pay(self):
        return self.__pay

    @property
    def email(self):
        return  f'{self.__first.lower()}.{self.__last.lower()}@example.com'

    @property
    def fullname(self) -> str:
        return f'{self.__first} {self.__last}'

    @fullname.setter
    def fullname(self, name_str):
        first, last = name_str.split()
        self.__first = first
        self.__last = last

    @fullname.deleter
    def fullname(self):
        self.__first = None
        self.__last = None

emp1 = Employee('Jack', 'Smith', 2000)

print(emp1.fullname)
emp1.fullname = 'Bob Dylan'
del emp1.fullname
print(emp1.fullname)
