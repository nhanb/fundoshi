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
    >>> chapter = parse_chapter('http://kissmanga.com/Manga/Naruto/Naruto-333?id=5461')
    >>> chapter.pages
    <generator object ...>

    >>> for page in chapter.pages:
    ...   print(page)
    http://2.bp.blogspot.com/-c_0OX-lXRNk/TlTyVUkVXgI/AAAAAAAAD4g/5dBbTcOpROU/000.jpg?imgmax=10000
    http://2.bp.blogspot.com/-RABTsjHeFzo/TlTyXXDPFmI/AAAAAAAAD5c/WX3cEI-PQ0k/001.jpg?imgmax=10000
    ...
    http://2.bp.blogspot.com/-OKSL6aBkwi0/TlTzP_RkLmI/AAAAAAAAEE4/tChEbaIr0Mc/016.jpg?imgmax=10000
