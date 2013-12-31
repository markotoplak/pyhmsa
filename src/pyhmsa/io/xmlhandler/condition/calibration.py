"""
================================================================================
:mod:`calibration` -- XML handler for calibrations
================================================================================

.. module:: calibration
   :synopsis: XML handler for calibrations

.. inheritance-diagram:: calibration

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2013 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.

# Third party modules.

# Local modules.
from pyhmsa.spec.condition.calibration import \
    (CalibrationConstant, CalibrationLinear,
     CalibrationPolynomial, CalibrationExplicit)
from pyhmsa.io.xmlhandler import _XMLHandler

# Globals and constants variables.

class CalibrationConstantXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'Calibration' and element.get('Class') == 'Constant'

    def parse(self, element):
        return self._parse_parameter(element, CalibrationConstant)

    def can_convert(self, obj):
        return isinstance(obj, CalibrationConstant)

    def convert(self, obj):
        return self._convert_parameter(obj, 'Calibration', {'Class': 'Constant'})

class CalibrationLinearXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'Calibration' and element.get('Class') == 'Linear'

    def parse(self, element):
        return self._parse_parameter(element, CalibrationLinear)

    def can_convert(self, obj):
        return isinstance(obj, CalibrationLinear)

    def convert(self, obj):
        return self._convert_parameter(obj, 'Calibration', {'Class': 'Linear'})

class CalibrationPolynomialXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'Calibration' and element.get('Class') == 'Polynomial'

    def parse(self, element):
        return self._parse_parameter(element, CalibrationPolynomial)

    def can_convert(self, obj):
        return isinstance(obj, CalibrationPolynomial)

    def convert(self, obj):
        return self._convert_parameter(obj, 'Calibration', {'Class': 'Polynomial'})

class CalibrationExplicitXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'Calibration' and element.get('Class') == 'Explicit'

    def parse(self, element):
        return self._parse_parameter(element, CalibrationExplicit)

    def can_convert(self, obj):
        return isinstance(obj, CalibrationExplicit)

    def convert(self, obj):
        return self._convert_parameter(obj, 'Calibration', {'Class': 'Explicit'})
