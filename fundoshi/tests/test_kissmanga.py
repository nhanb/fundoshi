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
        url = 'http://kissmanga.com/Manga/Naruto/Chapter-635?id=250370'
        expected = {
            'name': 'Chapter 635',
            'prev_chapter_url': 'http://kissmanga.com/Manga/Naruto/Chapter-634?id=250369',
            'next_chapter_url': 'http://kissmanga.com/Manga/Naruto/Chapter-635-005?id=250371',
            'series_url': 'http://kissmanga.com/Manga/Naruto',
            'pages': [
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-8SEHoIIaQVI%2fVjHk1Ox10rI%2fAAAAAAAE5zM%2fk6w-Oop32qE%2fs16000%2f0635-001.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-w9LCo3A9llk%2fVjHmARIaIEI%2fAAAAAAAE6SY%2fD772lWMIikE%2fs16000%2f0635-002.jpg&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-exdvDFecM9k%2fVjHTkNV9MOI%2fAAAAAAAEytU%2faE57np7YY7o%2fs16000%2f0635-003.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-ESj9w0JgCzk%2fVjHkPYt_LTI%2fAAAAAAAE5jY%2fJklAgVidgBQ%2fs16000%2f0635-004.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-yuqYlWcdPp0%2fVjHUwKwyPUI%2fAAAAAAAEzMk%2fS88s-s85M8c%2fs16000%2f0635-005.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-rp470RLLK_4%2fVjHk82fRDUI%2fAAAAAAAE52c%2fc9_pTI9iPS0%2fs16000%2f0635-006.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-upHUwBKhG2M%2fVjHmXSzURgI%2fAAAAAAAE6co%2fnQa6Pt5KH08%2fs16000%2f0635-007.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-7srlWao1gKE%2fVjHS8GaFobI%2fAAAAAAAEycw%2fATWCT0c2QU8%2fs16000%2f0635-008.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-EiVTO31IrOo%2fVjHdNfVaKeI%2fAAAAAAAE2po%2fUBjITkVX3a0%2fs16000%2f0635-009.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-pqKA5srtqd8%2fVjHf4YYgXII%2fAAAAAAAE3yY%2fqIC3P6ycYbs%2fs16000%2f0635-010.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-Qj_gkhD8pV8%2fVjHmmk2Ge-I%2fAAAAAAAE6ik%2fP971Qu6q4xo%2fs16000%2f0635-011.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-fQOGUrVBCzA%2fVjHUONMZsZI%2fAAAAAAAEy-I%2f_nOnrFRgihI%2fs16000%2f0635-012.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-uwmNNVct2uo%2fVjHVVCptwyI%2fAAAAAAAEza8%2fpaKUlC0iJIE%2fs16000%2f0635-013.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-2WEA9jnfSFs%2fVjHUsK8TzpI%2fAAAAAAAEzK0%2fXW8kxCZhZUo%2fs16000%2f0635-014.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-_yhOjn3Feyo%2fVjHi59Vhz0I%2fAAAAAAAE5BQ%2f5DQspKUZK-k%2fs16000%2f0635-015.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-k-ZQTBBbVME%2fVjHjtJ_m8KI%2fAAAAAAAE5U4%2f5uISFPL_eTU%2fs16000%2f0635-016.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-HQw7gyObhe4%2fVjHgk53RvyI%2fAAAAAAAE4Dk%2fVJdOAg0xcHM%2fs16000%2f0635-017.png&imgmax=30000',
                'https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-_s77E2rc-M0%2fVjHUJ5gUl5I%2fAAAAAAAEy8c%2fvRmMndDlYhU%2fs16000%2f0635-018.png&imgmax=30000',
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
