# Intermediate-Web-scraping-Data-Entry-Job-Automation
Intermediate level) Web scraping for Data Entry Job Automation



![zillow](https://user-images.githubusercontent.com/39882035/228649539-30f89952-07ad-42bc-90c6-755e308843c7.gif)




![form](https://user-images.githubusercontent.com/39882035/228649352-cff79db4-e674-44b1-8e3b-2c5b2aa706f7.gif)

This is the ImportData class that utilizes the Selenium web automation library to send data to a Google form. The class has two methods: send_data() and closeWeb().

The __init__() method initializes a Chrome webdriver instance and sets some options such as detaching the browser window.

The send_data() method takes a dictionary argument par which should contain the following keys: "prices", "links", and "addresses". The values associated with these keys should be lists of strings. The method then iterates over the lists, navigates to a Google form, enters the corresponding data from the lists into the form inputs, and submits the form.

The closeWeb() method simply quits the webdriver instance.





![Untitled video - Made with Clipchamp (5)](https://user-images.githubusercontent.com/39882035/228650030-ec12316c-87e3-4dd8-a3a9-3bf191bddc64.gif)




