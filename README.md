# Configuration Generator

## Prepare

#### Install [Python](https://www.python.org/)

#### Install [Jinja2](http://jinja.pocoo.org/)

`pip install jinja2`

## Usage

`python config_generator.py [options] <folder1>/<folder2>/<template> [data.json]`

### Folders
```
root/
   ./config_generator.py
   ./templates/
             ./folder1/
             ./defaults.json
             ./device1.j2
                    ./folder2/
                    ./defaults.json
                    ./device2.j2
                    ./device2.json
   ./json/
        ./data1.json
        ./data2.json
```

###TODO:

- [x] cmd format <vendor>/<type>/<device> to ./templates/vendor/type/device.j2
- [x] defaults parameters
- [x] scan defaults.json in templates
- [ ] scan <filename>.json for <filename>.j2
- [x] add option **-t** **--template** to set templates folder
- [x] add option **-o** **--output** to set output folder

> _Original idea: [Configuration Generator with Python and Jinja2](https://codingnetworker.com/2015/09/configuration-generator-with-python-and-jinja2/), [GitHub](https://github.com/hoelsner/python-script-examples/tree/master/config-generator-with-python-and-jinja2)_
