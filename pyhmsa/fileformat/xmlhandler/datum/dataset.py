from collections import OrderedDict

from pyhmsa.fileformat.xmlhandler.datum.datum import _DatumXMLHandler
from pyhmsa.spec.datum.dataset import Dataset


class DatasetXMLHandler(_DatumXMLHandler):

    def can_parse(self, element):
        return element.tag == 'Dataset'

    def _parse_data_offset(self, element):
        try:
            return super()._parse_data_offset(element)
        except ValueError:
            # DataOffset may be omitted for the first element
            return 8

    def _parse_int(self, element):
        return int(element.text)

    def _parse_datum_dimensions(self, element):
        dimensions = OrderedDict()

        for subelement in element.findall('Dimensions/'):
            value = self._parse_int(subelement)
            dimensions[subelement.tag] = value

        return dimensions

    def _parse_numerical_attribute(self, element, attrib=None):
        if element.tag in {"DataOffset", "DataLength"}:
            # we know these have to be int from the spec
            return int(element.text)
        else:
            return super()._parse_numerical_attribute(element, attrib)

    def parse(self, element):
        dtype = self._parse_datum_type(element)

        dimensions = self._parse_datum_dimensions(element)
        shape = list(dimensions.values())

        buffer = self._parse_binary(element)

        ds = Dataset(shape, dtype, buffer, order="F")
        ds.dimensions = dimensions
        return ds

    def can_convert(self, obj):
        return False
