import scrapy

# class inherits scrapy.Spider
# scarppers on scrapy are called spiders
class GITSpider(scrapy.Spider):
    # name of spider
    name = 'Udemy'

    # list of urls
    urls = ['https://blog.udemy.com/github-tutorial-how-to-make-your-first-github-repository/?utm_source=adwords&utm_medium=udemyads&utm_campaign=DSA_Catchall_la.EN_cc.ROW&utm_content=deal4584&utm_term=_._ag_88010211481_._ad_535397282064_._kw__._de_c_._dm__._pl__._ti_dsa-39880105563_._li_9061063_._pd__._&matchtype=&gclid=CjwKCAjww7KmBhAyEiwA5-PUStFU7Y-uzAtbEuuKLO-xB92l1We6I-gW_-DowjX9_xoJuUN4sQD0kRoCMzUQAvD_BwE']
    
    # this function is called when request to the website is executed
    def parse(self, response):
        for h2 in response.xpath('//h2'):
            print(h2)