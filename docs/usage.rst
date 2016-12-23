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
    >>> chapter = parse_chapter('http://kissmanga.com/Manga/Naruto/Naruto-333?id=290537')
    >>> chapter.name
    'Naruto 333'
    >>> chapter.prev_chapter_url
    'http://kissmanga.com/Manga/Naruto/Naruto-332?id=290536'
    >>> chapter.next_chapter_url
    'http://kissmanga.com/Manga/Naruto/Naruto-334?id=290538'
    >>> chapter.series_url
    'http://kissmanga.com/Manga/Naruto'
    >>> chapter.pages
    <generator object ...>
    >>> for page in chapter.pages:
    ...     print(page)
    https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-333%2f001.jpg&imgmax=30000
    https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-333%2f002.jpg&imgmax=30000
    ...
    https://images1-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2fcdn.eatmanga.com%2fmangas%2fManga-Scan%2fNaruto%2fNaruto-333%2f017.jpg&imgmax=30000


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

