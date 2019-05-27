import argparse
import logging
logging.basicConfig(level=logging.INFO)

import news_page_objects as news

from common import config

logger = logging.getLogger(__name__)

def _new_scraper(new_site_uid):
    host = config()['news_sites'][new_site_uid]['url']
    logger.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(new_site_uid, host)

    for link in homepage.article_links:
        print(link)

if __name__ == "__main__":
    news_sites_choices = list(config()['news_sites'].keys())
    parser = argparse.ArgumentParser()
    parser.add_argument('news_site',
                         help = 'The news site you want to scrape',
                         type = str,
                         choices = news_sites_choices)

    args = parser.parse_args()
    _new_scraper(args.news_site)
