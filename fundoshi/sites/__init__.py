from urllib.parse import urlparse
from .kissmanga import Kissmanga

available_sites = (
    Kissmanga(),
)


# Factory function, return instance of suitable "site" class from url
def get_site(url):
    netloc = urlparse(url).netloc
    for site in available_sites:
        if netloc in site.netlocs:
            return site
    return None
