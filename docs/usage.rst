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
    >>> chapter = parse_chapter('http://kissmanga.com/Manga/Naruto/Chapter-333?id=250065')
    >>> chapter.name
    'Chapter 333'
    >>> chapter.prev_chapter_url
    'http://kissmanga.com/Manga/Naruto/Chapter-332?id=250064'
    >>> chapter.next_chapter_url
    'http://kissmanga.com/Manga/Naruto/Chapter-334?id=250066'
    >>> chapter.series_url
    'http://kissmanga.com/Manga/Naruto'
    >>> chapter.pages
    <generator object ...>
    >>> for page in chapter.pages:
    ...     print(page)
    https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-DSAcvDl8W6I%2fVjIH5IZNaII%2fAAAAAAAFHEo%2fQSGZVRVNpqI%2fs16000%2f0333-001.png&imgmax=30000
    https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-NMP8GeH7HlE%2fVjIHZzox6FI%2fAAAAAAAFG3Q%2fDZlc46p7c_U%2fs16000%2f0333-002.png&imgmax=30000
    ...
    https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&gadget=a&no_expand=1&resize_h=0&rewriteMime=image%2F*&url=http%3a%2f%2f2.bp.blogspot.com%2f-_wSdCpx-0Os%2fVjIEBLePU2I%2fAAAAAAAFFgU%2fsETIDkfGEpQ%2fs16000%2f0333-016.png&imgmax=30000


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

