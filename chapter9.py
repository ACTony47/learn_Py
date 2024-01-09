# # 类 面向对象编程
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f"{self.name} is now sitting")
#
#     def roll_over(self):
#         print(f"{self.age} is now rolling over")
#
#
# my_dog = Dog("william", 6)
# print(f"{my_dog.name} is dog's name")
class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type
        self.number_servers = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.restaurant_type} restaurant")

    def increment_number_served(self, num):
        self.number_servers = num
        print(f"{self.restaurant_name} can serve {self.number_servers} guests")

class Chinese_Restaurant(Restaurant):
    def __init__(self, name, type, host):
        super().__init__(name, type)
        self.owner = host

    def describe_restaurant(self):
        print(f"{self.owner} owns this dinner hall and its name is {self.restaurant_name}")

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = []

    def show_flavors(self):
        for flavor in self.flavors:
            print(f"we {self.restaurant_name} serves {flavor} icecream")

    def add_flavors(self):
        for i in range(3):
            flavor = input('enter flavor:')
            self.flavors.append(flavor)


