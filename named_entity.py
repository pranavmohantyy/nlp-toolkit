import re

class NamedEntityRecognizer:
    def __init__(self):
        self.name_pattern = re.compile(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b')
        self.date_pattern = re.compile(r'\b\d{1,2} [A-Za-z]{3,9} \d{4}\b')
        self.location_pattern = re.compile(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b')

    def extract_entities(self, text):
        names = self.name_pattern.findall(text)
        dates = self.date_pattern.findall(text)
        locations = self.location_pattern.findall(text)
        return names, dates, locations
