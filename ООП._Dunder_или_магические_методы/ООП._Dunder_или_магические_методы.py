#задача 1
SIGNATURE = "-~=$([{PETR}])$=~-"
def infiltrate():
    pass

class SignedMessage:
    def __new__(cls, *args, **kwargs):
        infiltrate()
        return object.__new__(cls)
    def __init__(self, message, signature):
        self.message = message
        self.signature = signature
    def __str__(self):
        return f"{self.message} {self.signature}"
    def __add__(self, any):
        return SignedMessage(self.message + any.message, self.signature)


nam = SignedMessage("It's PETR", SIGNATURE)
print(nam)
print(SignedMessage("Hello ", SIGNATURE) + SignedMessage("world ", SIGNATURE))

#задача 2
from functools import reduce
import math
class Vector2:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, obj):
         return Vector2(self.x + obj.x, self.y + obj.y)
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    def __sub__(self, obj):
        return Vector2(self.x-obj.x, self.y - obj.y)
    def __abs__(self):
        return ((self.x)**2+(self.y)**2)**(1/2)
    def __len__(self):
        return ((self.x) ** 2 + (self.y) ** 2) ** (1 / 2)
    def __str__(self):
        return f"<{self.x} {self.y}>"
    def __eq__(self,obj):
        return self.x == obj.x and self.y == obj.y
    def __ne__(self, obj):
        return not (self == obj)
    def __mul__(self, obj):
        return self.x*obj.x + self.y*obj.y
class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z =z
    def __add__(self, obj):
         return Vector3(self.x + obj.x, self.y + obj.y, self.z + obj.z)
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    def __sub__(self, obj):
        return Vector3(self.x-obj.x, self.y - obj.y, self.z-obj.z)
    def __abs__(self):
        return ((self.x)**2+(self.y)**2 + (self.z)**2)**(1/2)
    def __len__(self):
        return ((self.x) ** 2 + (self.y) ** 2 + (self.z)**2) ** (1 / 2)
    def __str__(self):
        return f"<{self.x} {self.y} {self.z}>"
    def __eq__(self,obj):
        return self.x == obj.x and self.y == obj.y and self.z == obj.z
    def __ne__(self, obj):
        return not (self == obj)
    def __mul__(self, obj):
        return self.x*obj.x + self.y*obj.y + self.z*obj.z
a=Vector2(1,2)
b=Vector2(1,3)
print(str(a+b), str(a-b), -a, abs(a), a == b, a != b, a * b)
a=Vector3(1,2,5)
b=Vector3(1,3,7)
print(str(a+b), str(a-b), -a, abs(a), a == b, a != b, a * b)
#задача 3
from random import randint

class Item:
    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color
    def __lt__(self, obj):
            if self.ID < obj.ID:
                return True
            if self.ID > obj.ID:
                return False

            if self.price < obj.price:
                return True
            if self.price > obj.price:
                return False

            if self.rarity > obj.rarity:
                return True
            if self.rarity < obj.rarity:
                return False
            if self.color < obj.color:
                return False
            return False

    def __eq__(self, obj):
        return self.ID == obj.ID and self.price == obj.price and self.rarity == obj.rarity and self.color == obj.color


    def __ne__(self,obj):
        return not self == obj
    def __gt__(self, obj):
        return not self <= obj
    def __le__(self,obj):
        return (self < obj or self == obj)
    def __ge__(self,obj):
        return not self < obj


    def __str__(self):
        return f"[{self.ID}] {self.price}g, {RARITY[self.rarity]}, #{self.color}"

RARITY = ["common", "rare", "epic", "legendary"]


def generate_item():
    return Item(randint(0, 127),
                randint(0, 16) * 1000,
                randint(0, 3),
                hex(randint(0, 16) * 1000000)[2:].zfill(6).upper())


items = [generate_item() for i in range(256)]
items.sort()
print(*items, sep="\n")