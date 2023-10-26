import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, url):
        self.url = url

    def parse_site(self):
        # Send an HTTP request to the URL
        response = requests.get(self.url)

        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract and return all text from the site
            return soup.get_text()
        else:
            return None

    def filter_data_by_keyword(self, text, keyword):
        # Split the text into lines
        lines = text.split('\n')
        # Filter lines containing the keyword but not including [전자출판물 array] and [종이책 array]
        filtered_lines = [line.strip() for line in lines if keyword in line and line != f"[{keyword} array]"]
        return filtered_lines

    def make_array(self, filtered_data):
        parsed_data = []
        skip_next = False
        for line in filtered_data:
            if line == "[Cartoon] Me and Tiger! Set":
                skip_next = not skip_next
                continue
            if not skip_next:
                if line:
                    parsed_data.append(line)
        return parsed_data