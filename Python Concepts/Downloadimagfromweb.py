import random
import urllib.request

def download_image(url):
    name = random.randrange(1,100)
    full_file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_file_name)



download_image("https://images.app.goo.gl/uxwikB93MaGenvkd8")
