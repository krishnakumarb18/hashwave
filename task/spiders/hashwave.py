import scrapy
class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    
    start_urls = [
        'https://www.globaltrade.net/United-States/expert-service-provider.html',
        "https://www.globaltrade.net"
    ]
    companyUrl=""

    def parse(self, response):
        for providers in response.xpath("//p[@class='sp-name']"):
            endPart = str(providers.xpath("a/@href").extract())
            endPart = endPart[3:-2]
            self.companyUrl = self.start_urls[1]+endPart
        

            yield scrapy.Request(url=self.companyUrl,callback=self.parseCompanyPage)
            
            
            nextPage=str(response.xpath('.//div[@class="nav-page"]/a[text()="Next >"]/@href').extract_first())    
            actualPage=self.start_urls[1]+nextPage
            if actualPage  :
             yield scrapy.Request(url=actualPage,callback=self.parse)
            
    def parseCompanyPage(self, response):
       
        yield {
             
            'pageUrl':self.companyUrl,
            'logoUrl': response.xpath("normalize-space(.//img[@class='lazy']/@src)").extract_first(),
            'title': response.xpath("normalize-space(.//h1/span/text())").extract_first(),
            'subTitle': response.xpath("normalize-space(.//span[@class='sub']/text())").extract_first(),
            'primaryLocation':response.xpath("normalize-space(.//span[@itemprop='addressLocality']/text())").extract_first(),
            'areaOfExpertise':response.xpath("normalize-space(.//a[@class='mainExp']/text())").extract_first(),
            'about':response.xpath("normalize-space(.//tr[td/text() ='About:']/td/p/text())").extract_first(),
            'website':response.xpath("normalize-space(.//tr[td/text() ='Website:']/td/a/@href)").extract_first(),
            "languageSpoken":response.xpath("normalize-space(.//tr[td/text() ='Languages spoken:']/td[2]/text())").extract_first()
        }


     
        
         
        
            
    
        







            



       