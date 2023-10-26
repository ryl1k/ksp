from modules.parser import Parser
from modules.output import Output
from modules.changemanager import ChangeManager

class Controller:
    def __init__(self, num_pages, keywords):
        self.num_pages = num_pages
        self.keywords = keywords
        self.base_url = "https://www.nl.go.kr/seoji/contents/S80100000000.do?page={}&pageUnit=10&schType=simple&schStr=웹툰"
        self.results = {}

    def scrape_data(self):
        for page_number in range(1, self.num_pages + 1):
            url = self.base_url.format(page_number)
            parser = Parser(url)

            for keyword in self.keywords:
                site_text = parser.parse_site()
                filtered_data = parser.filter_data_by_keyword(site_text, keyword)
                parsed_data = parser.make_array(filtered_data)

                # Remove lines with numbers and unwanted strings
                parsed_data = [line for line in parsed_data if any(char.isalpha() for char in line) and "제본형태:" not in line]

                if keyword not in self.results:
                    self.results[keyword] = []
                self.results[keyword].extend(parsed_data)

    def output_data(self):
        output = Output(self.results, self.keywords)
        filtered_data = output.prepare_results()

        return filtered_data

    def manage_changes(self):
        change_manager = ChangeManager()
        change_manager.check_and_update(self.output_data())
        change_manager.find_changes()
        change_manager.compare_files('filtered_results.txt', 'previous_results.txt')

if __name__ == "__main__":
    num_pages = 10
    keywords = ["종이책", "전자출판물"]
    
    scraper = Controller(num_pages, keywords)
    scraper.scrape_data()
    filtered_data = scraper.output_data()
    scraper.manage_changes()
