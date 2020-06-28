
from .base import TuyaDevice


class TuyaSwitch(TuyaDevice):

    def turn_on(self):
        success, response = self.api.device_control(self.obj_id, "turnOnOff", {"value": "1"})
        if success:
            self._update_data("state", True)
        else:
            self._update_data("online", False)

    def turn_off(self):
        success, response = self.api.device_control(self.obj_id, "turnOnOff", {"value": "0"})
        if success:
            self._update_data("state", False)
        else:
            self._update_data("online", False)

    def update(self):
        return self._update(use_discovery=True)
