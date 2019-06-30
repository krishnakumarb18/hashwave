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
            # yield{'hai':response.xpath('.//div[@class="nav-page"]/a[5]/@href').extract_first()}
           
        
        

    
            yield scrapy.Request(url=companyUrl,callback=self.parseCompanyPage)

        nextPage=str(response.xpath('.//div[@class="nav-page"]/a[5]/@href').extract_first())    
        actualPage=self.start_urls[1]+nextPage
        if actualPage :
         yield scrapy.Request(url=actualPage,callback=self.parse)
        

    def parseCompanyPage(self, response):
       
        yield {
            'logoUrl': response.xpath(".//img[@class='lazy']/@src").extract_first(),
            'title': response.xpath(".//h1/span/text()").extract_first(),
            'subTitle': response.xpath(".//span[@class='sub']/text()").extract_first(),
            'primaryLocation':response.xpath(".//span[@itemprop='addressLocality']/text()").extract_first(),
            'areaOfExpertise':response.xpath(".//a[@class='mainExp']/text()").extract_first(),
            'about':response.xpath(".//tr[td/text() ='About:']/td/p/text()").extract(),
            'website':response.xpath(".//tr[td/text() ='Website:']/td/a/@href").extract(),
            "languageSpoken":response.xpath(".//tr[td/text() ='Languages spoken:']/td/text()").extract()
        }


     
        
         
        
            
    
        
        # NEXT_PAGE_SELECTOR = './/div[@class="nav-page"]/a[5]/@href'
        # next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #       yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )   







            



       