from .sites import get_site
from .exceptions import UnsupportedSiteError


def parse_chapter(url):
    site = get_site(url)
    if site is None:
        raise UnsupportedSiteError()
    resp = site.get_chapter_seed_page(url)
    return site.chapter_info(resp.text)


def parse_series(url):
    site = get_site(url)
    if site is None:
        raise UnsupportedSiteError()
    resp = site.get_manga_seed_page(url)
    return site.series_info(resp.text)
