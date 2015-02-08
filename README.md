# image-dl
Python program for batch image downloading from various hosts (e.g. imagebam, imgbox, etc...).

### To Do
* [x] Single image downloading from a given URL
* [ ] Album/Gallery downloads
    * [ ] imagebam
    * [x] imagevenue
    * [x] imgbox
    * [x] imgur
    * [x] someimage
    * [ ] upix


## Installation
Download from Github and import `image_dl`.

### Dependencies
- Requests
```sh
>>> pip install requests
```
- BeautifulSoup
```sh
>>> pip install beautifulsoup4
```


## Usage

### Examples

#### Image
```python
# import
from image_dl import download_image

# required parameters
url = "<img_url>"
name = "<name>"

# download image to current directory
download_image(url, name)

# download image to "\img" directory
download_image(url, name, "img")
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
download_album(host, url, name)                      # first image = "<name>001.xxx"


# download album to "\img" directory
download_album(host, url, name, "img")               # first image = "img\<name>001.xxx"

# download with "_" delimiter
download_album(host, url, name, delim="_")           # first image = "<name>_001.xxx"

# download with image numbers of length 5
download_album(host, url, name, digits=5)            # first image = "<name>00001.xxx"

# download with image numbers starting at 17
download_album(host, url, name, number=17)           # first image = "<name>017.xxx"

# download with all of the changes above:
download_album(host, url, name, "img", '_', 5, 17)   # first image = "images\<name>_00017.xxx"
```
