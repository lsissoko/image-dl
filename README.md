# image-dl
Python program for batch image downloading from various hosts (e.g. imagebam, imgbox, etc...).

### To Do
* [x] Single image downloading from a given URL
* [ ] Gallery downloads
    * [ ] imagebam
    * [x] imagevenue
    * [x] imgbox
    * [ ] imgur
    * [ ] someimage
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
#### Download an image
```sh
>>> from image_dl import *
>>> url = "<image_url>"
>>> name = "<file_name>"
>>>
>>> download_image(url, name) # download to current working directory
>>>
>>> dest = create_folder("<dir_name>")
>>> download_image(url, name, dest) # download to chosen directory
```

#### Download a gallery
```sh
>>> from image_dl import *
>>> name = "<file_name>"
>>> dest = create_folder("<dir_name>")
>>>
>>> url = "<imgbox_url>"
>>> imgbox(url, name, dest) # Download imgbox gallery
>>>
>>> url = "<imagevenue_url>"
>>> imagevenue(url, name, dest) # Download imagevenue gallery
```
