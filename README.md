# image-dl
Python program for batch image downloading from various hosts (e.g. imagebam, imgbox, etc...).

### Working Hosts
* [imagebam](http://www.imagebam.com/)
* [imagevenue](http://imagevenue.com/)
* [imgbox](http://imgbox.com/)
* [imgur](http://imgur.com/)

### To Do
* Real error handling
* ~Parallel downloads~ (only imgbox is complete)

        Test Results (note: single test run because lazy)

        url: http://imgbox.com/g/IKVdGGtXFK
        count: 22
        size: 29.3 MB

        duration before: 75.85 seconds
        duration after: 20.48 seconds


## Installation
Download from Github.

### Requirements
- Python (3.3 or later)
- [Requests](http://docs.python-requests.org/en/latest/) -- `$ pip install requests`
- [RoboBrowser](https://github.com/jmcarp/robobrowser) -- `$ pip3 install robobrowser`


## Usage

### Examples

Take a look at `sample.py` or read below.

#### Image
```python
# import
from image_dl import download_file

# required parameters
url = "<img_url>"
name = "<name>"

# download image to current directory
download_file(url, name)

# download image to "<dest>"
download_file(url, name, "<dest>")
```

#### Album
See "To Do" section above for a list of valid `host` values.
```python
# import
from image_dl import download_album

# required parameters
url = "<album_url>"
name = "<name>"
host = "<host>" # (e.g. "imgur", "imgbox")

# optional parameters
dest = "<dest>"
delim = "_"
digits = 5
number = 17

# download album to current directory
download_album(host, url, name)

# download album to "<dest>"
download_album(host, url, name, dest=dest)

# download with "_" delimiter
download_album(host, url, name, delim=delim)

# download with image numbers of length 5
download_album(host, url, name, digits=digits)

# download with image numbers starting at 17
download_album(host, url, name, number=number)

# download with all of the changes above:
download_album(host, url, name, dest=dest, delim=delim, digits=digits, number=number)
```
