#!/usr/bin/env python
"""
================================================================================
:mod:`elementid` -- XML handler for element id condition
================================================================================

.. module:: elementid
   :synopsis: XML handler for element id condition

.. inheritance-diagram:: elementid

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2013 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import xml.etree.ElementTree as etree

# Third party modules.

# Local modules.
from pyhmsa.spec.condition.elementid import ElementID, ElementIDXray
from pyhmsa.io.xmlhandler import _XMLHandler

# Globals and constants variables.

class ElementIDXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'ElementID'

    def from_xml(self, element):
        return self._parse_parameter(element, ElementID)

    def can_convert(self, obj):
        return isinstance(obj, ElementID)

    def to_xml(self, obj):
        element = self._convert_parameter(obj, etree.Element('ElementID'))
        element.find('Element').set('Symbol', obj.symbol) # manually add symbol
        return element

class ElementIDXrayXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'ElementID' and element.get('Class') == 'X-ray'

    def from_xml(self, element):
        return self._parse_parameter(element, ElementIDXray)

    def can_convert(self, obj):
        return isinstance(obj, ElementIDXray)

    def to_xml(self, obj):
        element = etree.Element('ElementID', {'Class': 'X-ray'})
        element = self._convert_parameter(obj, element)
        element.find('Element').set('Symbol', obj.symbol) # manually add symbol
        return element
