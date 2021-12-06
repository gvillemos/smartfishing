#Downloading weather data using Python as a CSV using the Visual Crossing Weather API
#See https://www.visualcrossing.com/resources/blog/how-to-load-historical-weather-data-using-python-without-scraping/ for more information.
import csv
import codecs
import urllib.request
import ssl

class WeatherOracle:

    weatherData = {}

    def get(self) :
        # Create the URL request
        URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'
        URL += '/55.95705419727239,11.77694151701307'
        URL += '/2021-12-1T12:00:00'
        URL += '/2021-12-1T13:00:00'
        URL += '?unitGroup=metric&key=D3UKY2YTUW67ZRRGSWQFBNQY4&include=obs'

        #Ignore certifications following https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
        ssl._create_default_https_context = ssl._create_unverified_context

        # Parse the results as CSV
        CSVBytes = urllib.request.urlopen(URL)
        CSVText = csv.reader(codecs.iterdecode(CSVBytes, 'utf-8'))

        # Iterate through all rows of the file. For each row, break it down into the columns (separated by a ',').
        # Each field has the format 'key:value'. We split and access these as data[0] and data[1] respectively.
        for Row in CSVText:
            for Column in range(11, 40):
                data = Row[Column].split(':')
                print(data[0], ':', data[1].replace('"', ''))
                self.weatherData[data[0]] = data[1].replace('"', '')

oracle = WeatherOracle()
oracle.get()
