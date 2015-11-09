def _test_series(case, site, url, expected):
    """
    Helper to use in site-specific test cases. See test_kissmanga.py for usage.
    """
    resp = site.get_manga_seed_page(url)
    if resp.status_code != 200:
        raise Exception('Failed to download series html')
    html = resp.text
    series = site.series_info(html)

    chapters = expected.pop('chapters', None)

    for key, val in expected.items():
        case.assertEqual(getattr(series, key), val)

    if chapters is None:
        return
    case.assertEqual(series.chapters[-1], chapters['first'])
    if 'last' in chapters:
        case.assertEqual(series.chapters[0], chapters['last'])


def _test_chapter(case, site, url, expected):
    resp = site.get_chapter_seed_page(url)
    if resp.status_code != 200:
        print('>> Error message from server:')
        print(resp.content)
        raise Exception('Failed to download chapter html')
    html = resp.text
    chapter = site.chapter_info(html)

    # chapter.pages is a generator. Make it a list for easy testing:
    pages_list = [p for p in chapter.pages]
    chapter.pages = pages_list

    for key, val in expected.items():
        case.assertEqual(getattr(chapter, key), val)


def _test_search_by_author(case, site, author_name, expected):
    results = site.search_by_author(author_name)

    for series in expected:
        case.assertIn(series, results)


def _test_search_series(case, site, name, expected):
    results = site.search_series(name)

    for series in expected:
        case.assertIn(series, results)
