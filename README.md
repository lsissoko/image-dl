# image-dl
Python program for batch image downloading from various hosts (e.g. ImageBam, imgbox, etc...).

### To Do
* [x] Single image downloading from a given URL
* [ ] Gallery downloads
    * [x] imgbox
    * [ ] ImageBam
    * [ ] ImageVenue
* [ ] More shit


## Installation
Download from github.

### Dependencies
- BeautifulSoup
```sh
>>> pip install beautifulsoup4
```
- PIL / Pillow
```sh
>>> pip install Pillow
```


## Usage
### Sample Usage
#### Download an image to the current working directory
```sh
>>> from image_dl import *
>>> url = "<image_url>"
>>> name = "<file_name>"
>>> download_image(url, name)
```

#### Download an image to a chosen directory
```sh
>>> from image_dl import *
>>> url = "<image_url>"
>>> name = "<file_name>"
>>> dest = create_folder(<dir_name>)
>>> download_image(url, name, dest)
```

#### Download an imgbox gallery
```sh
>>> from image_dl import *
>>> url = "<image_url>"
>>> name = "<file_name>"
>>> dest = create_folder(<dir_name>)
>>> imgbox(url, name, dest)
```
