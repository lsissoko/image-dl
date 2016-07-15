# image-dl
Python program for batch image downloading from various hosts (e.g. imagebam, imgbox, etc...).

**NEW**
Added support for manga chapters from [mangastream](http://mangastream.com/).

### Working Hosts
* [imagebam](http://www.imagebam.com/)
* [imagevenue](http://imagevenue.com/)
* [imgbox](http://imgbox.com/)
* [imgur](http://imgur.com/)
* [someimage](https://someimage.com/)
* [upix](http://upix.me/)
* [hotflick](http://www.hotflick.net/)
* [myceleb](http://www.myceleb.net/)
* [sharenxs] (http://sharenxs.com/)
* [mangastream](http://mangastream.com/)

### To Do
* Real error handling
* Parallel downloads


## Installation
Download from Github.

### Dependencies
- [Requests](http://docs.python-requests.org/en/latest/)
```sh
>>> pip install requests
```
- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
```sh
>>> pip install beautifulsoup4
```


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

# download album to current directory
download_album(host, url, name)                      # ["<name>001.xxx", ...]

# download album to "<dest>"
download_album(host, url, name, dest="<dest>")       # ["<dest>\<name>001.xxx", ...]

# download with "_" delimiter
download_album(host, url, name, delim="_")           # ["<name>_001.xxx", ...]

# download with image numbers of length 5
download_album(host, url, name, digits=5)            # ["<name>00001.xxx", ...]

# download with image numbers starting at 17
download_album(host, url, name, number=17)           # ["<name>017.xxx", ...]

# download with all of the changes above:
download_album(host, url, name, dest="<dest>", \
                delim='_', digits=5, number=17)      # ["<dest>\<name>_00017.xxx", ...]
```

## License

MIT. See [LICENSE](https://github.com/primeape91/image-dl/blob/master/LICENSE.txt).
