import re

from scrapy import log
from scrapy.conf import settings
from scrapy.http import FormRequest, Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from edzapp.items import JobItem

class EdZappSpider(BaseSpider):
    name = "edzapp"
    allowed_domains = ["edzapp.com"]
    start_urls = ['https://applicant.edzapp.com/login.aspx']

    def parse(self, response):
        return [FormRequest.from_response(
                            response,
                            formdata={
                                'email': settings['EMAIL'],
                                'password': settings['PASSWORD']
                            },
                            callback=self.get_search)]

    def get_search(self, response):
        return [Request("http://applicant.edzapp.com/default.aspx?page=jobsearch",
                        callback=self.set_100)]

    def set_100(self, response):
        return[FormRequest.from_response(
                            response,
                            formdata={
                                'ctl00$ddlResults': '100',
                                "__EVENTTARGET": 'ctl00$ddlResults',
                                "__EVENTARGUMENT": ''
                            },
                            dont_click=True,
                            callback=self.parse_tables)]

    def parse_tables(self, response):
        hxs = HtmlXPathSelector(response)
        table = hxs.select('//table[@class="resultTable"]')
        rows = table.select('tr[@class="whiteRow" or @class="resultTable"]')

        url_prefix = 'http://applicant.edzapp.com/'
        headers = ['position',
                   'organization',
                   'job_type',
                   'salary',
                   'is_external',
                   'date_posted',
                   'deadline']

        for row in rows:
            job = JobItem()
            values = row.select('td')

            for header, value in zip(headers, values):
                job[header] = ''.join(value.select('.//text()').extract()).strip()
            href = row.select('td/a/@href').extract()[0]
            job['url'] = url_prefix + href
            job['job_id'] = re.search('(\d+)$', href).groups()[0]

            yield job

        # Get next page
        current_page = table.select('tr[last()]//span[1]')
        next_page_href = current_page.select('following-sibling::a[1]/@href')

        if next_page_href:
            eventtarget = next_page_href.re("\('(ctl.+)',")
            yield FormRequest.from_response(
                                  response,
                                  formdata={
                                      "__EVENTTARGET": eventtarget,
                                      "__EVENTARGUMENT": ''
                                  },
                                  dont_click=True,
                                  callback=self.parse_tables)

class EdZappPublicSpider(BaseSpider):
    name = "edzapp-public"
    allowed_domains = ["edzapp.com"]
    start_urls = ['http://applicant.edzapp.com/default.aspx?page=JobSearchFree']

    def parse(self, response):
        return[FormRequest.from_response(
                            response,
                            formdata={
                                'ctl00$ddlResults': '100',
                                "__EVENTTARGET": 'ctl00$ddlResults',
                                "__EVENTARGUMENT": ''
                            },
                            dont_click=True,
                            callback=self.parse_tables)]

    def parse_tables(self, response):
        hxs = HtmlXPathSelector(response)
        table = hxs.select('//table[@id="ctl00_dgrResults"]')
        rows = table.select('tr[@class="DHTR_Grid_Row"]')

        url_prefix = 'http://applicant.edzapp.com/'
        headers = ['position',
                   'organization',
                   'school_name',
                   'job_type',
                   'salary',
                   'is_external',
                   'date_posted',
                   'deadline']

        for row in rows[1:]:
            job = JobItem()
            values = row.select('td')

            for header, value in zip(headers, values):
                job[header] = ''.join(value.select('.//text()').extract()).strip()
            href = row.select('td/a/@href').extract()[0]
            job['url'] = url_prefix + href
            job['job_id'] = re.search('(\d+)$', href).groups()[0]

            yield job

        # Get next page
        current_page = table.select('tr[last()]//span[1]')
        next_page_href = current_page.select('following-sibling::a[1]/@href')

        if next_page_href:
            eventtarget = next_page_href.re("\('(ctl.+)',")
            yield FormRequest.from_response(
                                  response,
                                  formdata={
                                      "__EVENTTARGET": eventtarget,
                                      "__EVENTARGUMENT": ''
                                  },
                                  dont_click=True,
                                  callback=self.parse_tables)
