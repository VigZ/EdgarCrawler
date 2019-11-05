from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import bs4 as bs

from ..items import EdgarCrawlerItem
from ..settings import BASE_URL, BASE_PARAMS
from ..utils import generate_url

class EdgarCrawler(CrawlSpider):
    name = "edgar_crawler"
    allowed_domains = ["sec.gov"]
    start_urls = [generate_url(BASE_URL, BASE_PARAMS)]
    custom_settings = {
    # specifies exported fields and order
    'FEED_EXPORT_FIELDS': [
        "issuer",
        "class_title",
        "cusip",
        "value",
        "shrs_prn_amt",
        "shrs_prn_type",
        "put_call",
        "investment_discretion",
        "other_manager",
        "vote_auth_sole",
        "vote_auth_shared",
        "vote_auth_none",
    ],
    'FEED_URI' : 'scraped_reports/' + BASE_PARAMS['CIK']+'_holdings.tsv'
  }

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[contains(@class,"tableFile2")]/tr[2]'))),

        Rule(LinkExtractor(allow=(), restrict_xpaths=('//tr[5]/td/a[contains(text(),".xml")]'),), callback='create_items',),
    )

    def create_items(self, response):
        soup = bs.BeautifulSoup(response.body,'lxml')
        table_rows = soup.find_all('infotable')

        for row in table_rows:
            field_dict = {
                'issuer':row.nameofissuer.text,
                'class_title': row.titleofclass.text,
                'cusip': row.cusip.text,
                'value': row.value.text,
                'shrs_prn_amt': row.shrsorprnamt.sshprnamt.text,
                'shrs_prn_type': row.shrsorprnamt.sshprnamttype.text,
                'investment_discretion': row.investmentdiscretion.text,
                'vote_auth_sole':row.votingauthority.sole.text,
                'vote_auth_shared':row.votingauthority.shared.text,
                'vote_auth_none':row.votingauthority.none.text,
            }

            # Try problem fields, default to empty string
            try:
                field_dict['put_call'] = row.putcall.text
            except:
                field_dict['put_call'] = ""
            try:
                field_dict['other_manager'] = row.othermanager.text
            except:
                field_dict['other_manager'] = ""

            yield EdgarCrawlerItem(**field_dict)
