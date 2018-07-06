#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from subprocess import call
from argparse import ArgumentParser
import logging
import io

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')


def _replace_template(template_content, website_name, website_url):
    return template_content.replace('$TEMPLATENAME', website_name)\
                           .replace('$TEMPLATEURL', website_url)


def initialize_django_apis():
    os.makedirs('apis', exist_ok=True)

def initialize_infra_stuff(current_path, name, url):
    if name is None or url is None:
        raise TypeError()
    os.makedirs('infra', exist_ok=True)
    
    templates_folder = os.path.join(current_path, 'templates', 'infra')
    for filename in os.listdir(templates_folder):
        logging.debug(f'Copying template {filename}...')

        # Read the template file
        with io.open(os.path.join(templates_folder, filename), 'r') as template:
            # Create the new config file
            config_filename = _replace_template(filename, name, url)
            with io.open(os.path.join('infra', config_filename), 'w') as config:
                for line in template.readlines():
                    # Replace the variables & Write to the new config file
                    config.write(_replace_template(line, name, url))


def initialize_webapp():
    call(['create-react-app', 'webapp'])
    # os.makedirs(os.path.join(path, 'webapp'), exist_ok=True)

def initialize_others():
    os.makedirs('resources', exist_ok=True)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-path', '--path', dest='path', default=os.getcwd(),
                        help='where to initialize the app', metavar='FILE')
    parser.add_argument('-name', '--name', dest='name',
                        help='Name of the App', metavar='string')
    parser.add_argument('-url', '--url', dest='url',
                        help='Domain of the App (base url without www.)', metavar='string')
    args = parser.parse_args()

    # Create the folder if it does not exists
    logging.debug(f'Making sure {args.path} exists...')
    os.makedirs(args.path, exist_ok=True)

    # Working directory set
    original_path = os.getcwd()
    os.chdir(args.path)
    logging.debug(f'Working directory set to {args.path}')
    
    initialize_django_apis()
    initialize_infra_stuff(original_path, args.name, args.url)
    # initialize_webapp()
    # initialize_others()
    os.chdir(original_path)
