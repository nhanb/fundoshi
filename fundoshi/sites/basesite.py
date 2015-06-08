from requests import get


# Skeleton site. If a site requires special requests (custom headers, etc.)
# then the site implementation should override these methods.
class BaseSite(object):

    get_manga_seed_page = get
    get_chapter_seed_page = get
    get_page_image = get

    def search_by_author(self, author):
        return []
