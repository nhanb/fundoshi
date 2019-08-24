from attr import attrib, attrs


@attrs(slots=True, kw_only=True)
class Title(object):
    url = attrib(type=str)
    name = attrib(type=str)
    alt_names = attrib(type=list)
    authors = attrib(type=list)
    tags = attrib(type=list)
    publication_status = attrib(type=str)
    descriptions = attrib(type=list)
    chapters = attrib(type=list)


@attrs(slots=True, kw_only=True)
class Chapter(object):
    name = attrib(type=str)
    pages = attrib(type=list)
