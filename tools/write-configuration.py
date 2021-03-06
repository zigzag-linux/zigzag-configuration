#!/usr/bin/python3

import os
import sys
import argparse
import subprocess

CONFIG_ROOT = '/usr/share/zigzag/ansible'

parser = argparse.ArgumentParser(description='Apply default configuration of Zigzag Linux to host system')
parser.add_argument('preset', default='root', type=str, nargs='?', help='name of the configuration preset')
parser.add_argument('--force', const=True, action='store_const', default=False,
                    help='change actual files (you have been warned)')

args = parser.parse_args()

if not args.force:
    sep = '\n{}\n'.format('*' * 65)
    sys.exit(sep +
            'This script is used to bootstrap configuration of Zigzag Linux.\n'
            'It will override *everything* to default values. \n'
            'Check --help for a way to proceed.\n'
            + sep)

if os.geteuid() != 0:
    exit("You need to have root privileges to apply the configuration.")

preset_path = '{}/{}.yml'.format(CONFIG_ROOT, args.preset)
subprocess.run(['ansible-playbook', '-i', 'localhost,', '-c', 'local', preset_path], check=True)
