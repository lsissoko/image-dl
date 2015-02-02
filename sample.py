import image_dl as IMGDL
import sys

def test(host=""):
    host = host.lower()
    if host == "imgbox":
        IMGDL.imgbox("http://imgbox.com/g/IKVdGGtXFK", "nature", "images\imgbox")
    elif host == "imgur":
        IMGDL.imgur("http://imgur.com/a/I5Yfd", "skijump", "images\imgur")
    else:
        print "Downloading image of Homer Simpson...\n"
        IMGDL.download_image("http://bit.ly/1DbCvWt", "homer.jpg", "images")

if __name__ == "__main__":
    host = ""
    if len(sys.argv) > 1:
        host = sys.argv[1]

    test(host)
