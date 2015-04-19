from image_dl import download_file, download_album
import os
import sys

"""
Run commands:
    python sample.py
    python sample.py imgbox
    python sample.py imgur
"""


def test(host=""):
    url, name, dest = "", "", "images"
    if host == "":
        print "Downloading image of Homer Simpson...\n"
        download_file("http://bit.ly/1DbCvWt", "homer.jpg", dest)
    else:
        host = host.lower()
        if host == "imgbox":
            url = "http://imgbox.com/g/IKVdGGtXFK"
            name = "imgbox_test"
            dest = os.path.join(dest, "imgbox")
        elif host == "imgur":
            url = "http://imgur.com/a/oa9mI"
            name = "imgur_test"
            dest = os.path.join(dest, "imgur")
        download_album(host, url, name, dest, delim="_")

if __name__ == "__main__":
    host = sys.argv[1] if (len(sys.argv) > 1) else ""
    test(host)
