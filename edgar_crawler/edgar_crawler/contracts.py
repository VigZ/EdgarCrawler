from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail
from .items import EdgarCrawlerItem

class ResponseCheck(Contract):
    """ Contract which checks the type of items returned.
        @itemtype EdgarCrawlerItem
    """

    name = 'itemtype'

    def post_process(self, output):
        if type(output) is not EdgarCrawlerItem:
                raise ContractFail('Items are not correct type.')
