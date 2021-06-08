import urllib.request


def get_html_as_string(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def scrape_site(url):
    print(url)
    return
