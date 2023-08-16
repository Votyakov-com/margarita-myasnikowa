#задача 1
class CoffeeMachine():
    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        self.water_level += amount
    def add_coffee(self, amount):
        self.coffee_level+=amount
    def add_milk(self, amount):
        self.milk_level+=amount

    def add_sugar(self, amount):
        self.sugar_level+=amount

    def add_cups(self, number):
        self.cups+=number

    def check_resources(self):
        if (self.water_level)*(self.coffee_level)*(self.milk_level)*(self.sugar_level)*(self.cups)>0:
            return True
        else: False

    def make_coffee(self):
        if self.check_resources():
            self.water_level-=1
            self.coffee_level-=1
            self.milk_level-=1
            self.sugar_level-=1
            self.cups-=1
            print("Кофе готов!")
        else:
            print("Недостаточно ингридиентов")


#задача 2
class PhotoCamera():
    def __init__(self,brand = "Canon",model="Extra", resolution = (1024,768),is_on=False,memory_capacity=8,photos=[]):
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.is_on=is_on
        self.memory_capacity = memory_capacity
        self.photos =photos
    def take_photos(self):
        print(f"Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]}.")
    def get_camera_info(self):
        print( f"Марка: {self.brand}, Модель: {self.model}, Разрешение: {self.resolution[0]}x{self.resolution[1]}.")
    def turn_on(self):
        self.is_on = True
        print("Фотокамера включена.")
    def turn_off(self):
        self.is_on =False
        print("Фотокамера выключена.")
    def is_camera_on(self):
        return self.is_on
    def store_photo(self,photo):
        if self.memory_capacity>0:
            self.memory_capacity-=1
            self.photos.append(photo)
            return True
        else:
            return False

    def view_photos(self):
        print( self.photos)
    def clear_memory(self):
        self.memory_capacity= 8
        self.photos =[]

#задача 3
import random
class Revolver():
    def __init__(self, gun_grum =[None]*6,index= 0,v3=6):
        self.v3=v3
        self.gun_drum =gun_grum
        self.index = index
    def add_bullet(self,bullet):
            for i in range(self.index,self.index+6):
                iterat = i%self.v3
                if self.gun_drum[iterat] == None:
                    self.gun_drum[iterat] = bullet
                    return True


            return False
    def add_bullets_from_list(self,b_list):
        if not b_list:
            return False
        added_bullet = 0
        for bullet in b_list:
            if self.add_bullet(bullet):
                added_bullet+=1
        return added_bullet >0



    def shoot(self):
        bullet = self.gun_drum[self.index]
        self.gun_drum[self.index] = None
        self.index =(self.index  +1)%6
        return bullet
    def unload(self,all_items=False):
        buk =[]
        if all_items:
            for bullet in self.gun_drum:
                if bullet!=None:
                    buk.append(bullet)
            self.gun_drum=[None]*6
            return buk

        else:
            bullet = self.gun_drum[self.index]
            self.gun_drum[self.index] = None
            return bullet
    def scroll(self):
        self.index = random.randint(0, self.v3-1)

    def bullet_count(self):
            return sum(bullet is not None for bullet in self.gun_drum)

revolver = Revolver()
revolver.add_bullet("bullet 1")
revolver.add_bullets_from_list(["bullet 2","bullet 3"])
print(list(revolver.gun_drum)) # ['bullet 1', 'bullet 2', 'bullet 3', None, None, None]

revolver.shoot()
print(list(revolver.gun_drum)) # [None, 'bullet 2', 'bullet 3', None, None, None]

revolver.unload()
print(list(revolver.gun_drum)) # [None, None, 'bullet 3', None, None, None]

revolver.add_bullet("bullet 1")
revolver.unload(all_items=True)
print(list(revolver.gun_drum)) #[None, None, None, None, None, None]

revolver.bullet_count()
print(list(revolver.gun_drum)) #[None, None, None, None, None, None]