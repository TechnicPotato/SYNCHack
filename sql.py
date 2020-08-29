import sqlite3
import time
import opportunity

class SQLDB():
    """SQL Database for storing information grabbed"""
    def __init__(self, database_arg=":memory:"):
        self.conn = sqlite3.connect("db.sqllite")
        self.cur = self.conn.cursor()
        self.opID = 0
    
    def execute(self, sql_string):
        """ 
        Handler to allow multiple commands in a statement
        """
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()
    
    def db_setup(self):
        self.cur.execute("""CREATE TABLE Opportunities(
            Id INT,
            company TEXT,
            type TEXT,
            location TEXT,
            application_link TEXT,
            info_link TEXT,
            info TEXT,
            review_score FLOAT,
            review_link TEXT,
            openD TEXT,
            closeD TEXT,
            startD TEXT,
            minsal TEXT,
            maxsal TEXT,
            vacancies INT
        )""")
        self.conn.commit()
    #-----------------------------------
    # Entry addition
    #-----------------------------------
    def add_opportunity(self, opportunity: opportunity):
        """ Adds an opportunity into the DB."""
        sql_cmd = """
                INSERT INTO Opportunities
                VALUES ({id}, '{company}', '{type}', '{location}', '{alink}', '{ilink}', '{info}', {rscore}, '{rlink}', '{opend}', '{closed}', '{startd}', '{minsal}', '{maxsal}', {vac})
                """

        # Filtering to replace numerical values with NULL.
        if (opportunity.vacancies == None):
            opportunity.vacancies = "NULL"
        if (opportunity.review_score == None):
            opportunity.review_score = "NULL"

        sql_cmd = sql_cmd.format(id=self.opID, company=opportunity.company, type=opportunity.o_type, location=opportunity.location,alink=opportunity.application_link,ilink=opportunity.info_link,info=opportunity.info, rscore=opportunity.review_score, rlink=opportunity.link,opend=opportunity.openD, closed=opportunity.closeD,startd=opportunity.start, minsal=opportunity.min, maxsal=opportunity.max, vac=opportunity.vacancies)
        # Add escape char.
        sql_cmd = sql_cmd.replace(":", "\:")
        
        self.cur.execute(sql_cmd)
        self.conn.commit()
        self.opID += 1
    
    def test(self):
        self.cur.execute("""SELECT * FROM Opportunities LIMIT 10""")
        all_rows = self.cur.fetchall()
        return all_rows

    def drop_table(self):
        """Used to reset the table"""
        self.cur.execute("""DROP TABLE Opportunities""")
        self.conn.commit()