class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, food):
        self.items.append(food)

    def remove_item(self, food):
        if food in self.items:
            self.items.remove(food)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


class Menu:
    def __init__(self):
        self.food_items = []

    def add_food(self, food):
        self.food_items.append(food)

    def remove_food(self, food):
        if food in self.food_items:
            self.food_items.remove(food)

    def display_menu(self):
        print("Menu:")
        for food in self.food_items:
            print(f"{food.name} - ${food.price}")


def main():
    menu = Menu()

    # Adding food items to the menu
    menu.add_food(Food("Burger", 5))
    menu.add_food(Food("Pizza", 10))
    menu.add_food(Food("Fries", 3))

    order = Order()

    while True:
        print("\n1. Display Menu")
        print("2. Add Item to Order")
        print("3. Remove Item from Order")
        print("4. Calculate Total")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            menu.display_menu()

        elif choice == "2":
            food_name = input("Enter the food name: ")
            found = False
            for food in menu.food_items:
                if food.name == food_name:
                    order.add_item(food)
                    print("food added ")
            food_qty=int(input("enter the quantities of items "))
            for i in range(food_qty):
                order.add_item(food)
                found = True
                break
        if not found:
                print("Food not found in the menu.")

        elif choice == "3":
            food_name = input("Enter the food name: ")
            found = False
            for food in order.items:
                if food.name == food_name:
                    order.remove_item(food)
                    found = True
                    break
            if not found:
                print("Food not found in the order.")

        elif choice == "4":
            total = order.calculate_total()
            print(f"Total: ${total*food_qty}")

        elif choice == "5":
            print("Thank you for using the food ordering system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
