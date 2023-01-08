import requests
from selectorlib import Extractor


class Temperature:

    url_base = 'https://www.timeanddate.com/weather/'
    yaml_url = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        # Creates the url for the country and selected city
        return self.url_base + self.country + '/' + self.city

    def _scrape(self):
        # Extract a value as instructed by the yml file and returns a dictionary

        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yaml_url)
        r = requests.get(url)
        full_content = r.text
        return extractor.extract(full_content)

    def get(self):
        # CLeans the output of _scrape()

        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°C", "").strip())


if __name__ == '__main__':
    temperature = Temperature(country='Italy', city='Firenze')
    print(temperature.get())
