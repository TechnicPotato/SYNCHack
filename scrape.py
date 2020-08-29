import bot as scraper

if __name__ == "__main__":
    user = scraper.bot("https://gradaustralia.com.au/", "Internship", headless=True)
    user.default_search()
    user.scrape_page()
    conditional = True
    while conditional:
        success = user.next_page()
        if success:
            user.scrape_page()
        else:
            conditional = False
    print("Finished!")
