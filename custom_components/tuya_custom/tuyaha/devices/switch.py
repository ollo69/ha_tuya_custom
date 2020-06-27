
from .base import TuyaDevice


class TuyaSwitch(TuyaDevice):

    def turn_on(self):
        self.api.device_control(self.obj_id, "turnOnOff", {"value": "1"})
        self._update_data("state", True)

    def turn_off(self):
        self.api.device_control(self.obj_id, "turnOnOff", {"value": "0"})
        self._update_data("state", False)

    def update(self):
        return self._update(use_discovery=True)
