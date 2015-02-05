import image_dl as IMGDL
import sys

def test(host=""):
    url, name, dest = "", "", "images"
    if host == "":
        print "Downloading image of Homer Simpson...\n"
        IMGDL.download_image("http://bit.ly/1DbCvWt", "homer.jpg", dest)
    else:
        host = host.lower()
        if host == "imgbox":
            url = "http://imgbox.com/g/IKVdGGtXFK"
            name = "imgbox_test"
            dest += "\imgbox"
        elif host == "imgur":
            url = "http://imgur.com/a/I5Yfd"
            name = "imgur_test"
            dest += "\imgur"
        IMGDL.download_album(host, url, name, dest, delim="_")

if __name__ == "__main__":
    host = ""
    if len(sys.argv) > 1:
        host = sys.argv[1]

    test(host)
