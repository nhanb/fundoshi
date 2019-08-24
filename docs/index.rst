.. Fundoshi documentation master file, created by
   sphinx-quickstart on Mon Jun  8 12:59:17 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Fundoshi - The universal manga data extractor
=============================================

.. image:: https://builds.sr.ht/~nhanb/fundoshi.svg
    :target: https://builds.sr.ht/~nhanb/fundoshi?

Fundoshi is nifty python library that lets you search for and extract manga
series' data from many online manga reader websites.

**WARNING**: This library is currently in its extremely early stage and under heavy
development. Please check back later if you intend to use it :)


Dependencies
------------

Cloudflare-protected sites (e.g. Kissmanga) require the use of **cfscrape**,
which depends on nodejs. Easiest way to satisfy this is to install nodejs using
your distro's package manager. Debian/Ubuntu users can get by with a simple
``sudo apt-get install nodejs``.

Table of Content
----------------

.. toctree::
   :maxdepth: 3

   dev
   usage
   faq
