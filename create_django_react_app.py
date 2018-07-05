#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from subprocess import call
from argparse import ArgumentParser
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

def initialize_django_apis(path):
    os.makedirs('apis', exist_ok=True)

def initialize_infra_stuff(path):
    os.makedirs(os.path.join(path, 'infra'), exist_ok=True)

def initialize_webapp(path):
    os.chdir(path)
    # os.makedirs(os.path.join(path, 'webapp'), exist_ok=True)

def initialize_others(path):
    os.makedirs(os.path.join(path, 'resources'), exist_ok=True)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-path", "--path", dest="path", default=os.getcwd(),
                        help="where to initialize the app", metavar="FILE")
    args = parser.parse_args()

    # Create the folder if it does not exists
    logging.debug(f'Making sure {args.path} exists...')
    os.makedirs(args.path, exist_ok=True)

    # Working directory set
    os.chdir(args.path)
    logging.debug(f'Working directory set to {args.path}')
    
    initialize_django_apis(args.path)
    # initialize_infra_stuff(args.path)
    # initialize_webapp(args.path)
    # initialize_others(args.path)
    # call(["create-react-app"])
