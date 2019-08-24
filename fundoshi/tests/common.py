import os

if os.environ.get("IGNORE_VCR"):
    from unittest import TestCase
else:
    from vcr_unittest import VCRTestCase as TestCase

print(f"Using {TestCase.__name__} as base test class.")


class MangaSiteTestCaseMixin:
    # Common unittest settings
    maxDiff = None

    # Case-specific
    site = None
    scrape_title_cases = None
    scrape_chapter_cases = None
    chapter_id_from_url_cases = None
    chapter_url_from_id_cases = None
    title_id_from_url_cases = None
    title_url_from_id_cases = None

    def test_scrape_title(self):
        for title_id, result in self.scrape_title_cases:
            self.assertEqual(self.site.scrape_title(title_id), result)

    def test_scrape_chapter(self):
        for chapter_id, result in self.scrape_chapter_cases:
            self.assertEqual(self.site.scrape_chapter(chapter_id), result)

    def test_chapter_id_from_url(self):
        for chapter_id, result in self.chapter_id_from_url_cases:
            self.assertEqual(self.site.chapter_id_from_url(chapter_id), result)

    def test_chapter_url_from_id(self):
        for chapter_id, result in self.chapter_url_from_id_cases:
            self.assertEqual(self.site.chapter_url_from_id(chapter_id), result)

    def test_title_id_from_url(self):
        for chapter_id, result in self.title_id_from_url_cases:
            self.assertEqual(self.site.title_id_from_url(chapter_id), result)

    def test_title_url_from_id(self):
        for chapter_id, result in self.title_url_from_id_cases:
            self.assertEqual(self.site.title_url_from_id(chapter_id), result)

    # Repetition is dumb but this way I can run these cases in isolation.
    # If someone has a neater solution I'm all ears...
