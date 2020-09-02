# SYNCHack Writeup
## Product
Product is TERNNER, an internship platform which combines a traditional job aggregation site with a simpler UI to make job searching both easier and quicker than traditional job aggregation sites. Here's some images of the prototype:
![Job Searching Mechanism](/Writeup1.png)
![Job Details](/Writeup2.png)
## Technical Details
Using Python and Selenium, a web scraping bot was built to obtain job details off GradAustralia. This data was then parsed into BeautifulSoup4 for html parsing and then inserted into a SQLite3 server for use in site formatting. Using these details, the bot was additionally tasked with navigation to the main job detail page and scraping the section, which was then parsed into Rake-nltk to identify keywords for use as search parameters. 

### Requirements
Python 3.6 and above. Back end uses SQLite3, Selenium, BeautifulSoup4 and Rake-nltk. 
Front end was built in html.

### Limitations
Due to time limitations, a front end was never properly devised for the product.
Rake-nltk was used due to not requiring training, at the expense of poorer keyword identification.

### Improvements
* Instead of running both Selenium and BS4, BeautifulSoup can be used to scrape and parse html. 
* Building more web scraping bots for additional sites for better data aggregation, from key vendors such as the Big 4 Accounting Firms. 
* Attach a working front end onto the SQL Server
* Run an improved keyword obtaining algorithm, either through Machine Learning or more specific parsing of keywords.
* Add a resume parsing mechanism by the same metrics of keyword parsing.

## What I learnt
Overall, despite the limited time and workarounds, various things were learnt from the experience. 
Several key things I took from this experience:
1. The legal side of webscraping and the prevalence and importance of web scrapers for job aggregation sites and job postings
2. How to build a competent web scraper and how difficult it can be to accurately select meaningful data from sites typically lacking meaningful tags and ids (using XPath)
3. How taxing webscraping small to moderate amounts of data can be without a full fledged scraping mechanism
4. How slow webscraping is, even running headless. Efforts also needed to be taken to consider the hits on a website's server (thus needing inbuilt delay)
5. Importance of proper training or proper adjustment of processing algorithms to obtain meaningful results. Tailoring of such algorithms is necessary.

Overall, I had a great time and much thanks to the SYNCS team and backers for organising the event.

### Minor Stuff
Scraping was done for research purposes only, with no intended commercial use.
