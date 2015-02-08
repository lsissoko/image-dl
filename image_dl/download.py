from utils import *
import os
import re
import requests
import sys
import urllib


def download_image(url, name, dest=".", number=1):
    print "  {0}) In: {1}".format(number, url)
    filepath = os.path.join(dest, name)
    urllib.urlretrieve(url, filepath)
    print "  Out: {}\n".format(filepath)


def download_album(host, url, name, dest=".", delim=" - ", digits=3, number=1):
    if not is_valid_url(url):
        sys.exit(1)

    host = host.lower()
    name = name.lower()
    dest = create_folder(dest)

    if host == "imagevenue":
        imagevenue(url, name, dest, delim, digits, number)
    elif host == "imgbox":
        imgbox(url, name, dest, delim, digits, number)
    elif host == "imgur":
        imgur(url, name, dest, delim, digits, number)
    elif host == "someimage":
        someimage(url, name, dest, delim, digits, number)
    else:
        print "ERROR: Unsupported image host '{}'".format(host)


def imgbox(url, name, dest, delim, digits, number):
    print "Downloading images from [imgbox]...\n"

    links = [el['src'] for el in get_elements(url, '#gallery-view-content img')]

    for link in links:
        try:
            # image name and filetype
            match = re.search(r'\.com/(\w*)(\.[a-zA-Z]*)$', link)
            image, ext = match.group(1), match.group(2)

            # image URL and output filename
            image_url = "http://i.imgbox.com/" + image
            new_name = set_name(name, ext, delim, number, digits)

            # download
            download_image(image_url, new_name, dest, number)
            number += 1
        except:
            pass


def imagevenue(url, name, dest, delim, digits, number):
    print "Downloading images from [imagevenue]...\n"
    
    links = [link for link in get_page_links(url) if "imagevenue.com" in link]
    
    for link in links:
        try:
            # Source image (i.e. "Open image in a new tab")
            img = get_elements(link, "img#thepic")

            base_url_match = re.search(r'.*imagevenue.com', link)
            if base_url_match and img is not []:
                # image name and filetype
                img_url = img[0]['src']
                ext = re.search(r'\.[a-zA-Z]*$', img_url).group(0)

                # image URL and output filename
                new_name = set_name(name, ext, delim, number, digits)
                image_url = "{0}/{1}".format(base_url_match.group(0), img_url)

                # download
                download_image(image_url, new_name, dest, number)
                number += 1
        except:
            pass


def imgur(url, name, dest, delim, digits, number):
    print "Downloading images from [imgur]...\n"

    divs = get_elements(url, "div.item.view.album-view-image-link")
    links = [div.a.get('href') for div in divs]
    
    for link in links:
        try:
            # image URL and filetype
            image_url = "http://" + link[2:]
            ext = re.search(r'\.com/\w*(\.[a-zA-Z]*)$', image_url).group(1)

            # output filename
            new_name = set_name(name, ext, delim, number, digits)

            # download
            download_image(image_url, new_name, dest, number)
            number += 1
        except:
            pass


def someimage(url, name, dest, delim, digits, number):
    print "Downloading images from [someimage]...\n"

    links = [l for l in get_image_links(url) if "t1.someimage.com" in l]

    for link in links:
        try:
            # image name and filetype
            match = re.search(r'\.com/(\w*(\.[a-zA-Z]*))$', link)
            image = match.group(1)
            ext = match.group(2)

            # image URL and output filename
            new_name = set_name(name, ext, delim, number, digits)
            image_url = "http://i1.someimage.com/" + image

            # download
            download_image(image_url, new_name, dest, number)
            number += 1
        except:
            pass
