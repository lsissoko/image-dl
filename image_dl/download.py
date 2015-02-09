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

    if host == "imagebam":
        imagebam(url, name, dest, delim, digits, number)
    elif host == "imagevenue":
        imagevenue(url, name, dest, delim, digits, number)
    elif host == "imgbox":
        imgbox(url, name, dest, delim, digits, number)
    elif host == "imgur":
        imgur(url, name, dest, delim, digits, number)
    elif host == "someimage":
        someimage(url, name, dest, delim, digits, number)
    else:
        print "ERROR: Unsupported image host '{}'".format(host)


from bs4 import BeautifulSoup
def imagebam(url, name, dest, delim, digits, number):
    print "Downloading images from [imagebam]...\n"

    # gallery page numbers (ascending)
    page_count = [int(el.contents[0]) \
        for el in get_elements(url, "a.pagination_link")]
    
    if page_count:
        # multi-page gallery
        links = get_imagebam_htmlcode_links(url, page_count[-1])
    else:
        # single-page gallery
        links = [l for l in get_page_links(url) if "imagebam.com" in l]
    
    # remove any duplicate links
    links = list(unique_everseen(links))

    regex = re.compile(r'\.[a-zA-Z]*$', re.IGNORECASE)

    for link in links:
        try:
            # source image (i.e. "Open image in a new tab")
            src = [el['src'] \
                    for el in get_elements(link, 'img') \
                    if 'id' in el.attrs]
            if len(src) > 0:
                # image URL
                image_url = src[0]
                
                # filetype
                ext = regex.search(image_url)
                if ext is None:
                    ext = ".jpg"
                else:
                    ext = ext.group(0)
                    
                # output filename
                new_name = set_name(name, ext, delim, number, digits)

                # download
                download_image(image_url, new_name, dest, number)
                number += 1
        except:
            pass


def imgbox(url, name, dest, delim, digits, number):
    print "Downloading images from [imgbox]...\n"

    links = [el['src'] for el in get_elements(url, '#gallery-view-content img')]

    regex = re.compile(r'\.com/(\w*)(\.[a-zA-Z]*)$', re.IGNORECASE)

    for link in links:
        try:
            # image name and filetype
            match = regex.search(link)
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
    
    regex_base_url = re.compile(r'.*imagevenue.com', re.IGNORECASE)
    regex_ext = re.compile(r'\.[a-zA-Z]*$', re.IGNORECASE)
    
    for link in links:
        try:
            # source image (i.e. "Open image in a new tab")
            img = get_elements(link, "img#thepic")

            base_url_match = regex_base_url.search(link)
            if base_url_match and img is not []:
                # image name and filetype
                img_url = img[0]['src']
                ext = regex_ext.search(img_url).group(0)

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

    regex = re.compile(r'\.com/\w*(\.[a-zA-Z]*)$', re.IGNORECASE)
    
    for link in links:
        try:
            # image URL and filetype
            image_url = "http://" + link[2:]
            ext = regex.search(image_url).group(1)

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

    regex = re.compile(r'\.com/(\w*(\.[a-zA-Z]*))$', re.IGNORECASE)
    
    for link in links:
        try:
            # image name and filetype
            match = regex.search(link)
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
