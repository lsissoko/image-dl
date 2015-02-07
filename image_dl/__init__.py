
import os
import re
import requests
import urllib
from BeautifulSoup import BeautifulSoup


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
    
def get_a(url):
    html = get_html(url)
    return [tag['href'] for tag in html.findAll('a', href=True)]

def get_img(url):
  html = get_html(url)
  return [tag['src'] for tag in html.findAll('img', src=True)]

def download_image(url, name, dest=".", number=1):
    print "  {0}) In: {1}".format(number, url)
    filepath = os.path.join(dest, name)
    urllib.urlretrieve(url, filepath)
    print "  Out: {}\n".format(filepath)


def download_album(imagehost, url, name, \
                    dest=".", delim=" - ", digits=3, number=1):
  if len(url) < 1:
    print "invalid URL"
    return
  if url[-1] == "/":
    url = url[:-1]
  name = name.lower()
  dest = create_folder(dest)
  imagehost = imagehost.lower()
  if imagehost == "imagevenue":
    imagevenue(url, name, dest, delim, digits, number)
  elif imagehost == "imgbox":
    imgbox(url, name, dest, delim, digits, number)
  elif imagehost == "imgur":
    imgur(url, name, dest, delim, digits, number)
  elif imagehost == "someimage":
    someimage(url, name, dest, delim, digits, number)
  else:
    print "ERROR: Unsupported image host '{}'".format(imagehost)


def imgbox(url, name, dest, delim, digits, number):
  print "Downloading images from [imgbox]...\n"
  dest = create_folder(dest)
  div = get_html(url).find('div', {"id":"gallery-view-content"})
  links = [str(tag['src']) for tag in div.findAll('img', src=True)]
  for link in links:
    try:
      match = re.search(r'\.com/(\w*)(\.\w*)', link)
      image, ext = match.group(1), match.group(2)
      image_url = "http://i.imgbox.com/" + image
      new_name = set_name(name, ext, delim, number, digits)
      download_image(image_url, new_name, dest, number)
      number += 1
    except:
      pass


def imagevenue(url, name, dest, delim, digits, number):
  print "Downloading images from [imagevenue]...\n"
  links = [link for link in get_a(url) if "imagevenue.com" in link]
  for link in links:
    try:
      # Source image (i.e. "Open image in a new tab")
      img = get_html(link).find('img', {"id" : "thepic"}, src=True)
      base_url_match = re.search(r'.*imagevenue.com', link)
      if base_url_match and img is not None:
        base_url = base_url_match.group(0)
        img_url = img['src']
        ext = re.search(r'\.\w*$', img_url).group(0)
        new_name = set_name(name, ext, delim, number, digits)
        image_url = "{0}/{1}".format(base_url, img_url)
        download_image(image_url, new_name, dest, number)
        number += 1
    except:
      pass


def imgur(url, name, dest, delim, digits, number):
  print "Downloading images from [imgur]...\n"
  dest = create_folder(dest)
  divs = get_html(url).findAll('div', {"class" : \
    "item view album-view-image-link"})
  links = [div.a.get('href') for div in divs]
  for link in links:
    try:
      image_url = "http://" + link[2:]
      ext = re.search(r'\.com/\w*(\.\w*)', image_url).group(1)
      new_name = set_name(name, ext, delim, number, digits)
      download_image(image_url, new_name, dest, number)
      number += 1
    except:
      pass


def someimage(url, name, dest, delim, digits, number):
  print "Downloading images from [someimage]...\n"
  dest = create_folder(dest)
  links = [link for link in get_img(url) if "t1.someimage.com" in link]
  for link in links:
    try:
      match = re.search(r'\.com/(\w*(\.\w*))$', link)
      image, ext = match.group(1), match.group(2)
      new_name = set_name(name, ext, delim, number, digits)
      image_url = "http://i1.someimage.com/" + image
      download_image(image_url, new_name, dest, number)
      number += 1
    except:
      pass
