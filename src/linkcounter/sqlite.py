import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("article.db")  # connects to a database called article.db
        self.cur = self.conn.cursor()  # creating a cursor to navigate through the database
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS article (date TEXT, 
                                                   time TEXT, 
                                                   title TEXT PRIMARY KEY, 
                                                   urls TEXT, 
                                                   total_urls INTEGER)
                                                   """)  # creating a table called article
        self.conn.commit()

    def view(self, title):  # To view all the data by article name
        view_list = []
        self.cur.execute("SELECT * FROM article WHERE title = :title", {'title': title})
        for row in self.cur.fetchall():
            view_list.append("{}".format(*row))
        return view_list

    def insert_article(self, article):
        self.cur.execute("INSERT INTO article VALUES (:date, :time, :name, :urls, :total_urls)",
                         {'date': article.date,
                          'time': article.time,
                          'name': article.name,
                          'urls': article.urls,
                          'total_urls': article.total_urls
                          })
        self.conn.commit()

    def get_article_data(self, title):
        article_data_list = []
        self.cur.execute("SELECT urls FROM article WHERE title = :title", {'title': title})
        for row in self.cur.fetchall():
            article_data_list.append("{}".format(*row))
        return article_data_list

    def get_count_of_links(self, title):
        count = 0
        self.cur.execute("SELECT total_urls FROM article WHERE title = :title", {'title': title})
        for row in self.cur.fetchall():
            count = "{}".format(*row)
        return count

    def remove_article(self, title):
        self.cur.execute("DELETE from article WHERE title = :title", {'title': title})
        self.conn.commit()

    def get_all(self):
        self.cur.execute("SELECT * FROM article")
        return self.cur.fetchall()



