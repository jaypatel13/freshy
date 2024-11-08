from tools import scraper as scraper

def main():
    scrapy = scraper.Scraper()
    url = "https://www.walmart.ca/en/search?q=sealtest+2%25+4L"
    data = scrapy.scrape(url)

    print (data)

if __name__ == "__main__":
    main()