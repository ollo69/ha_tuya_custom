from .base import TuyaDevice


class TuyaClimate(TuyaDevice):

    def __init__(self, data, api):
        super().__init__(data, api)
        self._unit = None
        self._divider = 0

    def _set_decimal(self, val):
        if val is None:
            return None
        if self._divider == 0:
            if val > 500 or val < -100:
                self._divider = 100
            else:
                self._divider = 1

        return round(float(val / self._divider), 2)

    def has_decimal(self):
        return self._divider > 1

    def temperature_unit(self):
        if not self._unit:
            if self.current_temperature() > 40 and not self.has_decimal():
                self._unit = "FAHRENHEIT"
            else:
                self._unit = self.data.get("temp_unit")
        return self._unit

    def current_humidity(self):
        pass

    def target_humidity(self):
        pass

    def current_operation(self):
        return self.data.get("mode")

    def operation_list(self):
        return self.data.get("support_mode")

    def current_temperature(self):
        curr_temp = self._set_decimal(self.data.get("current_temperature"))
        if not curr_temp:
            return self.target_temperature()
        return curr_temp

    def target_temperature(self):
        return self._set_decimal(self.data.get("temperature"))

    def target_temperature_step(self):
        return 0.5

    def current_fan_mode(self):
        """Return the fan setting."""
        fan_speed = self.data.get("windspeed")
        if fan_speed is None:
            return None
        if fan_speed == "1":
            return "low"
        elif fan_speed == "2":
            return "medium"
        elif fan_speed == "3":
            return "high"
        return fan_speed

    def fan_list(self):
        """Return the list of available fan modes."""
        return ["low", "medium", "high"]

    def current_swing_mode(self):
        """Return the fan setting."""
        return None

    def swing_list(self):
        """Return the list of available swing modes."""
        return None

    def min_temp(self):
        return self._set_decimal(self.data.get("min_temper"))

    def max_temp(self):
        return self._set_decimal(self.data.get("max_temper"))

    def min_humidity(self):
        pass

    def max_humidity(self):
        pass

    def set_temperature(self, temperature):
        """Set new target temperature."""
        if self._divider == 0:
            return
        temp_val = round(float(temperature) * self._divider)
        if self._control_device("temperatureSet", {"value": temp_val}):
            self._update_data("temperature", temp_val)

    def set_humidity(self, humidity):
        """Set new target humidity."""
        raise NotImplementedError()

    def set_fan_mode(self, fan_mode):
        """Set new target fan mode."""
        if self._control_device("windSpeedSet", {"value": fan_mode}):
            fanList = self.fan_list()
            if fan_mode in fanList:
                val = str(fanList.index(fan_mode) + 1)
            else:
                val = fan_mode
            self._update_data("windspeed", val)

    def set_operation_mode(self, operation_mode):
        """Set new target operation mode."""
        if self._control_device("modeSet", {"value": operation_mode}):
            self._update_data("mode", operation_mode)

    def set_swing_mode(self, swing_mode):
        """Set new target swing operation."""
        raise NotImplementedError()

    def support_target_temperature(self):
        if self.data.get("temperature") is not None:
            return True
        else:
            return False

    def support_mode(self):
        if self.data.get("mode") is not None:
            return True
        else:
            return False

    def support_wind_speed(self):
        if self.data.get("windspeed") is not None:
            return True
        else:
            return False

    def support_humidity(self):
        if self.data.get("humidity") is not None:
            return True
        else:
            return False

    def turn_on(self):
        if self._control_device("turnOnOff", {"value": "1"}):
            self._update_data("state", "true")

    def turn_off(self):
        if self._control_device("turnOnOff", {"value": "0"}):
            self._update_data("state", "false")

    def update(self):
        return self._update(use_discovery=True)
