thonimport json
from extractors.property_parser import PropertyParser
from extractors.utils import Utils
from outputs.exporters import Exporter

class Scraper:
    def __init__(self, search_url, output_file):
        self.search_url = search_url
        self.output_file = output_file

    def run(self):
        # Initialize the parser and utils
        parser = PropertyParser(self.search_url)
        utils = Utils()
        
        # Fetch and parse data
        data = parser.get_property_data()
        
        # Process data
        processed_data = utils.process_data(data)
        
        # Export the data
        exporter = Exporter(self.output_file)
        exporter.export(processed_data)

if __name__ == '__main__':
    scraper = Scraper(search_url='https://www.propertyfinder.ae/en/search?l=6&c=1&fu=0&ob=mr', output_file='output.json')
    scraper.run()