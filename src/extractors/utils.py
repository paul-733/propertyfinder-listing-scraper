thonclass Utils:
    def process_data(self, data):
        # Simple example of processing data: filter out properties above 1 million AED
        return [property for property in data if int(property['price'].replace('AED', '').replace(',', '').strip()) < 1000000]