#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Rae.py
~~~~~~
Api para los diccionarios de la Real Academia Española.


"""

try:
    from urllib.parse import urlencode, urljoin
    from urllib.error import URLError, HTTPError
    from urllib.request import Request, urlopen
except ImportError:  # python2
    from urllib import urlencode, quote                         # noqa
    from urlparse import urljoin                                # noqa
    from urllib2 import urlopen, Request, URLError, HTTPError   # noqa

from lxml.html import fromstring
from lxml.html import HTMLParser


class NotRegisteredWord(Exception):
    pass


class BaseRae(object):

    @staticmethod
    def get_lemas(html):
        root = fromstring(html, parser=HTMLParser(encoding='utf-8'))
        div_lemas = root.xpath("/html/body/div")
        lemas = []

        if not div_lemas:
            div_suger = root.xpath("/html/body/ul/li/a")
            if div_suger:
                aviso = root.xpath("/html/body/p/span")
                return {
                    'aviso': aviso[0].text_content() if aviso else '',
                    'sugerencias': [s.text_content() for s in div_suger],
                }
            div_aviso = root.xpath("/html/body/p/font")
            if div_aviso:
                return {
                    'aviso': div_aviso[0].text_content(),
                }

        for div_lema in div_lemas:
            lemas.append({
                'id': div_lema.xpath("./a")[0].attrib['name'] if div_lema.xpath("./a") else None,  # id palabra. necesario?
                'lema': div_lema.xpath("./p[1]")[0].text_content(),  # Lema
                'etimologia': div_lema.xpath("./p[2]")[0].text_content() if div_lema.xpath("./p[2]") else None,  # Información etimológica
                'definiciones': [p.text_content() for p in div_lema.xpath("./p[position()>2]") if p.text_content()],  # TODO: manejar lemas internos nopep8
            })
        return lemas

    def search(self, word=None, **kwargs):
        if not word:
            return {'errors': 'You need a to specify a word.'}
        word = word.encode('iso-8859-1')  # necessary for rae server
        params = {
            'type': '3',
            'val_aux': '',
            'origen': 'RAE',
        }
        params.update({self.arg: word})
        qs = urlencode(params)
        url = '{0}?{1}'.format(self.endpoint, qs)
        try:
            response = urlopen(url)
        except HTTPError as e:
            return {'error': 'We failed to reach a server. Reason: {o}'.format(e.reason)}  # nopep8

        except URLError as e:
            return {'error': 'The server couldn\'t fulfill the request. Error code: {0}'.format(e.code)}  # nopep8
        else:
            html = response.read()
            return self.get_lemas(html)


class Drae(BaseRae):
    endpoint = 'http://lema.rae.es/drae/srv/search'
    arg = 'val'


class Dpd(BaseRae):
    endpoint = 'http://lema.rae.es/dpd/srv/search'
    arg = 'key'


if __name__ == '__main__':
    pass
