from bs4 import BeautifulSoup
import requests
import time


def useful(url, root="/"):
    pic_ends = [".jpg", ".jpeg", ".png"]
    for end in pic_ends:
        if url.endswith(end):
            return False
    if url.startswith("/") or url.startswith(root):
        return True
    return False


def new_links(url, url_root=None):
    if url_root is None:
        url_root = url[:url.find("/", 9)]
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                             "/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, features="lxml")

    return [link.get("href") for link in soup.find_all("a") if useful(link.get("href"), url_root)]





