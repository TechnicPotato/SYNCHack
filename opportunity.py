class opportunity:
    """
    The opportunity class holds the information scraped from the GradAustralia website
    """
    def __init__(self, company, o_type, info, location=None, app = None):
        self.company = company
        self.o_type = o_type
        self.location = location
        self.application_link = app
        self.info = info

        self.hasreview = False
    
    def review_score(self, score, link):
        self.hasreview = True
        self.review_score = score
        self.link = link
    
    def dates(self, openD, closeD):
        self.openD = openD
        self.closeD = closeD

    def startdate(self, start):
        self.start = start

    def salary(self, smin, smax):
        self.min = smin
        self.max = smax

    def vacancies(self, spots):
        self.vacancies = spots