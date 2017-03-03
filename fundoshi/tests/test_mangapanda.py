import unittest
from fundoshi.sites.mangapanda import Mangapanda
from . import (
    _test_series,
    _test_chapter,
    _test_search_series
)
site = Mangapanda()


class TestMangapandaSearchSeries(unittest.TestCase):

    def test_beelzebub_search(self):
        expected = [
            {
                'name': 'Beelzebub',
                'url': 'http://www.mangapanda.com/beelzebub',
                'site': 'mangapanda',
            },
            {
                'name': 'Beelzebub Side Story',
                'url': 'http://www.mangapanda.com/beelzebub-side-story',
                'site': 'mangapanda',
            },
        ]
        _test_search_series(self, site, 'beelzebub', expected)

    def test_no_result_search(self):
        results = site.search_series('mot con vit xoe ra hai cai canh')
        self.assertListEqual(results, [])


class TestMangapandaSeries(unittest.TestCase):

    def test_completed_series(self):
        url = 'http://www.mangapanda.com/beelzebub'
        expected = {
            'name': 'Beelzebub',
            'tags': ['action', 'comedy', 'demons', 'fantasy', 'school life',
                     'shounen', 'supernatural'],
            'thumb_url': 'http://s4.mangapanda.com/cover/beelzebub/beelzebub-l0.jpg',
            'status': 'ongoing',
            'descriptions': [
                'The story follows the strongest juvenile delinquent, Oga Tatsumi, a first year in Ishiyama High the school for delinquents. One day while sleeping next to a river he sees a man floating down it, he pulls him to shore and the man splits in half revealing a baby boy. This boy is the son of the demon king and he has been chosen as the one to raise it with the baby s demon maid Hilda. The story follows his life with the child and at the delinquent school.[Source: Wiki]',
            ],
            'authors': ['Tamura, Ryuuhei (Story & Art)'],
            'chapters': {
                'last': {
                    'url': 'http://www.mangapanda.com/beelzebub/240',
                    'name': 'Beelzebub 240'
                },
                'first': {
                    'url': 'http://www.mangapanda.com/beelzebub/1',
                    'name': 'Beelzebub 1',
                },
            },
        }
        _test_series(self, site, url, expected)


class TestMangapandaChapter(unittest.TestCase):

    def test_middle_chapter(self):
        url = 'http://www.mangapanda.com/naruto/699'
        expected = {
            'name': 'Naruto 699',
            'prev_chapter_url': 'http://www.mangapanda.com/naruto/698',
            'next_chapter_url': 'http://www.mangapanda.com/naruto/700',
            'series_url': 'http://www.mangapanda.com/naruto',
            'pages': [
                'http://i9.mangapanda.com/naruto/699/naruto-5283045.jpg',
                'http://i1.mangapanda.com/naruto/699/naruto-5283047.jpg',
                'http://i1.mangapanda.com/naruto/699/naruto-5283049.jpg',
                'http://i5.mangapanda.com/naruto/699/naruto-5283051.jpg',
                'http://i9.mangapanda.com/naruto/699/naruto-5283053.jpg',
                'http://i9.mangapanda.com/naruto/699/naruto-5283055.jpg',
                'http://i7.mangapanda.com/naruto/699/naruto-5283057.jpg',
                'http://i5.mangapanda.com/naruto/699/naruto-5283059.jpg',
                'http://i8.mangapanda.com/naruto/699/naruto-5283061.jpg',
                'http://i2.mangapanda.com/naruto/699/naruto-5283063.jpg',
                'http://i10.mangapanda.com/naruto/699/naruto-5283065.jpg',
                'http://i6.mangapanda.com/naruto/699/naruto-5283067.jpg',
                'http://i8.mangapanda.com/naruto/699/naruto-5283069.jpg',
                'http://i10.mangapanda.com/naruto/699/naruto-5283071.jpg',
                'http://i2.mangapanda.com/naruto/699/naruto-5283073.jpg',
                'http://i2.mangapanda.com/naruto/699/naruto-5283075.jpg',
                'http://i10.mangapanda.com/naruto/699/naruto-5283077.jpg',
                'http://i2.mangapanda.com/naruto/699/naruto-5283079.jpg',
                'http://i8.mangapanda.com/naruto/699/naruto-5283081.jpg',
                'http://i2.mangapanda.com/naruto/699/naruto-5283083.jpg',
                'http://i4.mangapanda.com/naruto/699/naruto-5283085.jpg',
            ],
        }
        _test_chapter(self, site, url, expected)

    def test_first_chapter(self):
        """First chapter has no prev_chapter_url"""

        url = 'http://www.mangapanda.com/naruto/1'
        expected = {
            'prev_chapter_url': None,
        }
        _test_chapter(self, site, url, expected)

    def test_last_chapter(self):
        """Last chapter has no next_chapter_url"""

        url = 'http://www.mangapanda.com/naruto/700'
        expected = {
            'next_chapter_url': None,
        }
        _test_chapter(self, site, url, expected)
