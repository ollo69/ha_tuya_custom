# Integration ha_tuya_custom

**Important:** Due to dedicated Tuya API limitation, the refresh interval cannot be faster than 5 minutes
(reduced to 1 minute if you have only 1 device). Do not open issue to ask faster refresh because it is not possible. 
 
This custom component is the copy of the component implemented in Home Assistant but some modifications to the library
used to communicate with Tuya Cloud have been implemented inside it.
The aim is to allow tests on the modified library as quickly as possible and then report the changes in the original 
library used by HA.
Obviously, feedback is important to find an optimal solution

## Installation & configuration
You can install this component in two ways: via HACS or manually.

### Option A: Installing via HACS
If you have HACS, you must add this repository ("https://github.com/ollo69/ha_tuya_custom") to your Custom Repository 
selecting the Configuration Tab in the HACS page.
After this you can go in the Integration Tab and search the "Tuya Custom" component to configure it.

### Option B: Manually installation (custom_component)
1. Clone the git master branch.
1. Unzip/copy the tuya_custom direcotry within the `custom_components` directory of your homeassistant installation.
The `custom_components` directory resides within your homeassistant configuration directory.
Usually, the configuration directory is within your home (`~/.homeassistant/`).
In other words, the configuration directory of homeassistant is where the configuration.yaml file is located.
After a correct installation, your configuration directory should look like the following.
    ```
    └── ...
    └── configuration.yaml
    └── secrects.yaml
    └── custom_components
        └── tuya_custom
            └── __init__.py
            └── climate.py
            └── ...
    ```

    **Note**: if the custom_components directory does not exist, you need to create it.
    
## Component setup    

For the configuration use exactly the same options used to configure the standard Tuya component, however choosing the Tuya Custom component from the list of additions.

**N.B. Before configuring this integration, remove the standard Tuya integration.**

## Integration Options (From UI integration page)

It is possible to change various behaviors through the integration options, some common for integration and others specific to each `light` and `climate` devices. These can be changed at **Tuya Custom** -> **Options** on the Integrations page.

### Common Options

- **Discovery device polling interval** (default=605): define the interval between 2 consecutive calls to the `API discovery method`, which is used to get the status for all registered devices with a single call. If you set interval value too low, Tuya API will return errors, so it is suggested to use the default value until
you know that it is possible to use lower values.

- **Query device polling interval** (default=120): this option is available only if you have devices that can use the `API query method`. 
It defines the interval between 2 consecutive calls to the `API query method`, that is used to get the status for a specific device. 
This method is always used when it is available only one device that can use it. If you set interval value too low, Tuya API will return errors 
so it is suggested to use the default value until you know that is possible to use lower values.

- **Device that will use the query method**: this option is available only if you have devices that can use the `API query method`. 
Because it is not possible to make multiple calls to the `API query method`. If you have more than one device that can use it you can choose which one will use. This will give a better status refresh for this specific device.

- **Device to configure (multi-select list)**: this option is available only if you have a `light` or `climate` device. Selecting a device to 
configure to options page related to the device will be opened. You can also select more than one devices to configure them simultaneously, 
but all selected devices must be of the same type.

### Light Options

- **Force color support**: when checked force `color support` for devices that do not report this feature.

- **Brightness range**: change the `brightness range` used for the device. Possible options are:
    - range 1-255 (default)
    - range 10-1000

- **Min color temperature**: set minimum `color temperature` expressed in `kelvin` accepted by the light.

- **Max color temperature**: set maximum `color temperature` expressed in `kelvin` accepted by the light.

- **Max color temperature reported**: set the maximum `color temperature` value reported by the light.

### Climate Options

- **Temperature unit**: change the `temperature unit` used internally by the devices.

- **Temperature values divider**: `all temperatures` reported by device will be divided by this value.

- **Current Temperature value divider**: `current temperature` reported by device will be divided by this value.

- **Set Temperature value divided**: when checked use the divided temperature value for `set temperature` command.

- **Target Temperature step**: set the temperature step used to set target temperature.

- **Min target temperature**: set the minimum allowed `target temperature` for the entity.

- **Max target temperature**: set the maximum allowed `target temperature` for the entity.

- **Sensor for current temperature**: any HA sensor entity that provide `current temperature`, used when not available from device.

## Device parameters (configuration.yaml)

Configuration of device parameter using `configuration.yaml` is not supported anymore. Use integration options for this.
Please note that option previously set in configuration file will not be loaded anymore and must be configured again from integration page.
