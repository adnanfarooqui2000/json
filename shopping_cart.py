class MyCart:
    def __init__(self):
        self.my_items = []

    def add_item(self, item, price):
        # Convert price to float to handle both integers and decimals
        self.my_items.append({'item_name': item, 'item_price': float(price)})

    def show_items(self):
        if len(self.my_items) == 0:
            print("Cart is empty")  # Fixed typo: empyty -> empty
        else:
            print("All cart details are:")
            for i in self.my_items:
                print(i['item_name'], '=', i['item_price'])
    
    def total_price(self):
        total = 0
        for i in self.my_items:
            total += i["item_price"]
        print("Total Amount =", total)
    
    def remove_item(self, item_name):
        item_found = False
        for item in self.my_items:
            if item["item_name"] == item_name:
                self.my_items.remove(item)
                item_found = True
                print(f"'{item_name}' removed from cart")
                break
        if not item_found:
            print(f"Item '{item_name}' not found in cart")
    
    def clear_cart(self):
        self.my_items = []
        print("Now your cart is empty...")  # Fixed typo: empity -> empty

# Test the class
obj = MyCart()
obj.add_item('Laptop', 25000)  # Pass price as number, not string
obj.add_item('Table_Lamp', 5000)
obj.add_item('Decor', 2000)
obj.show_items()
obj.total_price()
obj.remove_item('Laptop')
obj.show_items()
obj.total_price()
obj.clear_cart()
obj.show_items()