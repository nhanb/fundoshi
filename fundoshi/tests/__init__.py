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
