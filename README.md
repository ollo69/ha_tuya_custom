# Integration ha_tuya_custom
 
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
    
### Component setup    

For the configuration use exactly the same options used to configure the standard Tuya component, however choosing the Tuya Custom component from the list of additions.

**N.B. Before configuring this integration, remove the standard Tuya integration.**

### Device parameters (configuration.yaml)

To provide device information that in some case are not correctly provided by the cloud, you can use 
configuration.yaml file. Following example of supported values:

- For light device:

```
tuya_custom:
  devices_config:
    - device_name: <Friendly Name of your device in HA> # this is mandatory with at least one of the other keys
      support_color: true # true or false, force color support for device
```

- For climate device:

```
tuya_custom:
  devices_config:
    - device_name: <Friendly Name of your device in HA> # this is mandatory with at least one of the other keys
      unit_of_measurement: "C" # "F" or "C", not set to use value provided from cloud
      temp_divider: 1 # any positive number, all temperature values will be divided by this value
      curr_temp_divider: 1  # any positive number, only current temperature values will be divided by this value
      ext_temp_sensor: sensor.temp # a sensor that provide ambient temp used when not provided by device
```

You can set configuration for multiple devices, adding one list that start with `- device_name:` for every device
