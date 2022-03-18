import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_amirkhan(site_url):
    ret = []
    r = requests.get(url=site_url, headers=header)
    soup = BeautifulSoup(r.content, features="html.parser")
    gallery = soup.find(
        "div", {"class": "GalleryItems-module__searchContent___DbMmK"})
    link = gallery.find_all("a")
    for i in link:
        ret.append((i.text, i['href']))
    return ret


def download_amirkhan(site_url):
    img_links = []
    r = requests.get(url=site_url, headers=header)
    soup = BeautifulSoup(r.content, features="html.parser")
    gallery = soup.find(
        "img", {"class": "AssetCard-module__image___dams4"})
    img_links.append(gallery['src'])
    print(img_links)
    count = 0
    for img in img_links:
        count += 1
        img_data = requests.get(img).content
        with open(f'Aamir_getty_v2/image_name_{count}.jpg', 'wb') as handler:
            handler.write(img_data)


def main():
    amirlink = get_amirkhan(
        "https://www.gettyimages.in/photos/aamir-khan-actor")
    head = "https://www.gettyimages.in"
    for name, link in amirlink:
        print(link)
        download_amirkhan(head + link)


if __name__ == "__main__":
    main()