import requests
from itertools import product
from string import ascii_lowercase
import eventlet

#------- SETUP SECTION -------
provider = "https://bit.ly/"
output_file = "bitly.txt"
#------- SETUP SECTION -------

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 2)]
file = open(output_file, "w")

for k in keywords:
        try:
                r = requests.head(provider + k, allow_redirects=True, timeout=10)

                if r.history:
                        print(r.url)
                        file.write(r.url + "\n")
        except:
                print("A problem has occurred... lets continue")

file.close()
