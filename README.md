# SetupScripts

Some setup scripts for different needs. Enjoy.

## Table of Contents

1. [GRC](#GRC-Setup)
2. [Python](#Python-Template-Creator)

## GRC Setup
### setup-grc.sh

This module specifically setups the `grc` command for use with the `tail` command.
It will add customization and coloring to any future tail commands for easier viewing.

Usage:
	Execute from command line using sudo.

	$ sudo /bin/bash setup-grc.sh


## Python Template Creator
### setup-python.py

This module sets up python files given command line arguments.
Designed to help user obey PEP 8 standards.

Usage:
    Executed from command line.

        $ python3 make-python.py <args>

Arguments:
    name: Required argument to set the name of the output file.
    -c <int>: Optional argument to generate n template classes.
    -f <int>: Optional argument to generate m template functions.
    -m: Optional boolean argument to remove default main function
