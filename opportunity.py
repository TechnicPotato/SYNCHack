class opportunity:
    """
    The opportunity class holds the information scraped from the GradAustralia website
    """
    def __init__(self, company, o_type, info, info_link, location=None, app = None):
        self.company = company
        self.o_type = o_type
        self.location = location
        self.application_link = app
        self.info = info
        self.info_link

        self.hasreview = False
    
    def review_score(self, score, link):
        self.hasreview = True
        self.review_score = score
        self.link = link
    
    def openDate(self, openD):
        self.openD = openD

    def closeDate(self, closeD):
        self.closeD = closeD

    def startdate(self, start):
        self.start = start

    def mnsalary(self, smin):
        self.min = smin
    
    def mxsalary(self, smax):
        self.max = smax

    def vacancies(self, spots):
        self.vacancies = spots