from urllib.parse import urlparse
from .kissmanga import Kissmanga
from .mangapanda import Mangapanda

_sites = [
    Kissmanga(),
    Mangapanda(),
]

available_sites = {site.name: site for site in _sites}


# Factory function, return instance of suitable "site" class from url
def get_site(url):
    netloc = urlparse(url).netloc
    for site in available_sites.values():
        if netloc in site.netlocs:
            return site
    return None
