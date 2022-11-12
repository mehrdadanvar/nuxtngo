import requests as r
from bs4 import BeautifulSoup as bs


def get_backend():
    response = r.get("http://localhost:5000")
    print(response.status_code)
    return response.text


data = get_backend()
start = []
end = []
for i in range(len(data)):
    scope = data[i]
    if scope == "{":
        start.append(i)
    elif scope == "}":
        end.append(i)
    else:
        pass
    pass

links = []
for x in range(len(end)):
    links.append(data[start[x]:end[x]])

links = [x.replace("\\", "") for x in links]
final = [x[10:-1] for x in links]

heading = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br"}

status = []
retrieved_pages = []


def get_sites(y):
    for site in y:
        try:
            response = r.get(site, headers=heading)
            print(response.status_code)
            status.append(response.status_code)
            if response.status_code == 200:
                page = bs(response.text, "lxml")
                retrieved_pages.append(page)
            else:
                print("not posible")
        except:
            print("not possible")
            pass
        pass


get_sites(final)


def get_icons(heads):
    rels = [x.select("link") for x in heads]
    hrefs = [x["href"] for x in rels]
    [x[0]["href"] for x in hrefs if len(x) > 0]
