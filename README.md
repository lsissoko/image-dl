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
### Download functions
* __`download_image(url, name, [dest[, number]])`__
    * Downloads the image at `url`.
    * Parameters:
        * `url`: album URL
        * `name`: output filename
        * `dest`: (optional) output directory
        * `number`: (optional) used for console logging

* __`download_album(imagehost, url, name, [dest[, ext[, delim[, digits[, number]]]]])`__
    * Downloads the album at `url`.
      * The output filenames will be: "<`name`><`delim`><`number`><`ext`>"
    * Parameters:
        * `imagehost`: album host (e.g. imgur)
        * `url`: album URL
        * `name`: base filename for the downloaded images
        * `dest`: (optional) output directory
        * `ext`: (optional) file extension
        * `delim`: (optional) delimiter separating the image name and number
        * `digits`: (optional) image number length
        * `number`: (optional) starting image number


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
```python
# required parameters
url = "<album_url>"
name = "<name>"
host = "imgur" # set to appropriate host


# download album to current directory
download_album(host, url, name)


# create new output directory
dest = create_folder("<dest>")

# download album to new output directory
download_album(host, url, name, dest)

# download with PNG filetype
download_album(host, url, name, dest, ext='.png')            # "<name>001.png"

# download with "_" delimiter
download_album(host, url, name, dest, delim="_")             # "<name>_001.xxx"

# download with image numbers of length 5
download_album(host, url, name, dest, digits=5)              # "<name>00001.xxx"

# download with image numbers starting at 17
download_album(host, url, name, dest, number=17)             # "<name>017.xxx"

# download with all of the changes above:
download_album(host, url, name, dest, '.png', '_', 5, 17)    # ["<name>_00017.png", "<name>_00018.png", ...]
```
