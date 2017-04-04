import unittest

from os.path import abspath, dirname, join
from FlaLD import FlaLD_DC, FlaLD_MODS, FlaLD_QDC

PATH = abspath(dirname(__file__))

class DCTests(unittest.TestCase):
    """
    
    """
    dc_json = FlaLD_DC(join(PATH, 'debug/test_data/DCdebugSmall.xml'))

    def test_dc_SourceResourceCreator(self):
        expected = [[{'name': 'Alexander Hamilton'}],
                    [{'name': 'Karl Cassell'}],
                    [{'name': 'Lewis Carroll'}]]
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['creator'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceContributor(self):
        expected = [[{'name': 'Buckethead'}],
                    [{'name': 'Primus'}],
                    [{'name': 'Thee Oh Sees'}]]
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['contributor'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceDate(self):
        expected = [{'begin': '1974', 'end': '1974'},
                    {'begin': '1972', 'end': '1972'}]
        results = []
        for record in self.dc_json:
            if 'date' in record['sourceResource'].keys():
                results.append(record['sourceResource']['date'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceDescription(self):
        expected = ['1 postcard, postally unused; caption: "Tropical Scenes, South of Florida, U.S.A.", "Copyright 1891 by Geo. Barker."',
                    ['1 postcard, postally used; caption: "View from highway, Royal Palm State Park, Homestead, Florida".',
                     '"The Park Contains 4000 Acres:–960 acres ceded by the State of Florida in 1915, 960 acres donated by Mrs. Henry M. Flagler, and 2080 acres ceded by the State of Florida in 1921. Trails provide access to the beauties and marvels of the tropical forest".'],
                    '1 postcard, postally unused; caption: "Alligator Joe watching the Young Alligators Hatch."']
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['description'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceIdentifier(self):
        expected = [['FI07050832'],
                    ['FI07050842'],
                    ['FI07040407']]
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['identifier'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceLanguage(self):
        expected = [{"name": "English"},
                    {"name": "English"},
                    {"name": "English"}]
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['language'])
        self.assertTrue(all(x in results for x in expected))

#    def test_dc_SourceResourcePublisher(self):
#        """"""
#        pass

    def test_dc_SourceResourceRights(self):
        expected = [['Rights 4A'],
                    ['Rights E3'],
                    ['Rights 1C']]
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['rights'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceSubject(self):
        expected = [[{"name": "Alligators--Florida--Everglades."}],
                    [{"name": "Homestead (Fla.)"}, {"name": "Everglades (Fla.)"}],
                    [{"name": "Tropical forests"}, {"name": "Everglades (Fla.)"}]]
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['subject'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceTitle(self):
        expected = ['Alligator Joe watching the young alligators hatch',
                    'View from highway, Royal Palm State Park, Homestead, Florida',
                    'Tropical Scenes, South of Florida, U.S.A.']
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['title'][0])
        self.assertTrue(all(x in results for x in expected))

#   def test_dc_AggregationDataProvider(self):

    def test_dc_AggregationIsShownAt(self):
        expected = ['http://dpanther.fiu.edu/dpService/dpPurlService/purl/FI07050832/00001',
                    'http://dpanther.fiu.edu/dpService/dpPurlService/purl/FI07050842/00001',
                    'http://dpanther.fiu.edu/dpService/dpPurlService/purl/FI07040407/00001']
        results = []
        for record in self.dc_json:
            results.append(record['isShownAt'])
        self.assertTrue(all(x in results for x in expected))

#   def test_dc_AggregationPreview(self):

#   def test_dc_AggregationProvider(self):


class QDCTests(unittest.TestCase):
    """

    """
    qdc_json = FlaLD_QDC(join(PATH, 'debug/test_data/QDCdebugSmall.xml'))

    def test_qdc_SourceResourceCreator(self):
        expected = [[{'name': 'Gilpin, Vincent'}],
                    [{'name': 'Munroe, Jessie N.'}],
                    [{'name': 'Thurston Moore'}]]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['creator'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceContributor(self):
        expected = [[{'name': 'Buckethead'}],
                    [{'name': 'Primus'}],
                    [{'name': 'Thee Oh Sees'}]]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['contributor'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceDate(self):
        expected = [{'begin': '1933-09-03', 'end': '1933-09-03'},
                    {'begin': '1915-04-26', 'end': '1915-04-26'},
                    {'begin': '1912-01-16', 'end': '1912-01-16'}]
        results = []
        for record in self.qdc_json:
            if 'date' in record['sourceResource'].keys():
                results.append(record['sourceResource']['date'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceDescription(self):
        expected = [['Test 001', 'Test 000'],
                    ['Test 002', 'Test 003']]
        results = []
        for record in self.qdc_json:
            if 'description' in record['sourceResource'].keys():
                results.append(record['sourceResource']['description'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceExtent(self):
        expected = [['1 letter'],
                    ['2 letters'],
                    ['4 letters']]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['extent'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceIdentifier(self):
        expected = ['http://merrick.library.miami.edu/cdm/ref/collection/asm0447/id/31',
                    'http://merrick.library.miami.edu/cdm/ref/collection/asm0447/id/39',
                    'http://merrick.library.miami.edu/cdm/ref/collection/asm0447/id/25']
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['identifier'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceLanguage(self):
        expected = [{"iso_639_3": "eng"},
                    {"iso_639_3": "eng"},
                    {"iso_639_3": "eng"}]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['language'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourcePublisher(self):
        expected = [['IDW'],
                    ['Image Comics'],
                    ['Arista Records']]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['publisher'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceRights(self):
        expected = [{'text': 'Rights 4A', '@id': 'http://rightsstatements.org/page/UND/1.0/'},
                    {'text': 'Rights E3', '@id': 'http://rightsstatements.org/vocab/InC/1.0/'},
                    {'text': 'Rights 1C', '@id': 'http://rightsstatements.org/vocab/InC/1.0/'}]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['rights'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceSubject(self):
        expected = [[{"name": "Gilpin, Vincent"}, {"name": "Munroe, Patty"}, {"name": "Munroe, Ralph, 1851-1933"}, {"name": "Letters"}],
                    [{"name": "Letters"}],
                    [{"name": "Munroe, Patty"}, {"name": "Letters"}]]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['subject'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceSpatial(self):
        expected = [['Coconut Grove (Miami, Fla.)'],
                    ['Death Star'],
                    ['Excelsior (Minn.)']]
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['spatial'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceTitle(self):
        expected = ['Vincent Gilpin letter to Patty Munroe, September 3, 1933',
                    'Jessie N. Munroe letter to Mrs. Gilpin, January 16, 1912',
                    'Jessie N. Munroe letter to Mrs. Gilpin, April 26, 1915']
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['title'][0])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_SourceResourceType(self):
        expected = ['Text',
                    'Rebel Alliance Victory Plans',
                    'Tax return from a VIP']
        results = []
        for record in self.qdc_json:
            results.append(record['sourceResource']['type'][0])
        self.assertTrue(all(x in results for x in expected))

#   def test_qdc_AggregationDataProvider(self):

    def test_qdc_AggregationIsShownAt(self):
        expected = ['http://merrick.library.miami.edu/cdm/ref/collection/asm0447/id/31',
                    'http://merrick.library.miami.edu/cdm/ref/collection/asm0447/id/39',
                    'http://merrick.library.miami.edu/cdm/ref/collection/asm0447/id/25']
        results = []
        for record in self.qdc_json:
            results.append(record['isShownAt'])
        self.assertTrue(all(x in results for x in expected))

    def test_qdc_AggregationPreview(self):
        expected = ['http://merrick.library.miami.edu/utils/getthumbnail/collection/asm0447/id/31',
                    'http://merrick.library.miami.edu/utils/getthumbnail/collection/asm0447/id/39',
                    'http://merrick.library.miami.edu/utils/getthumbnail/collection/asm0447/id/25']
        results = []
        for record in self.qdc_json:
            results.append(record['preview'])
        self.assertTrue(all(x in results for x in expected))

#   def test_qdc_AggregationProvider(self):


class MODSTests(unittest.TestCase):
    """

    """
    mods_json = FlaLD_MODS(join(PATH, 'debug/test_data/MODSdebugSmall.xml'))

#    def test_mods_SourceResourceAlternative(self):

#    def test_mods_SourceResourceCollection(self):

#    def test_mods_SourceResourceCreator(self):

#    def test_mods_SourceResourceContributor(self):

    def test_mods_SourceResourceDate(self):
        expected = [{'begin': '2013-05-27', 'end': '2013-05-27', 'displayDate': '2013-05-27'},
                    {'begin': 'circa 1965-1971', 'end': 'circa 1965-1971', 'displayDate': 'circa 1965-1971'},
                    {'begin': '1935', 'end': '1969', 'displayDate': '1935 - 1969'}]
        results = []
        for record in self.mods_json:
            if 'date' in record['sourceResource'].keys():
                results.append(record['sourceResource']['date'])
        self.assertTrue(all(x in results for x in expected))

    def test_mods_SourceResourceDescription(self):
        expected = [[{'Summary': 'Test 00'}],
                    [{'Summary': 'Test 03'}]]
        results = []
        for record in self.mods_json:
            if 'description' in record['sourceResource'].keys():
                results.append(record['sourceResource']['description'])
        self.assertTrue(all(x in results for x in expected))

#    def test_mods_SourceResourceExtent(self):

#    def test_mods_SourceResourceGenre(self):

    def test_mods_SourceResourceIdentifier(self):
        expected = [{'text': 'FSU_MSS_2015-007_S03_SS02_I003', '@id': 'http://purl.flvc.org/fsu/fd/FSU_MSS_2015-007_S03_SS02_I003'},
                    {'text': 'FSDT107201', '@id': 'http://purl.flvc.org/fcla/dt/107201'},
                    {'text': 'FSUspcn329b', '@id': 'http://purl.flvc.org/fsu/fd/FSUspcn329b'}]
        results = []
        for record in self.mods_json:
            results.append(record['sourceResource']['identifier'])
        self.assertTrue(all(x in results for x in expected))

    def test_mods_SourceResourceLanguage(self):
        expected = [[{"name": "English", "iso_639_3": "eng"}]]
        results = []
        for record in self.mods_json:
            if 'language' in record['sourceResource'].keys():
                results.append(record['sourceResource']['language'])
        self.assertTrue(all(x in results for x in expected))

#    def test_mods_SourceResourcePublisher(self):

    def test_mods_SourceResourceRights(self):
        expected = ['Rights 4A',
                    'Rights AC', # these two actually shouldn't appear... check after pymods==1.0.0 switch
                    'WHAT A BUG!']
        results = []
        for record in self.mods_json:
            results.append(record['sourceResource']['rights'])
        self.assertTrue(all(x in results for x in expected))

#    def test_mods_SourceResourceSubject(self):
#        expected = [[{"name": "Gilpin, Vincent"}, {"name": "Munroe, Patty"}, {"name": "Munroe, Ralph, 1851-1933"}, {"name": "Letters"}],
#                    [{"name": "Letters"}],
#                    [{"name": "Munroe, Patty"}, {"name": "Letters"}]]
#        results = []
#        for record in self.mods_json:
#            results.append(record['sourceResource']['subject'])
#        self.assertTrue(all(x in results for x in expected))

#    def test_mods_SourceResourceSpatial(self):
#        expected = [['Coconut Grove (Miami, Fla.)'],
#                    ['Death Star'],
#                    ['Excelsior (Minn.)']]
#        results = []
#        for record in self.mods_json:
#            results.append(record['sourceResource']['spatial'])
#        self.assertTrue(all(x in results for x in expected))

    def test_mods_SourceResourceTitle(self):
        expected = ['Fraternity fundraiser for injured student',
                    'Student Life Contact Sheet',
                    'Drew Shed: A Shed Alone']
        results = []
        for record in self.mods_json:
            results.append(record['sourceResource']['title'])
        self.assertTrue(all(x in results for x in expected))

    def test_mods_SourceResourceType(self):
        expected = ['still image',
                    'moving image']
        results = []
        for record in self.mods_json:
            results.append(record['sourceResource']['type'])
        self.assertTrue(all(x in results for x in expected))

#    def test_mods_AggregationDataProvider(self):

    def test_mods_AggregationIsShownAt(self):
        expected = ['http://purl.flvc.org/fsu/fd/FSUspcn329b',
                    'http://purl.flvc.org/fcla/dt/107201',
                    'http://purl.flvc.org/fsu/fd/FSU_MSS_2015-007_S03_SS02_I003']
        results = []
        for record in self.mods_json:
            results.append(record['isShownAt'])
        self.assertTrue(all(x in results for x in expected))

    def test_mods_AggregationPreview(self):
        expected = ['http://fsu.digital.flvc.org/islandora/object/fsu:24694/datastream/TN/view',
                    'http://fsu.digital.flvc.org/islandora/object/fsu:9420/datastream/TN/view',
                    'http://fsu.digital.flvc.org/islandora/object/fsu:394576/datastream/TN/view']
        results = []
        for record in self.mods_json:
            results.append(record['preview'])
        self.assertTrue(all(x in results for x in expected))

#    def test_mods_AggregationProvider(self):

if __name__ == '__main__':
    unittest.main()