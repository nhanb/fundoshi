from .exceptions import UnsupportedSiteError
from .sites import get_site


def parse_chapter(url):
    site = get_site(url)
    if site is None:
        raise UnsupportedSiteError()
    chapter_id = site.chapter_id_from_url(url)
    return site.scrape_chapter(chapter_id)


def parse_title(url):
    site = get_site(url)
    if site is None:
        raise UnsupportedSiteError()
    title_id = site.title_id_from_url(url)
    return site.scrape_title(title_id)
