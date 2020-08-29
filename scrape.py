import bot as scraper
import sql

if __name__ == "__main__":
    user = scraper.bot("https://gradaustralia.com.au", "Internship", headless=True)
    # user.default_search()
    # db = sql.SQLDB()
    # db.drop_table()
    # ## Setup initial table
    # db.db_setup()

    # opps = user.scrape_page()
    # for i in opps:
    #     db.add_opportunity(i)
    
    
    
    # conditional = True
    # counter = 0
    # while conditional:
    #     success = user.next_page()
    #     counter += 1
    #     if success:
    #         opps = user.scrape_page()
    #     if counter > 3:
    #         conditional = False
    #     else:
    #         conditional = False
    # print(db.test())

    # Perform via SQL selection instead of any other janky method
    # user.processpage("https://gradaustralia.com.au/graduate-employers/bdo/jobs-internships/2021-undergraduate-business-services-sydney")
    # print("Finished!")
