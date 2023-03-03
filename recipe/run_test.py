#!/usr/bin/env python

import ipyparallel
import ipyparallel.apps
import ipyparallel.client
import ipyparallel.controller
import ipyparallel.engine
import ipyparallel.serialize

import sys
from subprocess import check_output, STDOUT

def sh(cmd):
    out = check_output(cmd, stderr=STDOUT)
    return out.decode('utf8', 'replace')

# verify extension enabling
nbextensions = sh([sys.executable, '-m', 'jupyter', 'nbextension', 'list'])
print(nbextensions)
assert 'ipyparallel' in nbextensions

serverextensions = sh([sys.executable, '-m', 'jupyter', 'serverextension', 'list'])
print(serverextensions)
assert 'ipyparallel' in serverextensions
