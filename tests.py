import unittest

from os.path import abspath, dirname, join
from FlaLD import FlaLD_DC, FlaLD_MODS, FlaLD_QDC

PATH = abspath(dirname(__file__))

class DCTests(unittest.TestCase):
    """
    
    """
    dc_json = FlaLD_DC(join(PATH, 'debug/test_data/DCdebugSmall.xml'))

    def test_dc_SourceResourceDescription(self):
        expected = ['1 postcard, postally unused; caption: "Tropical Scenes, South of Florida, U.S.A.", "Copyright 1891 by Geo. Barker."',
                    ['1 postcard, postally used; caption: "View from highway, Royal Palm State Park, Homestead, Florida".',
                     '"The Park Contains 4000 Acres:–960 acres ceded by the State of Florida in 1915, 960 acres donated by Mrs. Henry M. Flagler, and 2080 acres ceded by the State of Florida in 1921. Trails provide access to the beauties and marvels of the tropical forest".'],
                    '1 postcard, postally unused; caption: "Alligator Joe watching the Young Alligators Hatch."']
        results = []
        for record in self.dc_json:
            results.append(record['sourceResource']['description'])
        self.assertTrue(all(x in results for x in expected))

    def test_dc_SourceResourceIidentifier(self):
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

    def test_dc_SourceResourceRights(self):
        expected = [['Please contact the owning institution for licensing and permissions. It is the users responsibility to ensure use does not violate any third party rights.'],
                    ['Please contact the owning institution for licensing and permissions. It is the users responsibility to ensure use does not violate any third party rights.'],
                    ['Please contact the owning institution for licensing and permissions. It is the users responsibility to ensure use does not violate any third party rights.']]
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


if __name__ == '__main__':
    unittest.main()