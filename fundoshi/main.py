from .sites import get_site


def parse_chapter(url):
    site = get_site(url)
    resp = site.get_chapter_seed_page(url)
    return site.chapter_info(resp.text)
