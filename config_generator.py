import jinja2
import json
import os
from optparse import OptionParser

__version__ = "0.1"
__copyright__ = "Vladimir Kushnir aka Kvantum i(c)2016"


def get_options(arguments=None):
    """Load commandline parameters"""
    cpath = os.path.dirname(os.path.realpath(__file__))
    parser = OptionParser(usage="%prog [options] <template.j2> <params.json>",
                          version="%prog " + __version__)
    parser.set_defaults(
        templates=os.path.join(cpath, 'templates'),
        json=os.path.join(cpath, 'json'),
        output=os.path.join(cpath, '_output')
    )
    parser.add_option('-t', '--templates', dest='templates', help="Path to templates folder")
    parser.add_option('-j', '--json', dest='json', help="Path to json folder")
    parser.add_option('-o', '--output', dest='output', help="Path to output folder")

    (opt, args) = parser.parse_args(arguments)

    if len(args) < 1:
        parser.error("You must specify template!")
        if len(args) < 2:
            parser.error("You must specify parameters!")

    if not os.path.exists(opt.output):
        os.mkdir(opt.output)

    template = os.path.abspath(os.path.join(opt.templates, args[0]))
    if not os.path.isfile(template):
        template += '.j2'
        if not os.path.isfile(template):
            parser.error("Can't find template '"+template+"'!")
    opt.template = template

    parameters = args[1]
    if os.path.splitext(parameters.lower())[1] != 'json':
        parameters += '.json'
    if not os.path.isfile(parameters):
        parameters = os.path.abspath(os.path.join(opt.json, parameters))
        if not os.path.isfile(parameters):
            parser.error("Can't find parameters '" + parameters + "'!")
    opt.parameters = parameters

    return opt


def get_parameters(opt):
    """Load json parameters"""
    defaults = []

    default_template_folder = os.path.relpath(os.path.dirname(opt.template), opt.templates)
    while default_template_folder:
        default = os.path.join(opt.templates, default_template_folder, 'defaults.json')
        if os.path.isfile(default):
            defaults.append(default)
        default_template_folder = os.path.dirname(default_template_folder)

    default = os.path.join(opt.templates, 'defaults.json')
    if os.path.isfile(default):
        defaults.append(default)
    defaults.reverse()

    default = os.path.splitext(opt.template)[0] + '.json'
    if os.path.isfile(default):
        defaults.append(default)

    jdefaults = {}
    for default in defaults:
        jdefaults.update(json.load(open(default)))
    jparameters = json.load(open(opt.parameters))
    return jparameters, jdefaults


def main():
    """Main procedure"""
    opt = get_options()
    config_parameters, config_defauts = get_parameters(opt)

    print("Create Jinja2 environment...")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=os.path.dirname(opt.template)),
                             trim_blocks=True,
                             lstrip_blocks=True)
    template = env.get_template(os.path.basename(opt.template))

    for config_parameter in config_parameters:
        full_config_parameter = {}
        full_config_parameter.update(config_defauts)
        full_config_parameter.update(config_parameter)
        result = template.render(full_config_parameter)
        f = open(os.path.join(opt.output, config_parameter['hostname'] + ".config"), "w")
        f.write(result)
        f.close()
        print("Configuration '%s' created..." % (config_parameter['hostname'] + ".config"))
    print("DONE")

    print ('Finish!')


if __name__ == "__main__":
    main()
