import requests
from bs4 import BeautifulSoup



for i in range(1, 30):
    url = 'https://www.trendyol.com/erkek-ayakkabi-x-g2-c114?pi=' + str(i)
    file = open("data.txt", "w")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link_head = "https://www.trendyol.com"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0"}

    for link in soup.find_all("div", attrs={"class": "p-card-chldrn-cntnr card-border"}):
        links = link.a.get('href')
        req = requests.get(link_head + links, headers=header)
        req_soup = BeautifulSoup(req.content, 'html.parser')
        products = req_soup.find_all("div", attrs={"class": "pr-in-cn"})

        for product in products:
            price = product.find("span", attrs={"class": "prc-dsc"}).text
            name = product.find("h1", attrs={"class": "pr-new-br"}).text
            data = name + " = " + price
            file.write("%s\n" % data)
            print(data)

