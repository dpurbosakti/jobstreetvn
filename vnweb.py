import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://www.topcv.vn/tim-viec-lam-cong-nghe-cao-c10009'

    ]

    def parse(self, response):
        for post in response.css('div.row.job'):
            yield {
                'job': post.css('.transform-job-title::text').get(),
                'company': post.css('.text-highlight::text').get(),
                'address': post.css('.address::text').get()
            }

            next_page = response.css('a[rel="next"]::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)

