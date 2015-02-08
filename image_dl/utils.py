import os
import requests
import urllib
from bs4 import BeautifulSoup

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

def is_valid_url(url):
    try:
        requests.get(url).raise_for_status()
        return True
    except:
        return False
    
def get_html(url):
    r = requests.get(url)
    return BeautifulSoup(r.content)

def get_elements(url, css):
    return get_html(url).select(css)
    
def get_page_links(url):
    return [tag['href'] for tag in get_elements(url, 'a')]

def get_image_links(url):
    return [tag['src'] for tag in get_elements(url, 'img')]