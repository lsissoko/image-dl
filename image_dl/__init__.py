
__author__ = 'Lamine Sissoko'

import os
import urllib

def create_folder(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise
    return path

def download_image(url, name, dest=None):
    if dest is None:
        dest = "."
    print "\n- Downloading from:\n{}\n\n- In progress ...".format(url)
    filepath = os.path.join(dest, name)
    urllib.urlretrieve(url, filepath)
    print "\n- Saved to:\n{}\n".format(filepath)
