.. Fundoshi documentation master file, created by
   sphinx-quickstart on Mon Jun  8 12:59:17 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Fundoshi - The universal manga data extractor
=============================================

Fundoshi is nifty library that lets you search for and extract manga series'
data from many online manga reader websites.

.. doctest::

    >>> from fundoshi import parse_chapter
    >>> chapter = parse_chapter('http://kissmanga.com/Manga/One-Piece/One-Piece-789--Lucy--?id=231238')
    >>> len(chapter['pages'])
    25
