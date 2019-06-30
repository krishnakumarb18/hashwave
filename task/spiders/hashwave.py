import scrapy
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://www.globaltrade.net/United-States/expert-service-provider.html',
        "https://www.globaltrade.net"
    ]

    def parse(self, response):
        for providers in response.xpath("//p[@class='sp-name']"):
            endPart = str(providers.xpath("a/@href").extract())
            endPart = endPart[3:-2]
            companyUrl = self.start_urls[1]+endPart
            # print(companyUrl)

            # compDet = response.xpath(companyUrl).extract()
            # compData = response.urljoin(compDet)

            yield scrapy.Request(url=companyUrl,callback=self.parseCompanyPage)

    def parseCompanyPage(self, response):
        print("xxxxxxxx:",response.xpath("//h1/span/text()"))


        # response.xpath("//h1/span/text()]")







            



        # for quote in response.css("div.quote"):
        #     yield { 'out':quote.css("a.href").extract_first(),}
            


# class BrickSetSpider(scrapy.Spider):
#     name = 'brick_spider'
#     start_urls = ['http://www.globaltrade.net/United-States/expert-service-provider.html']

#     def parse(self, response):
#         SET_SELECTOR = '.profileNavigator'

#         for brickset in response.css(SET_SELECTOR):

#             COUNTRY_SELECTOR = brickset.css(SET_SELECTOR).extract_first()

        #     NAME_SELECTOR = 'h1 ::text'
        #     PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
        #     MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
        #     IMAGE_SELECTOR = 'img ::attr(src)'
            # yield {
            #     'country': brickset.xpath(COUNTRY_SELECTOR).extract(),
                # 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                # 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                # 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            # }

        # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )

       