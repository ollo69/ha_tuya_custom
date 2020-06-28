from .base import TuyaDevice


class TuyaCover(TuyaDevice):

    def open_cover(self):
        """Open the cover."""
        success, response = self.api.device_control(self.obj_id, "turnOnOff", {"value": "1"})
        if success:
            self._update_data("state", True)
        else:
            self._update_data("online", False)

    def close_cover(self):
        """Close cover."""
        success, response = self.api.device_control(self.obj_id, "turnOnOff", {"value": "0"})
        if success:
            self._update_data("state", False)
        else:
            self._update_data("online", False)

    def stop_cover(self):
        """Stop the cover."""
        success, response = self.api.device_control(self.obj_id, "startStop", {"value": "0"})
        if success:
            self._update_data("state", False)
        else:
            self._update_data("online", False)

    def support_stop(self):
        support = self.data.get("support_stop")
        if support is None:
            return False
        return support

    def update(self):
        return self._update(use_discovery=True)
