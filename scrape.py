import bot as scraper
import sql

if __name__ == "__main__":
    user = scraper.bot("https://gradaustralia.com.au", "Internship", headless=True)
    user.default_search()
    db = sql.SQLDB()
    ## Setup initial table
    # db.db_setup()
    print(db.test())

    opps = user.scrape_page()
    for i in opps:
        db.add_opportunity(i)
    
    
    
    # conditional = True
    # while conditional:
    #     success = user.next_page()
    #     if success:
    #         opps = user.scrape_page()
    #     else:
    #         conditional = False
    print("Finished!")
