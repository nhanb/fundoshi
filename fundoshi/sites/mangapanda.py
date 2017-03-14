from bs4 import BeautifulSoup
from .utils import cfscraper
from fundoshi.classes import objdict

_get = cfscraper.get
_post = cfscraper.post


class Mangapanda(object):

    netlocs = ['www.mangapanda.com']
    name = 'mangapanda'

    def __init__(self):
        # mangapanda uses a lot of relative paths
        self.base_url = 'http://www.mangapanda.com'

    # Return a list of objdicts that store name, url, and site:
    # [{'name': 'Naruto', 'url': 'http://...', 'site': mangapanda}, ...]
    def search_series(self, keyword):
        url = 'http://www.mangapanda.com/search/'
        params = {
            'w': keyword,
        }
        resp = _post(url, params=params)

        soup = BeautifulSoup(resp.content, 'html.parser')
        manga_names = soup.find_all('div', {'class': 'manga_name'})
        atags = [name.find('h3').a for name in manga_names]
        return [objdict({'name': a.text.strip(),
                         'url': self.base_url + a['href'],
                         'site': self.name}) for a in atags]

    # All kinds of data
    # - name "Naruto"
    # - chapters [{name, url}, {}, ...] - latest first
    # - thumb_url "url"
    # - tags [tag1, tag2, ...]
    # - status "ongoing"/"completed"
    # - descriptions ["paragraph1", "paragraph2", ...]
    # - authors ["Kishimoto Masashi", ...]
    def series_info(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        chapters = self._chapters(soup)
        thumb_url = self._thumbnail_url(soup)
        tags = self._tags(soup)
        name = self._name(soup)
        status = self._status(soup)
        descriptions = self._descriptions(soup)
        authors = self._authors(soup)
        return objdict({
            'site': self.name,
            'chapters': chapters,
            'thumb_url': thumb_url,
            'tags': tags,
            'name': name,
            'status': status,
            'descriptions': descriptions,
            'authors': authors,
        })

    def _chapters(self, soup):
        table = soup.find('table', {'id': 'listing'})
        return [objdict({'url': self.base_url + a['href'],
                         'name': a.string.strip()})
                for a in reversed(table.find_all('a'))]

    def _thumbnail_url(self, soup):
        img_div = soup.find('div', {'id': 'mangaimg'})
        return img_div.find('img')['src']

    def _tags(self, soup):
        tag_list = soup.find(
            'td',
            {'class': 'propertytitle'},
            text='Genre:'
        ).findNext('td')
        tags = tag_list.find_all('a')
        return [text.string.strip().lower() for text in tags]

    def _name(self, soup):
        # <link rel='alternate' title='Naruto manga' ...
        # => must remove the ' manga' part
        title = soup.find('h2', {'class': 'aname'})
        return title.text.strip()

    def _status(self, soup):
        status_td = soup.find(
            'td',
            {'class': 'propertytitle'},
            text='Status:'
        ).findNext('td')
        return status_td.text.strip().lower()

    def _descriptions(self, soup):
        desc_div = soup.find('div', {'id': 'readmangasum'})
        p_tag = desc_div.findNext('p')
        desc = p_tag.text.replace('\r\n', '')
        return [desc]

    def _authors(self, soup):
        # mangapanda lists artists in some cases
        # lets strip these as well as the tags used
        authors = soup.find(
            'td',
            {'class': 'propertytitle'},
            text='Author:'
        ).findNext('td')
        return [authors.text.strip()]

    # Chapter data
    # - name "Naruto Ch.101"
    # - pages [url1, url2, ...] - in ascending order
    # - prev_chapter_url
    # - next_chapter_url
    # - series_url
    def chapter_info(self, html):
        pages = self._chapter_pages(html)
        soup = BeautifulSoup(html, 'html.parser')
        name = self._chapter_name(soup)
        series_url = self._chapter_series_url(soup)
        prev, next = self._chapter_prev_next(soup)
        return objdict({
            'name': name,
            'pages': pages,
            'series_url': series_url,
            'next_chapter_url': next,
            'prev_chapter_url': prev,
        })

    def _chapter_prev_next(self, soup):
        chapter_nav = soup.find('div', {'id': 'mangainfo_bas'}).table
        # There is always a "next page" on Mangapanda even if no release exists
        # so we check every page for the not released notification
        # before setting the next page link
        next_page = chapter_nav.find('span', text='Next Chapter:')
        next_page = self.base_url + next_page.findNext('a')['href']
        look_ahead = _get(next_page)
        look_ahead_soup = BeautifulSoup(look_ahead.text, 'html.parser')
        info = look_ahead_soup.find('div', {'id': 'recom_info'})
        if info and 'not released' in info.text:
            next_page = None
        prev_page = chapter_nav.find('span', text='Previous Chapter:')
        if prev_page:
            prev_page = self.base_url + prev_page.findNext('a')['href']
        return prev_page, next_page

    def _chapter_name(self, soup):
        chapter_info = soup.find('div', {'id': 'mangainfo'})
        chapter_name = chapter_info.h1
        return chapter_name.text.strip()

    def _chapter_pages(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # get last page number
        select_page = soup.find('div', {'id': 'selectpage'})
        last_page = int(select_page.text.strip().rsplit('of ', 1)[-1])

        # get base_url of chapter
        manga_info = soup.find('div', {'id': 'mangainfo_son'})
        chapter_base = manga_info.find('a')['href']

        # generate page urls
        page_urls = []
        for page_num in range(1, last_page + 1):
            page_urls.append('{0}{1}/{2}'.format(self.base_url,
                                                 chapter_base,
                                                 page_num))

        return (self._parse_page(url) for url in page_urls)

    def _parse_page(self, page_url):
        response = _get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # get img url
        img_holder = soup.find('div', {'id': 'imgholder'})
        return img_holder.img['src']

    def _chapter_series_url(self, soup):
        manga_info = soup.find('div', {'id': 'mangainfo_son'})
        a_tag = manga_info.find_all('a')[-1]
        return self.base_url + a_tag['href']

    def search_by_author(self, author):
        # This site simply doesn't support searching by author
        return []

    def get_manga_seed_page(self, url):
        return _get(url)

    def get_chapter_seed_page(self, url):
        # http://www.mangapanda.com/Manga-Name/X
        base = url[:url.rfind('/') + 1]  # http://.../Manga-Name/
        chapter = url.rsplit('/', 1)[-1]  # /X
        return _get(base + chapter, cookies={'vns_readType1': '1'})
