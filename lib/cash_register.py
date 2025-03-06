class CashRegister:
    def __init__(self, discount=None):
        self.total = 0.0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.items.append({"title": title, "price": price, "quantity": quantity})
        self.total += price * quantity

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * self.discount
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.") 
            return self.total
        else:
            print("There is no discount to apply.")

    def remove_last_item(self):
        if self.items:
            last_item = self.items.pop()  
            self.total -= last_item["price"] * last_item["quantity"]
        else:
            print("No items to remove.")  