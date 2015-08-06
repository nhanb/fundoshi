How to use
==========


Parse series data
------------------

.. doctest::

    >>> from fundoshi import parse_series
    >>> series = parse_series('http://kissmanga.com/Manga/Sayonara-Football')
    >>> series.name
    'Sayonara Football'
    >>> series.tags
    ['romance', 'school life', 'shounen', 'sports']
    >>> series.description
    ['Onda Nozomi is in ... one day playing in a game.']

    >>> chapter = series.chapters[-1]
    >>> chapter.name
    'Sayonara Football Vol.001 Ch.001: The Entry of an Unmanageable Woman'
    >>> chapter.url
    'http://kissmanga.com/Manga/Sayonara-Football/Vol-001-Ch-001--The-Entry-of-an-Unmanageable-Woman?id=95443'


Parse chapter data
------------------

.. doctest::

    >>> from fundoshi import parse_chapter
    >>> chapter = parse_chapter('http://kissmanga.com/Manga/Naruto/Naruto-333?id=5461')
    >>> chapter.name
    '333'
    >>> chapter.prev_chapter_url
    'http://kissmanga.com/Manga/Naruto/Naruto-332?id=5449'
    >>> chapter.next_chapter_url
    'http://kissmanga.com/Manga/Naruto/Naruto-334?id=5466'
    >>> chapter.series_url
    'http://kissmanga.com/Manga/Naruto'
    >>> chapter.pages
    <generator object ...>
    >>> for page in chapter.pages:
    ...     print(page)
    http://2.bp.blogspot.com/-c_0OX-lXRNk/TlTyVUkVXgI/AAAAAAAAD4g/5dBbTcOpROU/s16000/000.jpg
    http://2.bp.blogspot.com/-RABTsjHeFzo/TlTyXXDPFmI/AAAAAAAAD5c/WX3cEI-PQ0k/s16000/001.jpg
    ...
    http://2.bp.blogspot.com/-OKSL6aBkwi0/TlTzP_RkLmI/AAAAAAAAEE4/tChEbaIr0Mc/s16000/016.jpg


Search series
-------------

.. doctest::

    >>> from fundoshi import search_series
    >>> results = search_series('sayonara football')
    >>> results
    <generator object ...>
    >>> series = next(results)
    >>> series.name
    'Sayonara Football'
    >>> series.url
    'http://kissmanga.com/Manga/Sayonara-Football'

