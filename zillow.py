from bs4 import BeautifulSoup
import requests
import lxml
import json

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

class DataFromZillow:
    def __init__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive',
        }



        response = requests.get(url = URL, headers=headers)
        self.htmlFile = response.text
        self.soup = BeautifulSoup(self.htmlFile,"html.parser")

    def getData(self):

        data = self.soup.find_all(name="script", type = "application/json")
        self.data = json.loads( ( (data[1].text).replace("<!--","") ).replace("-->", "") )
        self.data = self.data["cat1"]["searchResults"]["listResults"]

        price = []
        self.links = []
        self.address = []

        for index in range(len(self.data)):

            try:

                price.append(self.data[index]["units"][0]["price"])
                self.address.append(self.data[index]["address"])

                if ("https://www.zillow.com" in self.data[index]['detailUrl']):
                    self.links.append(self.data[index]['detailUrl'])
                else:
                    self.links.append(f"https://www.zillow.com{self.data[index]['detailUrl']}")



            except KeyError:

                price.append(self.data[index]["price"])
                self.address.append(self.data[index]["address"])

                if ("https://www.zillow.com" in self.data[index]['detailUrl']):
                    self.links.append(self.data[index]['detailUrl'])
                else:
                    self.links.append(f"https://www.zillow.com{self.data[index]['detailUrl']}")


        self.price = [index.replace("+","").replace("/mo","")for index in price]

