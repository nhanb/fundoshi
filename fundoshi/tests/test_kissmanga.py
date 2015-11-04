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


class TestKissmangaChapter(unittest.TestCase):

    def test_middle_chapter(self):
        url = 'http://kissmanga.com/Manga/Naruto/Chapter-635?id=247772'
        expected = {
            'name': 'Chapter 635',
            'prev_chapter_url': 'http://kissmanga.com/Manga/Naruto/Chapter-634?id=247771',
            'next_chapter_url': 'http://kissmanga.com/Manga/Naruto/Chapter-635-005?id=247773',
            'series_url': 'http://kissmanga.com/Manga/Naruto',
            'pages': [
                'http://2.bp.blogspot.com/-e1lnFFuMvfw/VjgaM-g0PjI/AAAAAAABB6M/Maf3LoZCnEw/s16000-Ic42/000.png',
                'http://2.bp.blogspot.com/-dqxJbvshngQ/VjgaMpWWwcI/AAAAAAABB6M/_AM06sDxPIk/s16000-Ic42/001.jpg',
                'http://2.bp.blogspot.com/-t02bGWCGUSA/VjgaMor3PlI/AAAAAAABB6M/Ubw0LXd0m1o/s16000-Ic42/002.png',
                'http://2.bp.blogspot.com/-8PhW9BeUugA/VjgaNTDtqjI/AAAAAAABB6M/50ugYnWMXD0/s16000-Ic42/003.png',
                'http://2.bp.blogspot.com/-DEqyG36fStU/VjgaNnQa5FI/AAAAAAABB6M/tiY0d5K0b78/s16000-Ic42/004.png',
                'http://2.bp.blogspot.com/-0MAEhfdsBDg/VjgaVOfXnPI/AAAAAAABB6M/cLRgVt4m6v4/s16000-Ic42/005.png',
                'http://2.bp.blogspot.com/-alyVWkCofGE/VjgaOAdJ3NI/AAAAAAABB6M/532Mx9QTK8w/s16000-Ic42/006.png',
                'http://2.bp.blogspot.com/-NNaJodTFNxo/VjgaOTI2UsI/AAAAAAABB6M/ifj6WPz-KIw/s16000-Ic42/007.png',
                'http://2.bp.blogspot.com/-XnUkCmDshG0/VjgaPIvkvHI/AAAAAAABB6M/kBoYlj_pdj8/s16000-Ic42/008.png',
                'http://2.bp.blogspot.com/-iSjUWOfKbLs/VjgaPTGpEtI/AAAAAAABB6M/x7zo2muoNvA/s16000-Ic42/009.png',
                'http://2.bp.blogspot.com/-Z9PHrQGfghE/VjgaQMQ4UXI/AAAAAAABB6M/YtpI3piO5ns/s16000-Ic42/010.png',
                'http://2.bp.blogspot.com/-QvujNMRdXoo/VjgaRAhoC3I/AAAAAAABB6M/VFr9Ip3Gcuw/s16000-Ic42/011.png',
                'http://2.bp.blogspot.com/-Lu-oRhQzEZQ/VjgaRs4VNQI/AAAAAAABB6M/nyeO9T634xk/s16000-Ic42/012.png',
                'http://2.bp.blogspot.com/-1CMO_HbzEPw/VjgaR2g6SZI/AAAAAAABB6M/vkhzXIFZ8ms/s16000-Ic42/013.png',
                'http://2.bp.blogspot.com/-Wa1QvuBw6Do/VjgaSUDJTQI/AAAAAAABB6M/BiuRmE_Ey9Q/s16000-Ic42/014.png',
                'http://2.bp.blogspot.com/-y_WkcCW5jDA/VjgaSySCFLI/AAAAAAABB6M/8E4_6p6oDKo/s16000-Ic42/015.png',
                'http://2.bp.blogspot.com/-dUIrB7vqdP0/VjgaTf0VXoI/AAAAAAABB6M/dQ6bArmi6G4/s16000-Ic42/016.png',
                'http://2.bp.blogspot.com/-OXHKE4hm9ng/VjgaUAImhzI/AAAAAAABB6M/MtcFpJYYIw4/s16000-Ic42/017.png',
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
