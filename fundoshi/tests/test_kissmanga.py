import unittest
from fundoshi.sites.kissmanga import Kissmanga
from . import _test_series
site = Kissmanga()


class TestKissmangaSeries(unittest.TestCase):

    def test_completed_series(self):
        url = 'http://kissmanga.com/Manga/Beelzebub'
        expected = {
            'name': 'Beelzebub',
            'tags': ['action', 'comedy', 'fantasy', 'manga', 'school life',
                     'shounen', 'supernatural'],
            'thumb_url': 'http://kissmanga.com/Uploads/Etc/8-17-2011/75210229ef3c651a3.jpg',
            'status': 'completed',
            'description': [
                'The story follows the "strongest juvenile delinquent" as he watches over '
                "the devil king's son (and future devil king) with the fate of the world "
                'hanging in the balance.'
            ],
            'authors': ['Tamura Ryuuhei'],
            'chapters': {
                'last': {
                    'url': 'http://kissmanga.com/Manga/Beelzebub/Ch-240--Last-Babu'
                           '--Good-Babu--Ishiyama-High--End-?id=188430',
                    'name': 'Beelzebub 240: Last Babu, Good Babu, Ishiyama High [End]'
                },
                'first': {
                    'url': 'http://kissmanga.com/Manga/Beelzebub/Vol-1-Ch-01-Read-Online?id=407',
                    'name': 'Beelzebub 001 Read Online',
                },
            },
        }
        _test_series(self, site, url, expected)
