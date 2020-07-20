from math import pi


class Circle:
    def __init__(self, radius):
        self.radius=radius

    @property
    def area(self):
        print('calculating area')
        return pi*(self.radius**2)


c=Circle(2)
print(c.area)


class Circle:
    def __init__(self, radius):
        self._radius=radius
        self._area=None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._area=None
        self._radius=value

    @property
    def area(self):
        if self._area is None:
            print('calculating area...')
            self._area=pi*(self.radius**2)
        return self._area


c=Circle(3)
print(c.area)
print(c.area)
print(c.area)

c.radius=2
print(c.area)
print(c.area)


######################################
import urllib
from time import perf_counter


class WebPage:
    def __init__(self, url):
        self.url=url
        self._page=None
        self._load_time_secs=None
        self._page_size=None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url=value
        self._page=None

    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self):
        if self._page is None:
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs

    def download_page(self):
        self._page_size=None
        self._load_time_secs=None
        start_time=perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page=f.read()
        end_time=perf_counter()
        self._page_size=len(self._page)
        self._load_time_secs=end_time-start_time


urls=['https://www.google.com/', 'https://ro.yahoo.com/?p=us']

for url in urls:
    page=WebPage(url)
    print(f'{url}\tsize={page.page_size}')