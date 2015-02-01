# image-dl
Python program for batch image downloading from various hosts (e.g. imagebam, imgbox, etc...).

### To Do
* [x] Single image downloading from a given URL
* [ ] Album/Gallery downloads
    * [ ] imagebam
    * [x] imagevenue
    * [x] imgbox
    * [x] imgur
    * [ ] someimage
* [ ] More shit


## Installation
Download from github.

### Dependencies
- Requests
```sh
>>> pip install requests
```
- BeautifulSoup
```sh
>>> pip install beautifulsoup4
```
- Pillow
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

#### Download an album
```sh
>>> from image_dl import *
>>> name = "<file_name>"
>>> dest = create_folder("<dir_name>")
>>>
>>> url = "<imagevenue_url>"
>>> imagevenue(url, name, dest) # download imagevenue album
>>> imagevenue(url, name, dest, delim=' - ') # change delimiter
>>> imagevenue(url, name, dest, digits=6, number=39) # change image sequencing (start at 000039)
>>>
>>> url = "<imgbox_url>"
>>> imgbox(url, name, dest) # download imgbox album
>>>
>>> url = "<imgur_url>"
>>> imgur(url, name, dest) # download imgur album
```
