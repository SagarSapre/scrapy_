# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FirstPipeline:
    def __init__(self):
    ## Connection Details
        hostname = 'localhost'
        port=5432 #5432 for lap 5433 for pc
        username = 'postgres'
        password = '12345678' # your password
        database = 'books'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname,port=port, user=username, password=password, dbname=database)
        

        self.connection.autocommit=True
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes(
            id serial PRIMARY KEY, 
            title text,
            category text,
            description text
        )
        """)

    def process_item(self, item, spider):
        try:
        ## Define insert statement
            self.cur.execute(""" insert into quotes (title, category, description) values (%s,%s,%s)""", (
                item["title"],
                str(item["category"]),
                item["description"]
            ))

            ## Execute insert of data into database
            self.connection.commit()
        except:
            self.connection.rollback()
            raise    
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
