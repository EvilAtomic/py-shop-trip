from datetime import datetime

class Shop:

    def __init__(self, name: str, location: tuple, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def shop_products(self, shopping_cart: dict) -> float:
        total = 0
        for product, play in shopping_cart.items():
            price = self.products.get(product)
            if product is None:
                return None
            total += price * play
        return  total

    def chek_price(self, shopping_cart: dict) -> float:
        correct_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("DATA:", correct_time)

        total = 0
        for product, play in shopping_cart.items():
            if product in self.products:
                price = self.products[product]
                cost = price * play
                total += cost
                print(f"{play} {product} за {cost} money")

        print(f"result: {total} money")
        return total
