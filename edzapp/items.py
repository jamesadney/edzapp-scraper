# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class JobItem(Item):
    position = Field()
    url = Field()
    job_id = Field()
    organization = Field()
    school_name = Field()
    job_type = Field()
    salary = Field()
    is_external = Field()
    date_posted = Field()
    deadline = Field()
