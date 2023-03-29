from zillow import DataFromZillow
from importData import ImportData

# SURVEY
SURVEY = "https://docs.google.com/forms/d/e/1FAIpQLSdg3IhosQ2Y502fsQT5BYLdlcIhmJa5JmWNfi9A96U-FTW_SQ/viewform?usp=sf_link"

data = DataFromZillow()
data.getData()

data_send = ImportData()

parameter = {
    "url" : SURVEY,
    "prices" : data.price,
    "links" : data.links,
    "addresses" : data.address
}

data_send.send_data(parameter)
data_send.closeWeb()