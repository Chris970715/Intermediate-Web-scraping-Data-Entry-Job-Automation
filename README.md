# Intermediate-Web-scraping-Data-Entry-Job-Automation
Intermediate level) Web scraping for Data Entry Job Automation



![zillow](https://user-images.githubusercontent.com/39882035/228649539-30f89952-07ad-42bc-90c6-755e308843c7.gif)

Zillow code defines a class DataFromZillow that scrapes rental data from the website Zillow.com. 
The __init__ method sets up headers for the GET request and sends a request to the Zillow URL specified. 

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

The getData method extracts the data from the HTML using BeautifulSoup and JSON. It extracts the price, address, and link data from the JSON data and appends it to lists. The price list is then processed to remove any unwanted characters.

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


![form](https://user-images.githubusercontent.com/39882035/228649352-cff79db4-e674-44b1-8e3b-2c5b2aa706f7.gif)

This is the ImportData class that utilizes the Selenium web automation library to send data to a Google form. The class has two methods: send_data() and closeWeb().

The __init__() method initializes a Chrome webdriver instance and sets some options such as detaching the browser window.

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        chrome_driver_path = "C:\python_bot\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)

        self.driver = webdriver.Chrome(service=service, options=options)

The send_data() method takes a dictionary argument par which should contain the following keys: "prices", "links", and "addresses". The values associated with these keys should be lists of strings. The method then iterates over the lists, navigates to a Google form, enters the corresponding data from the lists into the form inputs, and submits the form.

    def send_data(self,par):

        for index in range(len(par["prices"])):
            self.driver.get(par["url"])

            time.sleep(1)
            inputs = self.driver.find_elements(By.CSS_SELECTOR, ".Xb9hP input")
            button = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
            time.sleep(1)

            inputs[0].click()
            inputs[0].send_keys(par["prices"][index])
            inputs[1].click()
            inputs[1].send_keys(par["links"][index])
            inputs[2].click()
            inputs[2].send_keys(par["addresses"][index])

            button.click()

The closeWeb() method simply quits the webdriver instance.

    def closeWeb(self):
        self.driver.quit()

![Untitled video - Made with Clipchamp (5)](https://user-images.githubusercontent.com/39882035/228650030-ec12316c-87e3-4dd8-a3a9-3bf191bddc64.gif)

All of data informed in the google form goes to Google sheet 


