
class Product:

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def in_stock(self, count):
        return self.quantity >= count

    def deduct(self, quantity):
        self.quantity -= quantity

    #Use to see if number of items are available
    def countAmount(self, number):
        return self.quantity >= number


    #Use to count cost of items
    def countCost(self, number):
        return self.price * number


class Store:

    def __init__(self):
        self.product_list = [
            Product(0, "Ultrasonic range finder", 2.5, 4),
            Product(1, "Servo motor", 14.99, 10), 
            Product(2, "Servo controller", 44.95, 5), 
            Product(3, "Microcontroller Board", 34.95, 7), 
            Product(4, "Laser range finder", 149.99, 2),
            Product(5, "Lithium polymer battery", 8.99, 8)
        ]

    def get(self, id):
        product = None
        for p in self.product_list:
            if p.id == id:
                product = p
                break
        return product

    def display(self):
        '''
        Dislays the current stock.
        '''
        print("\nAvailable product:")
        for product in self.product_list:
            if product.quantity > 0:
                print(f"{product.id}) {product.name} ${product.price} {product.quantity} in stock")

    def purchase(self, id, quantity):
        '''
        @id the id of the product to buy
        @quantity the total number of product to buy
        '''
        for product in self.product_list:
            if product.id == id:
                if product.in_stock(quantity):
                    product.deduct(quantity)
                else:
                    print("Not enough product.")


def main():
    print("Welcome to store!")
    money = float(input("How much money do you have?: "))
    store = Store()

    while money > 0:
        store.display()
        user_input = input("Enter id and quantity of what you want to buy separated by a space: ")

        if user_input == "exit":
            break

        vals = user_input.split(" ")

        id = int(vals[0])
        quantity = int(vals[1])

        product = store.get(id)

        if product == None:
            print(f"Couldn't find product with id {product.id}")
            continue

        if product.quantity < quantity:
            print("Not enough product.")
            continue

        total_cost = product.price * quantity

        if total_cost > money:
            print("Not enough money.")
            continue

        product.deduct(quantity)
        money -= total_cost

        print(f"You have {money} remaining.")

    print("Thanks for shopping!")

main()
