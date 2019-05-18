import argparse
import logging
logging.basicConfig(level=logging.INFO)

from common import config

logger = logging.getLogger(__name__)

def _new_scraper(new_site_uid):
    host = config()['new_sites'][new_site_uid]['url']
    logger.info('Beginning scraper for {}'.format(host))

if __name__ == "__main__":
    new_sites_choices = list(config()['new_sites'].keys())
    parser = argparse.ArgumentParser()
    parser.add_argument('new_site',
                         help = 'The news site you want to scrape',
                         type = str,
                         choices = new_sites_choices)

    args = parser.parse_args()
    _new_scraper(args.new_site)
