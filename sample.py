import image_dl as IMGDL

def test(host=""):
    host = host.lower()
    if host == "imgbox":
        IMGDL.imgbox("http://imgbox.com/g/IKVdGGtXFK", "nature", "images")
    else:
        print "Downloading image of Homer Simpson...\n"
        IMGDL.download_image("http://bit.ly/1DbCvWt", "homer.jpg", "images")

test()

# test("imgbox")
