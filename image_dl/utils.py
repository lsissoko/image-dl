import os
import requests
from bs4 import BeautifulSoup
from itertools import ifilterfalse


def create_folder(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise
    return path


def set_name(name, ext, delim, number, digits):
    paddedNumber = format(number, "0%dd" % digits)
    return "{0}{1}{2}{3}".format(name, delim, paddedNumber, ext)


def unique_everseen(iterable, key=None):
    """
    http://stackoverflow.com/a/12897501

    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def is_valid_url(url):
    try:
        requests.get(url).raise_for_status()
        return True
    except:
        print "url not valid:", url
        print "exiting..."
        return False


def get_html(url):
    return BeautifulSoup(requests.get(url).content, "html.parser")


def get_elements(url, css):
    return get_html(url).select(css)


def get_page_links(url, cond=None):
    if cond is None:
        return [tag['href'] for tag in get_elements(url, 'a')
                if tag.get('href')]
    else:
        return [tag['href'] for tag in get_elements(url, 'a')
                if tag.get('href') and cond(tag['href'])]


def get_image_links(url, cond=None):
    if cond is None:
        return [tag['src'] for tag in get_elements(url, 'img')
                if tag.get('src')]
    else:
        return [tag['src'] for tag in get_elements(url, 'img')
                if tag.get('src') and cond(tag['src'])]


def get_imagebam_htmlcode_links(url, page):
    """
    ImageBam download helper function.

    Returns the links listed at the bottom of each page in the 'HTML-Code' box.
    """
    if url[-1] == "/":
        url = url[:-1]
    links = []
    for i in range(1, page + 1):
        html = get_html(url + "/" + str(i))
        textareas = [tag for tag in html.findAll('textarea')]
        html = BeautifulSoup(str(textareas[1].contents))
        links.extend([tag['href'] for tag in html.findAll('a', href=True)])
    return links
