# Tool for automatic request to IAC-Star application

## Requirements
* Google Chrome(used in headless mode to limit the use of resources) 
* Python Module: Selenium

## Algorithm:

**iac_star_data_request.py**: Script to make requests to IAC-Star.


## Configuration file:

**config.json**: json file containing the parameters to personalize the request. 

### Detailed information

**Script parameters:**
* 'nrequest': number of requests to be done.
* 'time': time to be waited between requests. Set to 60 seconds to make sure that simulation will be completed before making another request.

**Simulation parameters:**
The different parameters can be found in the web of IAC-Star application:"http://iac-star.iac.es/cmd/www/form.htm" and a more detailed description in this web:"http://iac-star.iac.es/cmd/www/manual/node1.html".

Default values are set for every parameter except for name, email and institution. It is possible to add multiple values to a single parameter, to a group or to all of them. 

## Author:

**Pedro Hernández Cascales**

## Contact:

Email: pedrohe03@ucm.es

