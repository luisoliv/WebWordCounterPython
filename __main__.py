import scrape


# entrypoint of the program
url = "https://en.wikipedia.org/wiki/HNews"
html_src = scrape.get_html_as_string(url)
print(html_src)
