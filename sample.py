from image_dl import *

def homer_test():
    url = "http://img2.wikia.nocookie.net/__cb20141025143218/simpsons/images/8/83/Homer_Simpson2.jpg"
    name = "homer.jpg"
    dest = os.getcwd()
    download_image(url, name, dest)
	
if __name__ == "__main__":
	homer_test()