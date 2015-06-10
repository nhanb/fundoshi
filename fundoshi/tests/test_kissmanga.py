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
        url = 'http://kissmanga.com/Manga/Naruto/Naruto-635--A-new-wind?id=168179'
        expected = {
            'name': '635: A new wind',
            'prev_chapter_url': 'http://kissmanga.com/Manga/Naruto/Naruto-634--A-new-three-way-deadlock?id=167410',
            'next_chapter_url': 'http://kissmanga.com/Manga/Naruto/Naruto-636--The-current-Obito?id=168656',
            'series_url': 'http://kissmanga.com/Manga/Naruto',
            'pages': [
                'http://2.bp.blogspot.com/-oo5dvvZ4SYk/UcGPrS3gfBI/AAAAAAAAUak/qx8IXNbDsXE/001.png?imgmax=10000',
                'http://2.bp.blogspot.com/-VNmt-Gh1wWM/UcGPs992wJI/AAAAAAAAUas/GRWwt7reHwA/002.jpg?imgmax=10000',
                'http://2.bp.blogspot.com/-N858y2E4Z8Q/UcGPuMTL2oI/AAAAAAAAUa0/jSYWClX1cfA/003.jpg?imgmax=10000',
                'http://2.bp.blogspot.com/-NKlK9yDloqY/UcGPvcNg5WI/AAAAAAAAUa8/ozRFchEZbUs/004.jpg?imgmax=10000',
                'http://2.bp.blogspot.com/-BIune6hnblY/UcGPwWfGiyI/AAAAAAAAUbE/1OXh0OZS4dA/005.jpg?imgmax=10000',
                'http://2.bp.blogspot.com/-ui1CR8aiOuc/UcGP0CAfCuI/AAAAAAAAUbM/kzTRcMngR58/006.png?imgmax=10000',
                'http://2.bp.blogspot.com/-f5TUcCZrdmI/UcGP1BMz7JI/AAAAAAAAUbU/axhz-IFrBLg/007.png?imgmax=10000',
                'http://2.bp.blogspot.com/-no_1XqXEve0/UcGP1yKoerI/AAAAAAAAUbc/YXYIKytC_-E/008.png?imgmax=10000',
                'http://2.bp.blogspot.com/-G1mwgk5d1yg/UcGP2wIn4qI/AAAAAAAAUbk/uki7lPES6tw/009.png?imgmax=10000',
                'http://2.bp.blogspot.com/-2iaDojP-sjg/UcGP3ndaUqI/AAAAAAAAUbs/ILWIo-rAwhc/010.png?imgmax=10000',
                'http://2.bp.blogspot.com/-PFh_dEbfBfM/UcGP4wi91GI/AAAAAAAAUb0/UTi7Ps2oA0g/011.png?imgmax=10000',
                'http://2.bp.blogspot.com/-BH1VDi8Piks/UcGP5oCVtWI/AAAAAAAAUb8/GL4_t4GC0Nw/012.png?imgmax=10000',
                'http://2.bp.blogspot.com/-CVSRsfnMUpo/UcGP6natY-I/AAAAAAAAUcE/za7P0PH3wbw/013.png?imgmax=10000',
                'http://2.bp.blogspot.com/-gsLOD3dKR8c/UcGP7gX-_OI/AAAAAAAAUcM/SCnAhTUgWNs/014.png?imgmax=10000',
                'http://2.bp.blogspot.com/-TfpPYQWMYrw/UcGP8i2w9JI/AAAAAAAAUcU/CIaW90wOGrA/015.png?imgmax=10000',
                'http://2.bp.blogspot.com/-tiQTqNA4yOw/UcGP9dIovBI/AAAAAAAAUcc/hfF-n5hdjss/016.png?imgmax=10000',
                'http://2.bp.blogspot.com/-G9PrTWh8WfA/UcGP-cceW-I/AAAAAAAAUck/DAFbcJNanAo/017.png?imgmax=10000',
                'http://2.bp.blogspot.com/-CEsUmtukRBU/UcGP_tPAqfI/AAAAAAAAUcs/v0bxTtEDYH4/018.png?imgmax=10000',
                'http://2.bp.blogspot.com/-F6zT6kQKYZc/UcGQAxKgETI/AAAAAAAAUc0/6cZZ_S30uJI/019.png?imgmax=10000',
                'http://2.bp.blogspot.com/-ICA7eGUO4sg/UcGQCQ3XEPI/AAAAAAAAUc8/qqp5DcRj5G8/020.png?imgmax=10000',
                'http://2.bp.blogspot.com/-DPGmrkYpSc0/UcGQEnBKgSI/AAAAAAAAUdE/smID9qx16G0/021.png?imgmax=10000',
                'http://2.bp.blogspot.com/-PRqMX1IIbyA/UcGQHUFSK_I/AAAAAAAAUdM/QLUSdBtlJmQ/022.jpg?imgmax=10000',
                'http://2.bp.blogspot.com/-JLEkemXwZ-Q/UcGQIgYbqLI/AAAAAAAAUdU/CBgY0s8phIQ/023.jpg?imgmax=10000',
                'http://2.bp.blogspot.com/-oeMppzdO0AA/UcGQJspVbbI/AAAAAAAAUdc/5WA7MlQvGng/024.jpg?imgmax=10000',
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
