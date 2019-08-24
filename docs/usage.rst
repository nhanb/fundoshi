How to use
==========

Parse title data
------------------

.. doctest::

    >>> from fundoshi import parse_title
    >>> title = parse_title('https://mangadex.org/title/2597/sayonara-football')
    >>> title.name
    'Sayonara Football'
    >>> title.tags
    ['Comedy', 'Crossdressing', 'Drama', 'Romance', 'School Life', 'Sports']
    >>> title.descriptions
    ["Nozomi wants to enter ... wants to play in?"]
   >>> title.chapters[-1]
   {'id': '84585', 'name': 'Vol. 1 Ch. 1 - The Entry of an Unmanageable Woman'}


Parse chapter data
------------------

.. doctest::

    >>> from fundoshi import parse_chapter
    >>> chapter = parse_chapter('https://mangadex.org/chapter/333636/')

    >>> chapter.name
    'Intermission'

    >>> for page in chapter.pages:
    ...   print(page)
    https://s4.mangadex.org/data/fc5c4d2c2bd416058aef372872c08ca0/D1.png
    https://s4.mangadex.org/data/fc5c4d2c2bd416058aef372872c08ca0/D2.png
    https://s4.mangadex.org/data/fc5c4d2c2bd416058aef372872c08ca0/D3.png
    https://s4.mangadex.org/data/fc5c4d2c2bd416058aef372872c08ca0/D4.png
    https://s4.mangadex.org/data/fc5c4d2c2bd416058aef372872c08ca0/D5.png
    https://s4.mangadex.org/data/fc5c4d2c2bd416058aef372872c08ca0/D6.png
