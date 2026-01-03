import json
from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip():
    with open("config.json", "r") as file:
        trades = json.load(file)
        fuel_price = trades["FUEL_PRICE"]
        customs = trades["customers"]
        shops = trades["shops"]

        shop_objects = []
        for shop_data in shops:
            name = shop_data["name"]
            location = tuple(shop_data["location"])
            products = shop_data["products"]

            shop = Shop(name=name, location=location, products=products)
            shop_objects.append(shop)

        customer_objects = []
        for cust_data in customs:
            car = Car(
                brand=cust_data["car"]["brand"],
                fuel_consumption=cust_data["car"]["fuel_consumption"]
            )

            customer = Customer(
                name=cust_data["name"],
                money=cust_data["money"],
                location=tuple(cust_data["location"]),
                shopping_cart=cust_data["product_cart"],
                car=car
            )
            customer_objects.append(customer)


if __name__ == "__main__":
    shop_trip()
