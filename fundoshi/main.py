from .sites import get_site, available_sites
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


def search_series(name):
    for site in available_sites.values():
        results = site.search_series(name)
        for series in results:
            yield series


def search_series_from_sites(name, site_names):
    for sname in site_names:
        results = available_sites[sname].search_series(name)
        for series in results:
            yield series


def search_series_from_site(name, site_name):
    site = available_sites[site_name]
    return [series for series in site.search_series(name)]
