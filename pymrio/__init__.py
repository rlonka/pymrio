""" 
Pymrio - A python module for automating input output calculations and generating reports
========================================================================================

The classes and tools in this module should work with any symetric IO system.

The main class of the module (IOSystem) has attributes .A, .L, ... 
corresponding to a standard IO classification. 
Data can be assigned directly to the attributes or by calling the 
parsing or load functions.

Data storage
------------
Txt files together with a ini file are used for storing data. In addition, 
the IOSystem with all data can also be pickled (binary). 
Conversion to hdf5 and mat should be implemented...

Misc
----

Standard abbreviation for that module: mr
Dependencies:

- numpy
- scipy
- pandas
- matplotlib
- docutils (only for IOSystem.report* if format is html and tex - not 
            imported otherwise)

:Authors: Konstantin Stadler 

:license: BSD 2-Clause License

"""

import sys


# check for correct python version number
if sys.version_info.major < 3: 
    logging.warn('This package requires Python 3.0 or later.')

# version
__version__ = '0.2.1'

# import public functionality 

from pymrio.core.mriosystem import IOSystem
from pymrio.core.mriosystem import Extension

from pymrio.core.fileio import load_all
from pymrio.core.fileio import load
from pymrio.core.fileio import load_test

from pymrio.tools.parser import parse_exio_ext
from pymrio.tools.parser import parse_exiobase22

from pymrio.tools.util import concate_extension
from pymrio.tools.util import build_agg_vec
from pymrio.tools.util import build_agg_matrix

from pymrio.tools.iomath import calc_x
from pymrio.tools.iomath import calc_x_from_L
from pymrio.tools.iomath import calc_Z
from pymrio.tools.iomath import calc_A
from pymrio.tools.iomath import calc_L
from pymrio.tools.iomath import calc_S
from pymrio.tools.iomath import calc_F
from pymrio.tools.iomath import calc_M
from pymrio.tools.iomath import calc_e
from pymrio.tools.iomath import calc_accounts


#__all__ = ['spam', 'grok']
