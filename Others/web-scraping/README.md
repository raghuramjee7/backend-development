# Web Scraping

## Pre-requisites
1. Setup venv and install scrapy

## Scrapy
1. Create new project - `scrapy startproject <project_name>`
2. This creates a folder with the project name and the following files:
    - scrapy.cfg
    - items.py
    - middlewares.py
    - pipelines.py
    - settings.py
    - spiders/
3. All the .py files are in a folder called scraper
4. The items.py file is where we define the data structure of the scraped data
5. The spiders folder is where we define the spider classes
6. The middlewares.py, pipelines.py and settings.py files are used to configure the project and define the behaviour of the spider by setting up middlewares and pipelines.
7. To create a new scraper, go to the scrapers folder, and then use the following command - `scrapy genspider <spider_name> <url>`
8. This generates a new spider file and class in the scrapers folder.
9. The spider class has allowed_domains and start_urls attributes. The allowed_domains attribute is a list of domains that the spider is allowed to crawl. This stops the spider from going away from the site. The start_urls attribute is a list of urls that the spider will start crawling from.
10. The spider class also has a parse method which is called when the spider is started. This method is used to parse the response and extract data from it.
11. To run the spider, use the following command - `scrapy crawl <spider_name>`
12. We use ipython shell, install it with pip - `pip install ipython`
13. To run the ipython shell, use the following command - `scrapy shell`
14. To activate the shell, go to scrapy.cfg and add the following line - `shell = ipython`


## Extracting Data
1. To extract data from the response, we use the css or xpath selectors.
2. To extract data using css selectors, use the following command - `response.css('<css_selector>').extract()`
3. To extract data using xpath selectors, use the following command - `response.xpath('<xpath_selector>').extract()`
4. In the css() fuction we pass selectors in the format - class_name, #id_name, tag_name, tag_name.class_name, tag_name#id_name, tag_name[attribute_name=attribute_value], tag_name[attribute_name*=attribute_value], tag_name[attribute_name^=attribute_value], tag_name[attribute_name$=attribute_value]
6. We use .attrib['attribute_name'] to extract the value of an attribute in the tag.
7. We use .get() to extract the value of the tag.
8. We use .getall() to extract the values of all the tags.
9. We can use ::text in the css path to extract the text from the tag.
10. We can use ::attr(attribute_name) in the css path to extract the value of the attribute from the tag.

### Parse data
1. In the spider class, we have a parse function - this has the response object we can extract data from.
```
class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        
        # get all books
        books = response.css("article.product_pod")

        # return each books
        for book in books:
            yield {
                "name": book.css("h3 a::text").get(),
                "price": book.css("p.price_color::text").get(),
            }
        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)
```
2. To run a crawler, we use the following command - `scrapy crawl <spider_name> -o <filename>.<extension>`
3. We need to run this command at the same level as the scrapy.cfg file.
4.  