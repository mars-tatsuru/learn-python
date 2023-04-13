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



class Store:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.items = []

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        return sum([item["price"] for item in self.items])

    def __str__(self):
        return f"{self.name} has {len(self.items)} items."

store = Store("tatsuru",100)
print(store.add_item("tatsuru",100))
print(store.stock_price())
print(store.__str__())
