from clazz_hierarchy.FuelAware import FuelAware
from clazz_hierarchy.MoveDirections import MoveDirections as Move


class Car(FuelAware):
    def __init__(self, initial_fuel=FuelAware.get_default_fuel()):
        super().__init__(initial_fuel)
        self.__speed = 0
        self.__pos = (0, 0)
        self.__dir = Move.UP

    def accelerate(self, amount):
        self.consume_fuel(amount)
        self.__speed += amount

    def turn(self, direction):
        self.__dir = direction

    def update_position(self, position):
        self.__pos = position

    def move(self):
        self.consume_fuel(self.__speed)
        if self.__dir == Move.UP:
            self.update_position((self.__pos[0], self.__pos[1] + self.__speed))
        elif self.__dir == Move.RIGHT:
            self.update_position((self.__pos[0] + self.__speed, self.__pos[1]))
        elif self.__dir == Move.DOWN:
            self.update_position((self.__pos[0], self.__pos[1] - self.__speed))
        elif self.__dir == Move.LEFT:
            self.update_position((self.__pos[0] - self.__speed, self.__pos[1]))
        else:
            raise Exception("Invalid direction")

    def print_state(self):
        print("======================================")
        print("Position: " + str(self.__pos))
        print("Direction: " + str(self.__dir))
        print("Speed: " + str(self.__speed))
        print("Fuel: " + str(self.remaining_fuel()))
