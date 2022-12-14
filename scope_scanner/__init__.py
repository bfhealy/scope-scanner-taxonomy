"""
This module contains the Scope scanner taxonomy.
"""

__version__ = '1.1.0'
__all__ = ["__version__", "taxonomy", "name", "provenance"]

import os
from os.path import join
import yaml
from yaml import FullLoader

tax_path = join(os.path.dirname(__file__), 'scanner.yaml')

with open(tax_path) as taxonomy_yaml:
    taxonomy = yaml.load(taxonomy_yaml, Loader=yaml.FullLoader)

name = 'SCoPe Scanner Taxonomy'
provenance = 'https://github.com/bfhealy/scope-scanner-taxonomy'
