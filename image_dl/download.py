from utils import (
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
    print "  {0}) In: {1}".format(number, url)
    filepath = os.path.join(create_folder(dest), name)
    urllib.urlretrieve(url, filepath)
    print "  Out: {}\n".format(filepath)


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
    elif host == "someimage":
        someimage(url, name, dest, delim, digits, number)
    elif host == "upix":
        upix(url, name, dest, delim, digits, number)
    elif host == "hotflick":
        hotflick(url, name, dest, delim, digits, number)
    elif host == "myceleb":
        myceleb(url, name, dest, delim, digits, number)
    elif host == "mangastream":
        mangastream(url, name, dest, delim, digits, number)
    else:
        print "ERROR: Unsupported image host '{}'".format(host)


def imagebam(url, name, dest, delim, digits, number):
    print "Downloading images from [imagebam]...\n"

    # gallery page numbers (ascending)
    page_count = [int(el.contents[0])
                  for el in get_elements(url, "a.pagination_link")]

    if page_count:
        # multi-page gallery
        links = get_imagebam_htmlcode_links(url, page_count[-1])
    else:
        # single-page gallery
        links = get_page_links(url, lambda x: "imagebam.com" in x)

    # remove any duplicate links
    links = list(unique_everseen(links))

    regex = re.compile(r'\.[a-zA-Z]*$', re.IGNORECASE)

    for link in links:
        try:
            # source image (i.e. "Open image in a new tab")
            src = [el['src']
                   for el in get_elements(link, 'img')
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
                download_file(image_url, new_name, dest, number)
                number += 1
        except:
            pass


def imgbox(url, name, dest, delim, digits, number):
    print "Downloading images from [imgbox]...\n"

    links = [el['src']
             for el in get_elements(url, '#gallery-view-content img')]

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
            download_file(image_url, new_name, dest, number)
            number += 1
        except:
            pass


def imagevenue(url, name, dest, delim, digits, number):
    print "Downloading images from [imagevenue]...\n"

    links = get_page_links(url, lambda x: "imagevenue.com" in x)

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
                download_file(image_url, new_name, dest, number)
                number += 1
        except:
            pass


def imgur(url, name, dest, delim, digits, number):
    print "Downloading images from [imgur]...\n"

    if not str.endswith(url, "/layout/blog"):
        url += "/layout/blog"

    links = [div.a.get('href') for div in get_elements(
        url, "div.item.view.album-view-image-link")]

    regex = re.compile(r'\.com/\w*(\.[a-zA-Z]*)$', re.IGNORECASE)

    for link in links:
        try:
            # image URL and filetype
            image_url = "http://" + link[2:]
            ext = regex.search(image_url).group(1)

            # output filename
            new_name = set_name(name, ext, delim, number, digits)

            # download
            download_file(image_url, new_name, dest, number)
            number += 1
        except:
            pass


def someimage(url, name, dest, delim, digits, number):
    print "Downloading images from [someimage]...\n"

    links = get_image_links(url, lambda x: "t1.someimage.com" in x)

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
            download_file(image_url, new_name, dest, number)
            number += 1
        except:
            pass


def upix(url, name, dest, delim, digits, number):
    print "Downloading images from [upix]...\n"

    links = [str(tag['href'])
             for tag in get_html(url).findAll('a', {"class": "thumb"})]

    base_url = url
    if str.endswith(url, "/#none"):
        base_url = url[:-5]

    regex = re.compile(r'(\.[a-zA-Z]*)$', re.IGNORECASE)

    for link in links:
        try:
            # image URL and output filename
            image_url = base_url + link
            ext = regex.search(image_url).group(1)
            new_name = set_name(name, ext, delim, number, digits)

            # download
            download_file(image_url, new_name, dest, number)
            number += 1
        except:
            pass


def hotflick(url, name, dest, delim, digits, number):
    print "Downloading images from [hotflick]...\n"
    
    # get all page links if the gallery has more than one page
    div = get_html(url).find('div', {"class": "box-paging"})
    gallery_page_links = [str(tag['href'])
                          for tag in div.findAll('a', href=True)]

    # get image links
    if gallery_page_links != []:
        links = []
        for page in gallery_page_links:
            links.extend([link for link in get_page_links(
                "http://hotflick.net/" + page) if "/v/?q=" in link])
    else:
        links = [link for link in get_page_links(url) if "/v/?q=" in link]

    regex = re.compile(r'\.net/\w/v/\?q\=(\d+)\.(.*)(\.\w*)$', re.IGNORECASE)

    for link in links:
        try:
            # image name and filetype
            match = regex.search(link)
            ext = match.group(3)

            # image URL and output filename
            new_name = set_name(name, ext, delim, number, digits)
            image_url = "http://www.hotflick.net/u/n/{0}/{1}{2}".format(
                match.group(1), match.group(2), ext)

            # download
            download_file(image_url, new_name, dest, number)
            number += 1
        except:
            print "exception"
            pass


def myceleb(url, name, dest, delim, digits, number):
    print "Downloading images from [myceleb]...\n"
    new_url = url.replace("myceleb", "hotflick")
    hotflick(new_url, name, dest, delim, digits, number)


def mangastream(url, name, dest, delim, digits, number):
    print "Downloading images from [mangastream]...\n"

    links = [tag.get('href') for tag in get_html(url).findAll(
        "ul", {"class": "dropdown-menu"})[-1].select('li > a')]
    match = re.search(r"(.*\/)(\d*)$", links[-1])
    base_url, num_pages = match.group(1), int(match.group(2))

    for i in range(1, num_pages + 1):
        try:
            image_url = get_html(
                base_url + str(i)).select("#manga-page")[0].get("src")
            new_name = set_name("", ".jpg", "", i, digits)
            download_file(image_url, new_name, dest, i)
        except:
            print "exception"
            pass
