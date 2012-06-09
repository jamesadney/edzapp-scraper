from datetime import datetime

class DjangoJobPipeline(object):
    def process_item(self, item, spider):
        item['deadline'] = datetime.strptime(item['deadline'], '%d/%m/%Y')
        item['date_posted'] = datetime.strptime(item['date_posted'], '%d/%m/%Y')
        item.save()
        return item
