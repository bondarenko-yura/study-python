DEFAULT_TELEPORT_COUNT = 3


class TeleportAware:
    def __init__(self, initial_teleport_count=DEFAULT_TELEPORT_COUNT):
        self.__remain_teleport_count = initial_teleport_count

    @staticmethod
    def get_default_teleport_count():
        return DEFAULT_TELEPORT_COUNT

    def remaining_teleport_count(self):
        return self.__remain_teleport_count

    def consume_teleport(self):
        if self.__remain_teleport_count <= 0:
            raise Exception("No more teleports")
        self.__remain_teleport_count -= 1

    def teleport(self, position):
        pass
