class ScannedItem:
   def __init__(self, item_name, price, quantity, category):
       self.item_name = item_name
       self.price = price
       self.quantity = quantity
       self.category = category
  
   def get_item_details(self):
       subtotal = self.price * self.quantity
       return f"""[BEEP!] {self.item_name:<15}
       | {self.quantity} x {self.price} RWF
       | Category: {self.category:<10}
       | Subtotal: {subtotal} RWF"""
   def get_grand_total(self):
       grand_total = sum(item.price * item.quantity for item in simba_cart)
       return f"Grand Total: {grand_total} RWF"

simba_cart = [ScannedItem("CocaCola", 1200, 1, "Drinks"), ScannedItem("Winnaz", 1000, 2, "Snacks"), ScannedItem("Fanta", 1200, 1, "Drinks"), ScannedItem("Pepsi", 1200, 1, "Drinks")]

# The cashier scans your first item:
winnaz = ScannedItem("Winnaz Chips", 1000, 2, "Snacks")
print(winnaz.get_item_details())
print(winnaz.get_grand_total())
