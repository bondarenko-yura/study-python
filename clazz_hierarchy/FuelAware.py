DEFAULT_FUEL_SUPPLY = 100


class FuelAware:
    def __init__(self, initial_fuel=DEFAULT_FUEL_SUPPLY):
        self.__fuel = initial_fuel

    @staticmethod
    def get_default_fuel():
        return DEFAULT_FUEL_SUPPLY

    def remaining_fuel(self):
        return self.__fuel

    def consume_fuel(self, amount):
        if amount > self.__fuel:
            raise Exception("Not enough fuel")
        self.__fuel -= amount

    def refuel(self, amount):
        self.__fuel += amount
