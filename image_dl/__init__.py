
__author__ = 'Lamine Sissoko'

import os
import re
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

def set_name(name, ext, delim, number, digits):
    paddedNumber = format(number, "0%dd" % digits)
    return "{0}{1}{2}{3}".format(name, delim, paddedNumber, ext)
    
def get_html(url):
    r = requests.get(url)
    return BeautifulSoup(r.content)
    
def get_links(url):
    html = get_html(url)
    return [tag['href'] for tag in html.findAll('a', href=True)]

def download_image(url, name, dest=".", number=1):
    print "  {0}) In: {1}".format(number, url)
    filepath = os.path.join(dest, name)
    r = requests.get(url)
    i = Image.open(StringIO(r.content))
    i.save(filepath)
    print "  Out: {}\n".format(filepath)


def imgbox(url, name, dest=".", ext=".jpg", delim="", digits=3, number=1):
  name = name.lower()
  links = get_links(url)
  print "Downloading images from [imgbox]...\n"
  for link in links:
    try:
      new_name = set_name(name, ext, delim, number, digits)
      image_url = "http://i.imgbox.com{0}{1}".format(link, ext)
      download_image(image_url, new_name, dest, number)
      number += 1
    except IOError:
      pass


def imagevenue(url, name, dest=".", ext=".jpg", delim="", digits=3, number=1):
  name = name.lower()

  links = get_links(url)
  links = [link for link in links if re.search(r'imagevenue.com', link)]
  
  print "Downloading images from [imagevenue]...\n"

  for link in links:
    try:
      # Source image (i.e. "Open image in a new tab")
      html = get_html(link)
      src = [tag['src'] for tag in html.findAll('img', src=True) \
          if not str.startswith(str(tag['src']), 'http')]
      
      # Base URL (i.e. http://imgXXX.imagevenue.com)
      base_url_match = re.search(r'.*imagevenue.com', link)
      
      if base_url_match and len(src) > 0:
        new_name = set_name(name, ext, delim, number, digits)
        image_url = "{0}/{1}".format(base_url_match.group(0), str(src[0]))
        download_image(image_url, new_name, dest, number)
        number += 1
    except IOError:
      pass
