# Configuration Generator

## Prepare

`pip install jinja2`

## Usage
`python config_generator.py [options] <vendor>/<type>/<device> [data.json]`

###TODO:
- [x ] cmd format <vendor>/<type>/<device> to ./templates/vendor/type/device.j2
- [x] defaults parameters
- [x] scan defaults.json in templates
- [ ] scan <filename>.json for <filename>.j2
- [x] add option **-t** **--template** to set templates folder
- [x] add option **-o** **--output** to set output folder

> _[Jinja2](https://github.com/pallets/jinja)_
>> _Original idea: [Configuration Generator with Python and Jinja2](https://codingnetworker.com/2015/09/configuration-generator-with-python-and-jinja2/), [GitHub](https://github.com/hoelsner/python-script-examples/tree/master/config-generator-with-python-and-jinja2)_