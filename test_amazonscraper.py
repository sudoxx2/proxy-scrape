""" unit test for AmazonScraper class """

import unittest
from amazonscraper import AmazonScraper


class TestAmazonScraper(unittest.TestCase):
	""" test all functions in AmazonScraper class """

	def test_get_title(self):
		amazonscraper = AmazonScraper('https://www.amazon.com/dp/B01N9O413M')
		self.assertEqual(amazonscraper.get_title(), 'Vegas Deluxe Slots')

	def test_get_version(self):
		amazonscraper = AmazonScraper('https://www.amazon.com/dp/B01N9O413M')
		self.assertTrue(amazonscraper.get_version())

	def test_get_change_log(self):
		amazonscraper = AmazonScraper('https://www.amazon.com/dp/B01N9O413M')
		self.assertTrue(amazonscraper.get_change_log())

	def test_get_release_date(self):
		amazonscraper = AmazonScraper('https://www.amazon.com/dp/B01N9O413M')
		self.assertEqual(amazonscraper.get_release_date(), 'Original Release Date: January 6, 2017')


if __name__ == "__main__":
	unittest.main()