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
If you have HACS, you must add this repository ("https://github.com/ollo69/ha-tuya-custom") to your Custom Repository 
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