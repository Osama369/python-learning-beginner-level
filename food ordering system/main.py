from food import Food
from order import Order
from menu import Menu

def main(): # main function 

 menus= Menu()

 # adding food items into menus
 menus.add_food(Food("pizza", 1000))
 menus.add_food(Food("Biryani", 200))
 menus.add_food(Food("samoosa",50))
 

 while True:
  print("\n 1. disaplay Menu")
  print("\n 2 add Items to  Order")
  print ("\n 3.remove Items to Order")
  print("\n 4. calculate Total")
  print("\n 5. exit")

  choice = int(input("Enter your choice "))
  if choice == 1:
   menus.display_menus()


   if __name__== "__main__":
     main()








