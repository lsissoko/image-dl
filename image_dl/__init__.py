
__author__ = 'Lamine Sissoko'

import os
import re
import requests
import urllib

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
    urllib.urlretrieve(url, filepath)
    print "  Out: {}\n".format(filepath)


def imgbox(url, name, dest=".", ext=".jpg", delim="", digits=3, number=1):
  dest = create_folder(dest)

  html = get_html(url).find('div', {"id":"gallery-view-content"})
  links = [str(tag['src']) for tag in html.findAll('img', src=True)]

  print "Downloading images from [imgbox]...\n"
  for link in links:
    try:
      image = re.search(r'\.com/(\w*\.\w*)', link).group(1)
      image_url = "http://i.imgbox.com/{}".format(image)
      new_name = set_name(name, ext, delim, number, digits)
      download_image(image_url, new_name, dest, number)
      number += 1
    except:
      pass


def imagevenue(url, name, dest=".", ext=".jpg", delim="", digits=3, number=1):
  dest = create_folder(dest)

  links = [l for l in get_links(url) if re.search(r'imagevenue.com', link)]
  
  print "Downloading images from [imagevenue]...\n"
  for link in links:
    try:
      # Source image (i.e. "Open image in a new tab")
      html = get_html(link)
      src = [tag['src'] for tag in html.findAll('img', src=True) \
          if not str.startswith(str(tag['src']), 'http')]
      
      base_url_match = re.search(r'.*imagevenue.com', link)
      if base_url_match and len(src) > 0:
        new_name = set_name(name, ext, delim, number, digits)
        image_url = "{0}/{1}".format(base_url_match.group(0), str(src[0]))
        download_image(image_url, new_name, dest, number)
        number += 1
    except:
      pass


def imgur(url, name, dest=".", ext=".jpg", delim="", digits=3, number=1):
  dest = create_folder(dest)

  html = get_html(url).findAll('meta', {'property':'og:image'})
  links = [tag['content'] for tag in html][1:]

  print "Downloading images from [imgur]...\n"
  for image_url in links:
    try:
      ext = re.search(r'\.com/\w*(\.\w*)', image_url).group(1)
      new_name = set_name(name, ext, delim, number, digits)
      download_image(image_url, new_name, dest, number)
      number += 1
    except:
      pass