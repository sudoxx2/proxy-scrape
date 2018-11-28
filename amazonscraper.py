""" Controllers can utilize this class to gather amazon android app data for client
Currently this app can retrieve app title, version, change log, and release date. """

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from proxies import *
import requests


class AmazonScraper:
    """ Class to scrape Amazon Android App websites """

    def __init__(self, site_url):

        # instantiating soup object from BeautifulSoup module
        self.site_url = Request(site_url)
        # bypassing captcha with random user agent
        self.site_url.add_header('User-Agent', ua.random)
        self.source = urlopen(self.site_url).read().decode('utf8')
        self.soup = BeautifulSoup(self.source, 'lxml')

        # instantiating class member variables
        self.app_title = ''
        self.app_version = ''
        self.app_change_log = []
        self.app_release_date = ''

    def get_title(self):
        """ find and return app title from soup object """

        # soup object is unwrapped to find app title
        self.app_title = self.soup.find('span',
                class_='a-size-large a-text-bold').text
        return self.app_title

    def get_version(self):
        """ find and return app version from soup object """

        # soup object is unwrapped to find app version
        tech_details = self.soup.find('div',
                {'id': 'masTechnicalDetails-btf'})
        self.app_version = tech_details.findAll('span')[3].text
        self.app_version = self.app_version.lstrip()
        return self.app_version

    def get_change_log(self):
        """ find and return change log list from soup object """

        # soup object is unwrapped to find change log list
        change_log_container = self.soup.find('div',
                {'id': 'mobileApplicationLatestUpdates_feature_div'})
        change_log_title = change_log_container.h2.text

        # finding all change log table rows dynamically and storing in a list
        change_log_ul = change_log_container.findAll('li')
        for list_item in change_log_ul:
            list_item = list_item.text
            self.app_change_log.append(list_item)
        return self.app_change_log

    def get_release_date(self):
        """ find and return app release date from soup object """

        # soup object is unwrapped to find app release date
        self.app_release_date = self.soup.find('td',
                {'class': 'bucket'})
        self.app_release_date = self.app_release_date.findAll('li')
        self.app_release_date = self.app_release_date[1].text
        return self.app_release_date


if __name__ == '__main__':

    amazon_scraper = AmazonScraper('https://www.amazon.com/dp/B01N9O413M')

    print(amazon_scraper.get_title())
    print(amazon_scraper.get_version())
    print(amazon_scraper.get_change_log())
    print(amazon_scraper.get_release_date())
