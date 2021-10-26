# ScriptGUIfier
## Description
Have nice a Graphical User Interface for your scripts.
To do so, you just need to fill a configuration file describing your scripts (options, location, etc) and voilà, you have a GUI to use your script.

## How to use
### Requirements
You need to have python 3 installed (no other dependy normally).

### Launch the application
You just need to execute the __main.py__ script, by default it try to search the configuration file at __./test_data/SimpleConf.json__ but you can choose an other name and location with the option __-c__ or __--config__.
Examples:
- `./main.py --config ~/my_config_file` 
- `python3 ./src/main.py -c ../my_conf_file.json`

## The configuration file
The configuration fis a simple json file. The top object has 2 attributes:
- __app_name__: (String) The name that will appear on the window
- __categories__: (Array) An array of __Category__.

A __Category__ is the representation of a page, and on this page. It allows to group script by type. A __Category__ has the followings attributes:
- __name__: (String) It will be display at the top of the page. 
- __scripts__: (Array) an array of __Script__.

A __Script__ contains everything needed to be able to create the components to use a script with all its options. It has 3 attributes:
- __name__: (String) The displayed name on the application.
- __script__: (String) The location of the script.
- __options__: (Array) An array of __Option__.

An __Option__ describes the arguments your program takes. It has a several attributes but some are optionals:
- __name__: (Optional String) The text shown on the GUI, if not set it has the takes the value of the __literal__.
- __literal__: (String) it is the option name used on the command line it can be empty. It often begins by __-__ or __--__.
- __description__: (Optional String): Describe what the option is, not use for the moment.
- __type__:
- __default_value__:
- __default_value_from_env__:
- __default_value_from_script__:
- __values__: 

## TODO
See: https://github.com/Baduit/ScriptGUIfier/projects/2

