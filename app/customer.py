from app.car import Car
import math


class Customer:

    def __init__(self, name: str, money: float, location: tuple,
                 shopping_cart: dict, car: Car) -> None:
        self.name = name
        self.money = money
        self.location = location
        self.shopping_cart = shopping_cart
        self.car = car
        self.home_location = location

    def trip_cost_to_shop(self, shop, fuel_price: float) -> float:
        dx = shop.location[0] - self.location[0]
        dy = shop.location[1] - self.location[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)


        trip_cost = (distance / 100) * self.car.fuel_consumption
        cost = trip_cost * fuel_price
        return round(cost, 2)
