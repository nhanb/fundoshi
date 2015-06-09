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
    print('Name:', series.name)
    print('Tags:', series.tags)
    print('Description:', series.description)

    chapter = series.chapters[-1]
    print('\nFirst chapter info')
    print('> Name:', chapter.name)
    print('> Url:', chapter.url)

Output:

.. testoutput:: series

    Name: Sayonara Football
    Tags: ['romance', 'school life', 'shounen', 'sports']
    Description: ['Onda Nozomi is in her second year on the middle school soccer team but has yet to play a single game because she is a girl. Growing up playing soccer, she has the technical skills, endurance and the elegance. However, as a girl, she can’t overcome the physical difference and she can see all her male teammates that she grew up playing soccer with get further and further away from her. Even her younger brother, Junpei, who is also on the team, is starting to rise above her. Coach Samejima sees that Nozomi is an amazing player but because soccer is such a physical sport, he can’t let her play. Nozomi isn’t the kind of girl that just gives up so she practices harder than anyone and drives the team in the hopes of one day playing in a game.']

    First chapter info
    > Name: Sayonara Football Vol.001 Ch.001: The Entry of an Unmanageable Woman
    > Url: http://kissmanga.com/Manga/Sayonara-Football/Vol-001-Ch-001--The-Entry-of-an-Unmanageable-Woman?id=95443


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
