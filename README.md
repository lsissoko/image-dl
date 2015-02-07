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
# required parameters
url = "<img_url>"
name = "<name>"


# download image to current directory
download_image(url, name)


# create new output directory
dest = create_folder("<dest>")

# download album to new output directory
download_image(url, name, dest)
```

#### Album
See "To Do" section above for a list of valid `host` values.

```python
# required parameters
url = "<album_url>"
name = "<name>"
host = "<host>" # (e.g. "imgur", "imgbox")


# download album to current directory
download_album(host, url, name)                      # "<name>001.xxx"


# create new output directory
dest = create_folder("<dest>")

# download album to new output directory
download_album(host, url, name, dest)                # "<dest>\<name>001.xxx"

# download with "_" delimiter
download_album(host, url, name, dest, delim="_")     # "<dest>\<name>_001.xxx"

# download with image numbers of length 5
download_album(host, url, name, dest, digits=5)      # "<dest>\<name>00001.xxx"

# download with image numbers starting at 17
download_album(host, url, name, dest, number=17)     # "<dest>\<name>017.xxx"

# download with all of the changes above:
download_album(host, url, name, dest, '_', 5, 17)    # ["<dest>\<name>_00017.xxx", "<dest>\<name>_00018.xxx", ...]
```
