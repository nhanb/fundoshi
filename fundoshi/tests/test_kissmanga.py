import unittest
from fundoshi.sites.kissmanga import Kissmanga
from . import _test_series, _test_chapter, _test_search_by_author, \
    _test_search_series
site = Kissmanga()


class TestKissmangaSearchSeries(unittest.TestCase):

    def test_beelzebub_search(self):
        expected = [
            {
                'name': 'Beelzebub',
                'url': 'http://kissmanga.com/Manga/Beelzebub',
                'site': 'kissmanga',
            },
            {
                'name': 'Beelzebub Bangai Hen',
                'url': 'http://kissmanga.com/Manga/Beelzebub-Bangai-Hen',
                'site': 'kissmanga',
            },
        ]
        _test_search_series(self, site, 'beelzebub', expected)

    def test_no_result_search(self):
        results = site.search_series('mot con vit xoe ra hai cai canh')
        self.assertListEqual(results, [])


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
                    'url': 'http://kissmanga.com/Manga/Beelzebub/Babu-240?id=285551',
                    'name': 'Beelzebub Babu 240'
                },
                'first': {
                    'url': 'http://kissmanga.com/Manga/Beelzebub/Babu-000?id=285306',
                    'name': 'Beelzebub Babu 000',
                },
            },
        }
        _test_series(self, site, url, expected)


class TestKissmangaChapter(unittest.TestCase):

    def test_middle_chapter(self):
        url = 'http://kissmanga.com/Manga/Naruto/Naruto-635?id=290868'
        expected = {
            'name': 'Naruto 635',
            'prev_chapter_url': 'http://kissmanga.com/Manga/Naruto/Naruto-634?id=290867',
            'next_chapter_url': 'http://kissmanga.com/Manga/Naruto/Naruto-636?id=290869',
            'series_url': 'http://kissmanga.com/Manga/Naruto',
            'pages': [
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f01.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f02.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f03.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f04.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f05.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f06.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f07.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f08.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f09.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f10.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f11.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f12.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f13.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f14.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f15.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f16.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f17.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f18.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f19.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f20.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f21.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f22.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f23.jpg&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-635%2f24.jpg&imgmax=30000',

            ],
        }
        _test_chapter(self, site, url, expected)

    def test_first_chapter(self):
        """First chapter has no prev_chapter_url"""

        url = 'http://kissmanga.com/Manga/5-Centimeters-per-Second/Vol-1-Ch-1-Read-Online?id=62872'
        expected = {
            'prev_chapter_url': None,
        }
        _test_chapter(self, site, url, expected)

    def test_last_chapter(self):
        """Last chapter has no next_chapter_url"""

        url = 'http://kissmanga.com/Manga/Shigatsu-wa-Kimi-no-Uso/Vol-011-Ch-044---End-?id=223537'
        expected = {
            'next_chapter_url': None,
        }
        _test_chapter(self, site, url, expected)


class TestKissmangaSearchByAuthor(unittest.TestCase):

    def test_normal_author(self):
        _test_search_by_author(self, site, 'ARAKAWA Naoshi', [
            {
                'url': 'http://kissmanga.com/Manga/Sayonara-Football',
                'site': 'kissmanga',
                'name': 'Sayonara Football',
            },
            {
                'url': 'http://kissmanga.com/Manga/Shigatsu-wa-Kimi-no-Uso',
                'site': 'kissmanga',
                'name': 'Shigatsu wa Kimi no Uso',
            },
            {
                'url': 'http://kissmanga.com/Manga/Shigatsu-wa-Kimi-no-Uso-Coda',
                'site': 'kissmanga',
                'name': 'Shigatsu wa Kimi no Uso - Coda',
            },
        ])
