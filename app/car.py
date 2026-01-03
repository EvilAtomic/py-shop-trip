class Car:

    def __init__(self, marks: str, fuel_price: float) -> None:
        self.marks = marks
        self.fuel_price = fuel_price

    def fuel_cost(self, distance: float, fuel_consumption: float) -> float:
        liters = distance * fuel_consumption / 100
        cost = liters * self.fuel_price
        return cost
