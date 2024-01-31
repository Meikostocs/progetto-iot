import json
from request.oxygenation_request import OxygenationRequest as oxi_req
class Oxygenator:

    def __init__(self, room_id, bed_id):
        self.room_id= room_id
        self.bed_id = bed_id
        self.oxigenation_state = oxi_req.OXYGENATION_STOP

    def set_oxigenation_state(self,level):
        self.oxigenation_state = level

    def to_json(self):
        #return json.dumps(self, default=lambda o: o.__dict__)
        return json.dumps(self, default=lambda o: o.value if isinstance(o, Enum) else o.__dict__)