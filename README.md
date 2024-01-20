### There are 3 readmes in this repo. in technical/tech1, technical/tech2, and on root directory. Please check all of them

# About
This is a scraping script intended to scrape items in tokopedia through their search page.

# How To Use
Check the main function and input keyword and how many pages you want to scrape

## tokpedscrape(keyword,pages)  

### Parameters:
- keyword (mandatory, string), insert a keyword to search into the tokopedia website in string type. for example "rockbros"
- pages (mandatory, int), insert an integer to indicate how many pages you want to scrape. If the page number ends before reaching the initial target page, then program will return immediately.  

### Returns:
- returns a dataframe containing the scraped data
- a csv file denoted by keyword and number of pages scraped (same as parameters) will be created automatically within the file directory

Created by Rifky Ariya Pratama for Junior Scraper Technical Test on Magpie 