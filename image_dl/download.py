from .utils import (
    create_folder,
    set_name,
    unique_everseen,
    is_valid_url,
    get_html,
    get_elements,
    get_page_links,
    get_image_links,
    get_imagebam_htmlcode_links
)
import os
import re
import sys
import urllib


def download_file(url, name, dest=".", number=1):
    print("  {0}) In: {1}".format(number, url))
    filepath = os.path.join(create_folder(dest), name)
    try:
        res = urllib.request.urlopen(url)
        pic = res.read()
        with open(filepath, 'wb') as f:
            f.write(pic)
    except:
        print("  !!!! FAIL:", url)
    print("  Out: {}\n".format(filepath))


def download_album(host, url, name, dest=".", delim=" - ", digits=3, number=1):
    if not is_valid_url(url):
        sys.exit(1)

    host = host.lower()
    name = name.lower()

    if host == "imagebam":
        imagebam(url, name, dest, delim, digits, number)
    elif host == "imagevenue":
        imagevenue(url, name, dest, delim, digits, number)
    elif host == "imgbox":
        imgbox(url, name, dest, delim, digits, number)
    elif host == "imgur":
        imgur(url, name, dest, delim, digits, number)
    else:
        print("ERROR: Unsupported image host '{}'".format(host))


def imagebam(url, name, dest, delim, digits, number):
    print("Downloading images from [imagebam]...\n")

    # gallery page numbers (ascending)
    pages = [int(el.contents[0])
             for el in get_elements(url, "a.pagination_link")]

    if len(pages) > 0:
        # multi-page gallery
        links = get_imagebam_htmlcode_links(url, pages[-1])
    else:
        # single-page gallery
        links = get_page_links(url, lambda x: "imagebam.com" in x)

    # remove any duplicate links
    links = list(unique_everseen(links))

    # duplicate first link to deal with "Continue to your image"
    if len(links) > 0:
        links.insert(0, links[0])

    regex = re.compile(r'\.[a-zA-Z]*$', re.IGNORECASE)

    from robobrowser import RoboBrowser
    browser = RoboBrowser()

    for link in links:
        try:
            html = browser.open(link)
            image_tags = browser.select('img')
            src = [el['src'] for el in image_tags if 'id' in el.attrs]

            if len(src) > 0:
                image_url = src[0]
                match = regex.search(image_url)
                ext = ".jpg" if match is None else match.group(0)
                new_name = set_name(name, ext, delim, number, digits)
                download_file(image_url, new_name, dest, number)
                number += 1
        except:
            pass


def imgbox(url, name, dest, delim, digits, number):
    print("Downloading images from [imgbox]...\n")

    links = ['https://imgbox.com/' + el['href']
             for el in get_elements(url, '#gallery-view-content a')]

    indexes = list(range(len(links)))
    filenumbers = list(range(number, number + len(links)))

    regex = re.compile(r'(\.[a-zA-Z]*)$', re.IGNORECASE)

    from concurrent.futures import ThreadPoolExecutor

    def download_helper(index, filenumber):
        image_url = [el['src'] for el in get_elements(links[index], '#img')][0]
        ext = regex.search(image_url).group(1)
        filename = set_name(name, ext, delim, filenumber, digits)
        download_file(image_url, filename, dest, filenumber)

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(download_helper, indexes, filenumbers)


def imagevenue(url, name, dest, delim, digits, number):
    print("Downloading images from [imagevenue]...\n")

    links = get_page_links(url, lambda x: "imagevenue.com" in x)

    regex_base_url = re.compile(r'.*imagevenue.com', re.IGNORECASE)
    regex_ext = re.compile(r'\.[a-zA-Z]*$', re.IGNORECASE)

    for link in links:
        try:
            # source image (i.e. "Open image in a new tab")
            img = get_elements(link, "img#thepic")

            base_url_match = regex_base_url.search(link)
            if base_url_match and img is not []:
                src_url = img[0]['src']
                ext = regex_ext.search(src_url).group(0)
                new_name = set_name(name, ext, delim, number, digits)
                image_url = "{0}/{1}".format(base_url_match.group(0), src_url)
                download_file(image_url, new_name, dest, number)
                number += 1
        except:
            pass


def imgur(url, name, dest, delim, digits, number):
    print("Downloading images from [imgur]...\n")

    links = ['https:' + el['src']
             for el in get_elements(url, '.post-image-placeholder, .post-image img')]

    regex = re.compile(r'\.com/\w*(\.[a-zA-Z]*)$', re.IGNORECASE)

    for image_url in links:
        try:
            ext = regex.search(image_url).group(1)
            new_name = set_name(name, ext, delim, number, digits)
            download_file(image_url, new_name, dest, number)
            number += 1
        except:
            pass
