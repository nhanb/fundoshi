import os

from fundoshi.classes import Chapter, Title
from fundoshi.sites import mangadex

from .common import MangaSiteTestCaseMixin, TestCase


class MangadexTestCase(TestCase, MangaSiteTestCaseMixin):
    site = mangadex
    img_server = ""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._set_img_server()

    @classmethod
    def _set_img_server(cls):
        """
        Mangadex's image server domain may vary depending on client's location.
        """
        if os.environ.get("IGNORE_VCR"):
            img_server = mangadex.session.get(
                "https://mangadex.org/api/?id=333636&type=chapter&baseURL=%2Fapi"
            ).json()["server"]
        else:
            # what's currently in the vcrpy cache:
            img_server = "https://s4.mangadex.org/data/"

        # Populate chapter test cases with actual img server
        for chapter_id, expected in cls.scrape_chapter_cases:
            if expected is not None:
                expected.pages = [
                    page.replace("{{img_server}}", img_server)
                    for page in expected.pages
                ]

    chapter_id_from_url_cases = [
        ("https://mangadex.org/chapter/123", "123"),
        ("https://mangadex.org/chapter/123/", "123"),
        ("https://mangadex.org/title/123", None),
        ("rubbish", None),
    ]
    chapter_url_from_id_cases = [("123", "https://mangadex.org/chapter/123")]
    title_id_from_url_cases = [
        ("https://mangadex.org/title/123", "123"),
        ("https://mangadex.org/title/123/", "123"),
        ("https://mangadex.org/title/123/default-title-name", "123"),
        ("https://mangadex.org/chapter/123", None),
        ("rubbish", None),
    ]
    title_url_from_id_cases = [("123", "https://mangadex.org/title/123")]

    scrape_title_cases = [
        (
            "2597",
            # fmt: off
            Title(
                url="https://mangadex.org/title/2597/sayonara-football",
                name="Sayonara Football",
                alt_names=["Adiós al fútbol", "さよならフットボール", "再见足球"],
                authors=["Arakawa Naoshi"],
                tags=[
                    "Comedy",
                    "Crossdressing",
                    "Drama",
                    "Romance",
                    "School Life",
                    "Sports",
                ],
                publication_status="Completed",
                descriptions=["Nozomi wants to enter the newcomer's competition. But the coach is against it, because their club is a boy's football club and she's... a she. Will she be able to enter the match she wants to play in?"],
                chapters=[
                    {"id": "84598", "name": "Vol. 2 Ch. 8 - Epilogue"},
                    {"id": "84596", "name": "Vol. 2 Ch. 7 - Football Under the Blue Sky"},
                    {"id": "84594", "name": "Vol. 2 Ch. 6 - Everyone in a Crisis"},
                    {"id": "84592", "name": "Vol. 2 Ch. 5 - Clash and Decide"},
                    {"id": "84590", "name": "Vol. 1 Ch. 4 - And There's the Whistle"},
                    {"id": "84589", "name": "Vol. 1 Ch. 3 - A Plan to Become a Regular"},
                    {"id": "84587", "name": "Vol. 1 Ch. 2 - Her Determination at That Time"},
                    {"id": "84585", "name": "Vol. 1 Ch. 1 - The Entry of an Unmanageable Woman"},
                ],
            ),
            # fmt: on
        ),
        (
            "2436",
            # fmt: off
            Title(
                url="https://mangadex.org/title/2436/manhole",
                name="Manhole",
                alt_names=[
                    "Manhole ~Nou wo Kurau Kiseichuu~",
                    "マンホール",
                    "マンホール 〜脳を喰らう寄生虫〜",
                ],
                authors=["Tsutsui Tetsuya"],
                tags=["Horror", "Mystery", "Psychological"],
                publication_status="Completed",
                descriptions=["What do two Japanese detectives, a naked man on a city street, and a roundworm from Botswana all have in common? In the first volume of Manhole, Ken Mizoguchi and Nao Inoue investigate a string of bloody and mysterious murders, but their work uncovers a deadly biological agent which poses a threat of epidemic proportions. An unlikely lead starts them in the pursuit of a mysterious self-titled photographer, but meanwhile the infections keep spreading. The series may be best described as the thrilling combination of a detective story with biological horror."],
                chapters=[
                    {"id": "199912", "name": "Vol. 3 Ch. 28.5 - Epilogue"},
                    {"id": "199911", "name": "Vol. 3 Ch. 28 - Hiroshi Kurokawa"},
                    {"id": "199910", "name": "Vol. 3 Ch. 27 - Epidemic"},
                    {"id": "199909", "name": "Vol. 3 Ch. 26 - Strange Incidents"},
                    {"id": "199908", "name": "Vol. 3 Ch. 25 - Determination"},
                    {"id": "199907", "name": "Vol. 3 Ch. 24 - Ken Mizoguchi"},
                    {"id": "199906", "name": "Vol. 3 Ch. 23 - You were wrong"},
                    {"id": "199905", "name": "Vol. 3 Ch. 22 - The Collaborator"},
                    {"id": "199904", "name": "Vol. 3 Ch. 21 - Menace"},
                    {"id": "199903", "name": "Vol. 3 Ch. 20 - Pursuit"},
                    {"id": "199902", "name": "Vol. 2 Ch. 19 - Oppression"},
                    {"id": "199901", "name": "Vol. 2 Ch. 18 - Coincidence"},
                    {"id": "199900", "name": "Vol. 2 Ch. 17 - Mika Sekiguchi"},
                    {"id": "199899", "name": "Vol. 2 Ch. 16 - Nightmare in Taketoyo DIstrict"},
                    {"id": "199898", "name": "Vol. 2 Ch. 15 - Elimination"},
                    {"id": "199897", "name": "Vol. 2 Ch. 14 - Worst-case Scenario"},
                    {"id": "199896", "name": "Vol. 2 Ch. 13 - Black Fog"},
                    {"id": "199895", "name": "Vol. 2 Ch. 12 - Testimony"},
                    {"id": "199894", "name": "Vol. 2 Ch. 11 - The Second Man (Part 2)"},
                    {"id": "199893", "name": "Vol. 2 Ch. 10 - The Second Man (Part 1)"},
                    {"id": "199892", "name": "Vol. 1 Ch. 9 - Crimes of Conscience"},
                    {"id": "199891", "name": "Vol. 1 Ch. 8 - One-Eyed Family"},
                    {"id": "199890", "name": "Vol. 1 Ch. 7 - The Photographer"},
                    {"id": "199889", "name": "Vol. 1 Ch. 6 - Institution"},
                    {"id": "199888", "name": "Vol. 1 Ch. 5 - Hole"},
                    {"id": "199887", "name": "Vol. 1 Ch. 4 - Infection"},
                    {"id": "199886", "name": "Vol. 1 Ch. 3 - Amamiya Youichi"},
                    {"id": "199885", "name": "Vol. 1 Ch. 2 - Horikawa Yoshito"},
                    {"id": "199884", "name": "Vol. 1 Ch. 1 - Incident"},
                ],
            ),
            # fmt: on
        ),
    ]

    scrape_chapter_cases = [
        (
            "333636",
            Chapter(
                name="Intermission",
                pages=[
                    "{{img_server}}fc5c4d2c2bd416058aef372872c08ca0/D1.png",
                    "{{img_server}}fc5c4d2c2bd416058aef372872c08ca0/D2.png",
                    "{{img_server}}fc5c4d2c2bd416058aef372872c08ca0/D3.png",
                    "{{img_server}}fc5c4d2c2bd416058aef372872c08ca0/D4.png",
                    "{{img_server}}fc5c4d2c2bd416058aef372872c08ca0/D5.png",
                    "{{img_server}}fc5c4d2c2bd416058aef372872c08ca0/D6.png",
                ],
            ),
        ),
        (
            # Deleted chapter
            "679966",
            None,
        ),
    ]
