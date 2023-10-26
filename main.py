import datetime
import time
from controller import Controller


current_time_long = str(datetime.datetime.now())
current_time = current_time_long[:-10]

print("-----------------------------------------------------------")
print("       卐卐卐  卐卐卐   卐卐卐  卐卐卐   卐卐卐  卐卐卐")
print("       卐  卐  卐  卐   卐  卐  卐       卐      卐  卐") 
print("       卐卐卐  卐卐卐   卐卐卐  卐       卐      卐卐卐")
print("       卐      卐  卐   卐 卐   卐卐卐   卐卐卐  卐 卐") 
print("       卐      卐  卐   卐  卐      卐   卐      卐  卐") 
print("       卐      卐  卐   卐   卐 卐卐卐   卐卐卐  卐   卐")
print("-----------------------------------------------------------")
print(f"--------------------{current_time}-----------------------")
print("-----------------------------------------------------------")
time.sleep(0.8)
print("Started modules")
print("Starting controller")
if __name__ == "__main__":
    num_pages = 10
    keywords = ["종이책", "전자출판물"]
    
    scraper = Controller(num_pages, keywords)
    scraper.scrape_data()
    filtered_data = scraper.output_data()
    scraper.manage_changes()
