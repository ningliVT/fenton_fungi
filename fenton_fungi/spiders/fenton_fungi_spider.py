import scrapy

class FentonFungiSpider(scrapy.Spider):
    name = "fenton_fungi_spider"
    # baseurl = 'http://genome.jgi.doe.gov/cgi-bin/getDbSeq?db=Pospl1&searchTabList=protein,proteinHitDesc&hitSeqList='
    baseurl = 'http://genome.jgi.doe.gov/cgi-bin/getDbSeq?db=Wolco1&searchTabList=protein,proteinHitDesc&hitSeqList='
    # build url with interested ids
    start_urls = []
    # read data
    f = open("GSE78007-2FC", "r")
    for line in f:
        start_urls.append(baseurl + line)
        # start_urls.append(baseurl + line.split('_')[0])
    f.close()

    def parse(self, response):
        if response.status == 200: # search found
            with open('results2.txt', 'a') as f:
                f.write(response.xpath('//div[@class="home"]/pre/text()').extract()[0])
