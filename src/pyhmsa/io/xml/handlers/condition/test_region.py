#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2013 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import unittest
import logging
import xml.etree.ElementTree as etree
from io import StringIO

# Third party modules.

# Local modules.
from pyhmsa.io.xml.handlers.condition.region import RegionOfInterestXMLHandler
from pyhmsa.core.condition.region import RegionOfInterest

# Globals and constants variables.

class TestRegionOfInterestXMLHandler(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.h = RegionOfInterestXMLHandler()

        self.obj = RegionOfInterest(556, 636)

        source = StringIO('<RegionOfInterest><StartChannel DataType="uint32">556</StartChannel><EndChannel DataType="uint32">636</EndChannel></RegionOfInterest>')
        self.element = etree.parse(source).getroot()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testcan_parse(self):
        self.assertTrue(self.h.can_parse(self.element))

    def testfrom_xml(self):
        obj = self.h.from_xml(self.element)
        self.assertEqual(556, obj.start_channel)
        self.assertEqual(636, obj.end_channel)

        source = StringIO('<RegionOfInterest><EndChannel DataType="uint32">636</EndChannel></RegionOfInterest>')
        element = etree.parse(source).getroot()
        self.assertRaises(ValueError, self.h.from_xml, element)

        source = StringIO('<RegionOfInterest><StartChannel DataType="uint32">556</StartChannel></RegionOfInterest>')
        element = etree.parse(source).getroot()
        self.assertRaises(ValueError, self.h.from_xml, element)

    def testcan_convert(self):
        self.assertTrue(self.h.can_convert(self.obj))

    def testto_xml(self):
        element = self.h.to_xml(self.obj)
        self.assertEqual('RegionOfInterest', element.tag)
        self.assertEqual('556', element.find('StartChannel').text)
        self.assertEqual('636', element.find('EndChannel').text)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
