from rich.console import Console
from rich.table import Table

class Product:
    
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        
class ProductStore:
    
    def __init__(self, product_list = [], total_sale = 0):
        self.product_list = []
        self.total_sale = total_sale
 
    def add(self, product, amount=0):
        self.product = product
        self.amount = amount
        
        if self.amount < 1:
            raise ValueError("Can't add less than 0 product")
        
        self.product_list.append({"type": self.product.type, 
                                  "name": self.product.name, 
                                  "price": self.product.price * 1.3,
                                  "amount": self.amount,
                                  "sale": 0,
                                  })

    def set_discount(self, identifier, percent, identifier_type='name'):
        self.identifier_type = identifier_type
        self.identifier = identifier
        self.percent = percent
        
        if self.percent < 0 or self.percent > 100:
            raise ValueError("Discount can't be less than 0 or more than 100 percent")
        
        if self.identifier_type == "name":
            for prod in self.product_list:
                if identifier == prod["name"]:
                    prod["price"] = prod["price"] - prod["price"] * self.percent / 100
        
        elif self.identifier_type == "type":
            for prod in self.product_list:
                if identifier == prod["type"]:
                    prod["price"] = prod["price"] - prod["price"] * self.percent / 100 
    
    def sell_product(self, product_name, amount):
        self.product_name = product_name
        self.amount = amount
        
        for prod in self.product_list:
            if self.product_name == prod["name"]:
                if prod["amount"] < self.amount:
                    raise ValueError("The sale quantity can't exceed the balance of the goods")
                else:
                    prod["amount"] -= self.amount
                    prod["sale"] += prod["price"] * amount
                    self.total_sale += prod["price"] * amount
    
    def get_income(self):
        return self.total_sale
    
    def get_all_products(self):
        
        table = Table(title="Product")

        table.add_column("Type")
        table.add_column("Name")
        table.add_column("Price")
        table.add_column("Amount")
        table.add_column("Sale")

        for prod in self.product_list:
            table.add_row(
                prod["type"],
                prod["name"],
                str(prod["price"]),
                str(prod["amount"]),
                str(prod["sale"])
            )

        console = Console()
        console.print(table)
    
    def get_product_info(self, product_name):
        self.product_name = product_name
        
        for prod in self.product_list:
            if  prod["name"] == product_name:
                return (prod["name"], prod["amount"])
        return "Product not found"


t_shirt = Product('Sport', 'Football T-Shirt', 100)
ramen = Product("Food", "Ramen", 1)
ramen_hot = Product("Food", "Ramen_hot", 2)

store_1 = ProductStore()

store_1.add(ramen, 300)
store_1.add(ramen_hot, 300)
store_1.add(t_shirt, 10)

store_1.sell_product('Ramen', 40)
store_1.sell_product('Football T-Shirt', 1)

store_1.set_discount("Ramen", 10)
store_1.set_discount("Food", 20, "type")

store_1.sell_product('Ramen', 10)

store_1.get_all_products()

print(store_1.get_product_info("Ramen"))
print(store_1.get_product_info("Ramen11"))