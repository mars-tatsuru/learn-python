# import requests
# print(requests.get("https://www.python.jp").text)

name = 'tatsuru'
# name = 'takeshi'

# print(name)

# if name == 'tatsuru':
#     print('hello tatsuru')
# elif name == 'takeshi':
#     print('hello takeshi')

# friends = ['tatsuru', 'takeshi', 'satoshi']
# for friend in friends:
#     print(friend)

# friends_members = input('input your friends name: ')

# if friends_members in friends:
#     print(friends_members + ' is your friend')


friends_age = [
    {'name': 'tatsuru', 'age': 30},
    {'name': 'tatsuru', 'age': 30},
    {'name': 'tatsuru', 'age': 30},
]

# print(friends_age[1]["name"])

# for friend in friends_age:
#     print(f"{friend['name']} is {friend['age']}")

# print(friends_age[1].items())

# def add(a, b):
#     return a + b

# print(add(1, 2))


# users = [
#     (0, 'tatsuru', "aaaa"),
#     (1, 'takeshi', "aaaa"),
#     (2, 'manami', "aaaa"),
#     (3, 'monmo', "aaaaa"),
# ]


# user_mapping = {user[1]: user for user in users}

# username_input = input('input your name: ')
# userpassword_input = input('input your password: ')

# _, username, password = user_mapping[username_input]

# if userpassword_input == password:
#     print('your login is success')
# else:
#     print('your login is failed')


# def named(arg, **kwargs):
#     print(arg,kwargs)

# named(arg=[1,2,3],name="tatsuru",age=30)



# class Store:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.items = []

#     def add_item(self, name, price):
#         item = {"name": name, "price": price}
#         self.items.append(item)

#     def stock_price(self):
#         return sum([item["price"] for item in self.items])

#     def __str__(self):
#         return f"{self.name} has {len(self.items)} items."

# store = Store("tatsuru",100)
# print(store.add_item("tatsuru",100))
# print(store.stock_price())
# print(store.__str__())




# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")

#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")

#     @staticmethod
#     def static_method():
#         print("Called static_method")

# # test = ClassTest()
# # test.instance_method()
# ClassTest.static_method()


# class Book:
#     TYPES = ("hardcover", "paperback")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight

#     def __repr__(self):
#         return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return cls(name, cls.TYPES[0], page_weight + 100)

#     @classmethod
#     def paperback(cls, name, page_weight):
#         return cls(name, cls.TYPES[1], page_weight)


# book = Book.hardcover("Harry Potter", 1500)
# light = Book.paperback("Harry Potter", 1500)

# print(book)
# print(light)


# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"

#     def disconnect(self):
#         self.connected = False
#         print("Disconnected.")

# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

#     def print(self, pages):
#         if not self.connected:
#             print("Your printer is not connected!")
#             return
#         print(f"Printing {pages} pages.")
#         self.remaining_pages -= pages


# class BookShelf:
#     def __init__(self, *books):
#         self.books = books

#     def __str__(self):
#         return f"BookShelf with {len(self.books)} books."

# class Book:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Book {self.name}"

# book = Book("Harry Potter")
# # book2 = Book("Python 101")
# shelf = BookShelf(book)

# print(shelf)



# def divide(dividend, divisor):
#     if divisor == 0:
#         return dividend / divisor

# grades = [1,2,3,4,5]

# print("Welcome to the average grade program.")
# try:
#     average = divide(sum(grades), len(grades))
#     print(f"The average grade is {average}.")
# except ZeroDivisionError as e:
#     print(e)
#     print("There are no grades yet in your list.")


# class Book:
#     def __init__(self, name: str, page_count: int):
#         self.name = name
#         self.page_count = page_count
#         self.page_read = 0

#     def __repr__(self):
#         return f"<Book {self.name}, read {self.page_read} pages out of {self.page_count}>"

#     def read(self, page_count: int):
#         self.page_read += page_count
#         print(f"You have now read {self.page_read} pages out of {self.page_count}")


# from operator import itemgetter

# def search (sequense, expected, finder):
#     for elem in sequense:
#         if finder(elem) == expected:
#             return elem
#     raise RuntimeError(f"Could not find an element with {expected}.")

# friends = [
#     {"name": "Rolf Smith", "age": 24},
#     {"name": "Adam Wool", "age": 30},
#     {"name": "Anne Pun", "age": 27},
# ]

# print(search(friends, "Rolf Smith", itemgetter("name")))

# import functools

# user = {"username": "jose123", "access_level": "admin"}

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function(*args, **kwargs):
#         if user["access_level"] == "admin":
#             return func(*args, **kwargs)
#         else:
#             return f"No admin permissions for {user['username']}."

#     return secure_function

# @make_secure
# def get_password(pannel):
#     if pannel == 'admin':
#         return "1234"
#     elif pannel == 'billing':
#         return "super_secure_password"

# print(get_password('billing'))


# *args, **kwargsについて
# def my_function(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(key, value)

# my_function(1, 2, 3, a=4, b=5, c=6)


# a = 'hello'
# b = a

# print(id(a))
# print(id(b))

# a += ' world'


# print(a)
# print(id(b))

# from typing import List, Optional


# class Student:
#     def __init__(self, name: str, grades:Optional[List[int]] = None):
#         self.name = name
#         self.grades = grades or []

#     def take_exam(self, result):
#         self.grades.append(result)

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)

# bob = Student("Bob")
# rolf = Student("Rolf")
# bob.take_exam(90)
# print(bob.grades)
# print(rolf.grades)
# # print(bob.average_grade())
