import os
import urllib.request

data_dir = "LAB6_websites"
pages = [
    {'name': 'wikipedia', 'url': 'https://pl.wikipedia.org'},
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    #{'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}
]

for page in pages:
    try:
        filename = f"{page['name']}.html"
        page_path = os.path.join(data_dir, filename)
        urllib.request.urlretrieve(page['url'], page_path)
    except:
        print("Could not get website "+page['name'])
        break

else:
    print("Success")
