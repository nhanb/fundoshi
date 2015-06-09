.. Fundoshi documentation master file, created by
   sphinx-quickstart on Mon Jun  8 12:59:17 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Fundoshi - The universal manga data extractor
=============================================

Fundoshi is nifty library that lets you search for and extract manga series'
data from many online manga reader websites.

Parse series data
------------------

Example code:

.. testcode:: series

    from fundoshi import parse_series
    series = parse_series('http://kissmanga.com/Manga/Sayonara-Football')
    for chapter in series.chapters:
        print(chapter.name)
        print(chapter.url + '\n')
    print('Done')

Output:

.. testoutput:: series

    Sayonara Football Vol.002 Ch.008: [End]
    http://kissmanga.com/Manga/Sayonara-Football/Vol-002-Ch-008---End-?id=124898

    Sayonara Football Vol.002 Ch.007 Read Online
    http://kissmanga.com/Manga/Sayonara-Football/Vol-002-Ch-007-Read-Online?id=124897

    Sayonara Football Vol.002 Ch.006: Everything in Crisis
    http://kissmanga.com/Manga/Sayonara-Football/Vol-002-Ch-006--Everything-in-Crisis?id=109410

    Sayonara Football Vol.002 Ch.005: Clash and Decide
    http://kissmanga.com/Manga/Sayonara-Football/Vol-002-Ch-005--Clash-and-Decide?id=95447

    Sayonara Football Vol.001 Ch.004: And There's the Whistle
    http://kissmanga.com/Manga/Sayonara-Football/Vol-001-Ch-004--And-There-s-the-Whistle?id=95446

    Sayonara Football Vol.001 Ch.003: A Plan to Become a Regular!
    http://kissmanga.com/Manga/Sayonara-Football/Vol-001-Ch-003--A-Plan-to-Become-a-Regular-?id=95445

    Sayonara Football Vol.001 Ch.002: Her Determination at that Time
    http://kissmanga.com/Manga/Sayonara-Football/Vol-001-Ch-002--Her-Determination-at-that-Time?id=95444

    Sayonara Football Vol.001 Ch.001: The Entry of an Unmanageable Woman
    http://kissmanga.com/Manga/Sayonara-Football/Vol-001-Ch-001--The-Entry-of-an-Unmanageable-Woman?id=95443

    Done


Parse chapter data
------------------

Code:

.. testcode:: chapter

    from fundoshi import parse_chapter

    chapter = parse_chapter('http://kissmanga.com/Manga/Naruto/Naruto-333?id=5461')
    print(type(chapter.pages))

    for page in chapter.pages:
        print(page)

Output:

.. testoutput:: chapter

    <class 'generator'>
    http://2.bp.blogspot.com/-c_0OX-lXRNk/TlTyVUkVXgI/AAAAAAAAD4g/5dBbTcOpROU/000.jpg?imgmax=10000
    http://2.bp.blogspot.com/-RABTsjHeFzo/TlTyXXDPFmI/AAAAAAAAD5c/WX3cEI-PQ0k/001.jpg?imgmax=10000
    http://2.bp.blogspot.com/-ghaabMpRUlE/TlTyZcu985I/AAAAAAAAD5o/lb6B5734zLM/002.jpg?imgmax=10000
    http://2.bp.blogspot.com/-cyVeM4K87BU/TlTybUFq8JI/AAAAAAAAD58/icrYYxrP3tM/003.jpg?imgmax=10000
    http://2.bp.blogspot.com/-m8-ifLVznLo/TlTyzonV0II/AAAAAAAAD90/2e_RGurMXDY/004.jpg?imgmax=10000
    http://2.bp.blogspot.com/-jMIK3W-m-LI/TlTy1awJlJI/AAAAAAAAD-Y/D2xaYvOs14o/005.jpg?imgmax=10000
    http://2.bp.blogspot.com/-o3ZzqMQHljo/TlTy6krrhHI/AAAAAAAAD-w/6nVWf57bqlM/006.jpg?imgmax=10000
    http://2.bp.blogspot.com/-YRicEjVEkUQ/TlTy8HkVlxI/AAAAAAAAD_k/FvCw-B4f6-s/007.jpg?imgmax=10000
    http://2.bp.blogspot.com/-bErH47T_yeg/TlTy-96R0TI/AAAAAAAAEAQ/X5zh6bvWOus/008.jpg?imgmax=10000
    http://2.bp.blogspot.com/-A7ukGKyD1yM/TlTzAkXdFLI/AAAAAAAAEA0/Nwqiutu85M0/009.jpg?imgmax=10000
    http://2.bp.blogspot.com/-yjQa-iRmAZY/TlTzElAoPwI/AAAAAAAAEBg/HxKI3UlVJxQ/010.jpg?imgmax=10000
    http://2.bp.blogspot.com/-V7oSZiFx1RY/TlTzHlKJqtI/AAAAAAAAECA/5p17vi_8UEk/011.jpg?imgmax=10000
    http://2.bp.blogspot.com/-kUAdaR6n3ac/TlTzIv8D1xI/AAAAAAAAECg/xhRZSnGtC78/012.jpg?imgmax=10000
    http://2.bp.blogspot.com/-gsdDzNLlU9A/TlTzKAxknXI/AAAAAAAAEC4/kPUqKNjJC1I/013.jpg?imgmax=10000
    http://2.bp.blogspot.com/-55NkLOMmjxM/TlTzLWk5cVI/AAAAAAAAEDc/ees9kEQfo4s/014.jpg?imgmax=10000
    http://2.bp.blogspot.com/-aOmUpf-fi9g/TlTzOfM6R8I/AAAAAAAAEEY/lwkERwJ8GVc/015.jpg?imgmax=10000
    http://2.bp.blogspot.com/-OKSL6aBkwi0/TlTzP_RkLmI/AAAAAAAAEE4/tChEbaIr0Mc/016.jpg?imgmax=10000
