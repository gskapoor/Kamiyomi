import json

class Source:
    name = ''
    base_url = ''
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url
        return True
    def __init__(self):
        return True

class Shelf:
    manga_stored = []
    def __init__(self, source):
        self.source = source

class Manga:
    url_subset = ''
    chapters = []
    def __init__(self, url_subset):
        self.url_subset = url
    

class Chapter:
    number = 0
    title = ''
    url_subset_ch = ''