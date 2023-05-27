class Menu:

    def __init__(self) :
        self.food_items=[] # empty list of food items 



    def add_food(self, food):
        self.food_items.append(food) # food items list me append krenge



    def remove_food(self, food):
       if  food in self.food_items:
           self.food_items.remove(food)
           return True
       


    def display_menus(self):
       print("menus")
       for food in self.food_items:
           print(f"{food.name} - ${food.price}")