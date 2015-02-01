
__author__ = 'Lamine Sissoko'

import os
import requests

from BeautifulSoup import BeautifulSoup
from PIL import Image
from StringIO import StringIO


def create_folder(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise
    return path

def pad(number, digits):
    return format(number, "0%dd" % digits)

def set_name(name, extension, delimiter, number):
    return "{0}{1}{2}{3}".format(name, delimiter, number, extension)
    
def get_html(url):
    r = requests.get(url)
    return BeautifulSoup(r.content)
    
def get_links(url):
    html = get_html(url)
    return [tag['href'] for tag in html.findAll('a', href=True)]

def download_image(url, name, destination=".", number=1):
    print "{0}) In: {1}".format(number, url)
    filepath = os.path.join(destination, name)
    r = requests.get(url)
    i = Image.open(StringIO(r.content))
    i.save(filepath)
    print "Out: {}\n".format(filepath)


def imgbox(url, name, destination=".", extension=".jpg", delimiter="", \
            digits=3, number=1):
  name = name.lower()
  destination = create_folder(os.path.join(destination, name))
  links = get_links(url)
  print "Downloading images from [imgbox]...\n"
  for link in links:
    try:
      new_name = set_name(name, extension, delimiter, pad(number, digits))
      image_url = "http://i.imgbox.com{0}{1}".format(link, extension)
      download_image(image_url, new_name, destination, number)
      number += 1
    except IOError:
      pass
