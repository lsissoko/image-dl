
__author__ = 'Lamine Sissoko'

import urllib
import os

def download_image(url, name, dest):
    print "\n- Downloading from:\n{}\n\n- In progress ...".format(url)
    filepath = os.path.join(dest, name)
    urllib.urlretrieve(url, filepath)
    print "\n- Saved to:\n{}\n".format(filepath)
