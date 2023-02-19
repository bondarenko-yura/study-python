from clazz_hierarchy.Car import Car
from clazz_hierarchy.FuelAware import FuelAware
from clazz_hierarchy.TeleportAware import TeleportAware
from clazz_hierarchy.MoveDirections import MoveDirections as Move

# from clazz_hierarchy import MoveDirections as Move


class FutureCar(Car, TeleportAware):
    def __init__(self):
        Car.__init__(self)
        TeleportAware.__init__(self)

    def teleport(self, position):
        self.consume_teleport()
        self.update_position(position)

    def print_state(self):
        super().print_state()
        print("Teleport count: " + str(self.remaining_teleport_count()))


car = FutureCar()
car.accelerate(10)
car.turn(Move.RIGHT)
car.move()
car.print_state()
car.teleport((99, 99))
car.print_state()

print("found Car" if isinstance(car, Car) else "Not Car")
print("found FuelAware" if isinstance(car, FuelAware) else "Not FuelAware")
print("found TeleportAware" if isinstance(car, TeleportAware) else "Not TeleportAware")
print("found FutureCar" if isinstance(car, FutureCar) else "Not FutureCar")

custom = FutureCar()
custom.my_custom_attribute = "Hello"
print(custom.__class__.__name__ + ": has custom attribute" + custom.my_custom_attribute)


# print all parent classes of FutureCar
def inspect_class(clazz, intent=0):
    print("-" * 80)
    pref = (" " * intent)
    print(pref + "Inspecting class " + clazz.__name__)
    print(pref + "Parents:")
    for parent in clazz.__bases__: # __bases__ is a tuple of all parent classes
        print(pref + " > " + parent.__name__)
    print(pref + "Attributes:")
    for attr in clazz.__dict__:  # __dict__ is a dictionary of all attributes
        if not attr.startswith("__"):
            print(pref + " > " + attr + ": " + type(clazz.__dict__[attr]).__name__)
    for parent in clazz.__bases__:
        inspect_class(parent, intent + 1)


inspect_class(FutureCar)
