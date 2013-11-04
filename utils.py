#!/usr/local/bin/env python

try:
    from urllib.request import urlopen
    from urllib.request import Request
except ImportError:
    from urllib2 import urlopen
    from urllib2 import Request


def query(url, params=None, headers={}):
    """
    Get the contents of the page at the URL given by url. While making the
    request, we use the headers given in the dictionary in headers.
    """
    result = urlopen(Request(url, params, headers))
    try:
        charset = result.headers.get_content_charset(failobj="utf-8")
    except:
        charset = result.info().getparam('charset') or 'utf-8'
    return result.read().decode(charset)
