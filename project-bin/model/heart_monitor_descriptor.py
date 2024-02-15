import json


class HeartMonitorDescriptor:

    def __init__(self, id_room, id_bed):
        """
        Describes the data for the Heart Monitor.
        The monitor is uniquely identified by the tuple (id_room, id_bed), where id_room represents the room identifier and id_bed represents the bed identifier.
        :param id_room: Room id.
        :type id_room: str
        :param id_bed: Bed id.
        :type id_bed: str
        """
        self.id_room = id_room
        self.id_bed = id_bed


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)