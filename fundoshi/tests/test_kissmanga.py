from vcr_unittest import VCRTestCase
from fundoshi.sites.kissmanga import Kissmanga
from . import _test_series, _test_chapter, _test_search_by_author, \
     _test_search_series
site = Kissmanga()


class TestKissmangaSearchSeries(VCRTestCase):

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


class TestKissmangaSeries(VCRTestCase):

    def test_completed_series(self):
        url = 'http://kissmanga.com/Manga/Beelzebub'
        expected = {
            'name': 'Beelzebub',
            'tags': ['action', 'comedy', 'fantasy', 'manga', 'school life',
                     'shounen', 'supernatural'],
            'thumb_url': 'http://kissmanga.com/Uploads/Etc/8-17-2011/75210229ef3c651a3.jpg',
            'status': 'completed',
            'descriptions': [
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


class TestKissmangaChapter(VCRTestCase):

    def test_middle_chapter(self):
        url = 'http://kissmanga.com/Manga/Naruto/Chapter-635?id=377785'
        expected = {
            'name': 'Chapter 635',
            'prev_chapter_url': 'http://kissmanga.com/Manga/Naruto/Chapter-634?id=377784',
            'next_chapter_url': 'http://kissmanga.com/Manga/Naruto/Chapter-636?id=377786',
            'series_url': 'http://kissmanga.com/Manga/Naruto',
            'pages': [
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-K6wypMEsgdM%2fWCWgfPiziCI%2fAAAAAAACl0Y%2fiBo-uiCzb9EoUeob1dgm3jg86qMC7hS3ACHM%2fs16000%2f0635-001.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-5xTUdLluOr4%2fWCWghIUftSI%2fAAAAAAACl0Y%2fPDenl-f6j9cdlJ1UMwqB33Ju2Nvehu4ZwCHM%2fs16000%2f0635-002.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-fzUSepzKxyg%2fWCWgjpSrDGI%2fAAAAAAACl0Q%2fIcP5nxH_35UDccpgTeit3S4WPqSDNgWjwCHM%2fs16000%2f0635-003.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-p79bG5Ol8B4%2fWCWgnExdAbI%2fAAAAAAACl0Q%2ff5y649rPg00Tof93DFgr6QE3FIQhrw3bQCHM%2fs16000%2f0635-004.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-Ttg4VU-85O4%2fWCWgno8eixI%2fAAAAAAACl0Q%2fNsKe5G8atSQqfrIyZgVk-Z0BYkJqN908ACHM%2fs16000%2f0635-005.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-mbH-Kwtmmd8%2fWCWgsSKl7QI%2fAAAAAAACl0Q%2fOctAa92MlwMUWDUevVvvT7KyIV-9QF08QCHM%2fs16000%2f0635-006.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-E4tZ74I0btA%2fWCWguQWgrwI%2fAAAAAAACl0Q%2fRnWNYZv4Rtsxc1fmD9aRB-S8lcdkRcpqACHM%2fs16000%2f0635-007.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-3uInbNcNqYE%2fWCWgwFrsVDI%2fAAAAAAACl0Q%2fEgMKNXlfBLQe8nbZzOT-D60xdHB28hYjACHM%2fs16000%2f0635-008.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f--bn-IRIgbEo%2fWCWg1EeooOI%2fAAAAAAACl0Q%2fQSkIw8GNVegnCZHNpL9-dh4ZmmGBY09AgCHM%2fs16000%2f0635-009.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-usSi_u6_3Zk%2fWCWg1w7acLI%2fAAAAAAACl0Q%2fRMx1TETpwZI_hV2opwQSqWaeYxooGFV4gCHM%2fs16000%2f0635-010.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-lyiG1db7Uro%2fWCWg672LeMI%2fAAAAAAACl0Q%2f0MLkV0mRb4IJtOdm7OBSKqg43hkmlJ9sQCHM%2fs16000%2f0635-011.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-oSlz4CZzWGE%2fWCWg8BjVd1I%2fAAAAAAACl0Q%2fFftWXfxZQNszcM8eRUyhL00XkOI45AuUwCHM%2fs16000%2f0635-012.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-f_NLGWwKqc0%2fWCWhABQ5yJI%2fAAAAAAACl0Q%2fm5jkPwsg8ec4gFZCJVio2WNJ8_3o4l1qwCHM%2fs16000%2f0635-013.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-bSvX7qrQcUc%2fWCWhDuvxz0I%2fAAAAAAACl0Q%2fu0rqYKgS5DYDTGkmI73WIpP3MW0euH2UACHM%2fs16000%2f0635-014.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-B06HbME4cWc%2fWCWhF-ZHRyI%2fAAAAAAACl0Q%2fZPHAxkeKlQwrWDpYJBnDfBMNsDFRgvn6ACHM%2fs16000%2f0635-015.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-d04D0ZSda48%2fWCWhJlupfSI%2fAAAAAAACl0Q%2fCG7EOwSs3BYoAfH9dkHM5Yd5J3CJyIqzACHM%2fs16000%2f0635-016.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-lIa2sYxypNE%2fWCWhMRsnYwI%2fAAAAAAACl0Q%2fxKVtbiFpBAsk7f5bwchDN1gXo5GFbl1agCHM%2fs16000%2f0635-017.png&imgmax=30000',
                'https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-Y_CFs7twC2g%2fWCWhOTnUnCI%2fAAAAAAACl0Q%2fKDuSBzN_dPcAdzOqPDz75Vu89GbVwwzTwCHM%2fs16000%2f0635-018.png&imgmax=30000',
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


class TestKissmangaSearchByAuthor(VCRTestCase):

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
