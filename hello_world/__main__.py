# Entrypoint file when the package is run with the -m flag from the command line
from . import greeting

greeting.hello_world()
