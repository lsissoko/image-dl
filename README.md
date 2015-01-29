# image-dl
Small command-line program to download images from ImageBam and similar image hosting services.


### To Do
- a lot of shit
    - right now it can just grab one image from a given URL


## Installation
Download from github.


## Usage
### Sample Usage
#### Download an image to the current working directory

    >>> from image_dl import *
    >>> url = "<image_url>"
    >>> name = "<file_name>"
    >>> download_image(url, name)
    - Downloading from:
    <image_url>

    - In progress ...

    - Saved to:
    .\<file_name>


#### Download an image to a chosen directory

    >>> from image_dl import *
    >>> url = "<image_url>"
    >>> name = "<file_name>"
    >>> dest = create_folder(<dir_name>)
    >>> download_image(url, name, dest)
    - Downloading from:

    <image_url>
    - In progress ...

    - Saved to:
    <dir_name>\<file_name>